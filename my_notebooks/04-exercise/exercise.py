import numpy as np, matplotlib.pyplot as plt

# 1. Open the file './data/befkbhalderstatkode.csv'
filename = '../../data/befkbhalderstatkode.csv'
# 2. 2. Turn the csv file into a numpy ndarray with `np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)`
kbh_data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)


def number_of_people_per_neighbourhood(neighborhood, year_mask, age_mask=True, country_mask=True):
    all_people_in_given_n = kbh_data[year_mask & (kbh_data[:, 1] == neighborhood) & age_mask & country_mask]
    sum_of_people = all_people_in_given_n[:, 4].sum()  # index 4 is no of 'PERSONER'
    return sum_of_people


# 3. Using this data:
hoods = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
         5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
         10: 'Amager Vest', 99: 'Udenfor'}

mask_2015 = (kbh_data[:, 0] == 2015)

people_in_2015 = np.array([number_of_people_per_neighbourhood(
    n, mask_2015) for n in hoods.keys()])
print(f"People per neighborhood in copenhagen 2015: {people_in_2015}")

# 4. Make a bar plot to show the size of each city area from the smallest to the largest in 2015
# plt.bar(hoods.values(), people_in_2015, width=0.5, align='center', color='blue')
# plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
# plt.show()

# 5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
# added age mask for function
above_65 = (kbh_data[:, 2] > 65)
people_above_65 = np.array([number_of_people_per_neighbourhood(
    n, mask_2015, above_65) for n in hoods.keys()])

print(f"People above 65 in neighborhoods in copenhagen 2015: {people_above_65}")
# 6. How many of those were from the other nordic countries (not dk). Hint: see notebook: "04 Numpy"
nordic_countries = {5101: "Grønland", 5106: "Island", 5110: "Norge", 5120: "Sverige", 5130: "Finland"}
old_nords = 0
for key, value in nordic_countries.items():
    print(value)
    _mask = (kbh_data[:, 3] == key)
    sum_of_oldies = np.array(
        [number_of_people_per_neighbourhood(n, mask_2015, above_65, _mask) for n in hoods.keys()]).sum()
    print(sum_of_oldies)
    old_nords += sum_of_oldies

print(f"Nordic people above 65 in copenhagen 2015: {old_nords}")
# 7. Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015
mask_1992 = (kbh_data[:, 0] == 1992)
# Vesterbro 1992
vesterbro_1992 = np.array([number_of_people_per_neighbourhood(4, mask_1992)])
print(vesterbro_1992.sum())
# Vesterbro_2015
vesterbro_2015 = np.array([number_of_people_per_neighbourhood(4, mask_2015)])
print(vesterbro_2015.sum())
# Østerbro_1992
easterbronx_1992 = np.array([number_of_people_per_neighbourhood(2, mask_1992)])
print(easterbronx_1992.sum())
# Østerbro_2015
easterbronx_2015 = np.array([number_of_people_per_neighbourhood(2, mask_2015)])
print(easterbronx_2015.sum())

def getVesterbro():
    years = [1992 + i for i in range(2016 - 1992)]
    vesterbro_people = []
    for year in years:
        mask_years = (kbh_data[:, 0 ] == year)
        vesterbro_people.append(np.array([number_of_people_per_neighbourhood(4, mask_years)]).sum()) #4 for local area code

    print(vesterbro_people)

    return vesterbro_people


def getEasterbro():
    years = [1992 + i for i in range(2016 - 1992)]
    easterbro_people = []
    for year in years:
        mask_years = (kbh_data[:, 0] == year)
        easterbro_people.append(np.array([number_of_people_per_neighbourhood(2, mask_years)]).sum()) #2 for local area code

    print(easterbro_people)

    return easterbro_people


# Mies løsning
def line_plot():
    years = [1992 + i for i in range(2016 - 1992)]
    vesterbronx = [number_of_people_per_neighbourhood(4, ((kbh_data[:, 0] == year) & (kbh_data[:, 2] > 65))) for year in
                   years]
    easterbronx = [number_of_people_per_neighbourhood(2, ((kbh_data[:, 0] == year) & (kbh_data[:, 2] > 65))) for year in
                   years]
    plt.plot(years, vesterbronx, label="Vesterbro")
    plt.plot(years, easterbronx, label="Østerbro")
    plt.legend()
    plt.show()


# line_plot()

# Plotting time
# 1992 Plot

def plot_1992():
    years_of_interest_1992 = [1992, 1992]
    plt.axis([0, max(years_of_interest_1992) + 10, 0, 76000])
    title = 'Citizens in Vesterbro / Østerbro 1992'
    p1 = plt.bar(years_of_interest_1992, vesterbro_1992.sum(), width=100, align='center', color='red')
    p2 = plt.bar(years_of_interest_1992, easterbronx_1992.sum(), width=100, align='center', color='yellow')

    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("Citizens", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.legend([p1, p2], ['Vesterbro', 'Østerbro'], loc=1)
    plt.show()

# Won't work lol

# 2015 Plot

def plot_2015():
    years_of_interest_2015 = [2015, 2015]
    plt.axis([0, max(years_of_interest_2015) + 10, 0, 76000])
    title = 'Citizens in Vesterbro / Østerbro 2015'
    p1 = plt.bar(vesterbro_2015.sum(), years_of_interest_2015, width=0.5, align='center', color='red')
    p2 = plt.bar(easterbronx_2015.sum(), years_of_interest_2015, width=0.5, align='center', color='yellow')

    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("Citizens", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.legend([p1, p2], ['Vesterbro', 'Østerbro'], loc=1)
    plt.show()


#plot_1992()
#plot_2015()
#line_plot()

def new_solution():
    years = [1992 + i for i in range(2016-1992)]

    vesterbro_peeps = getVesterbro()
    easterbro_peeps = getEasterbro()

    x_axis = np.arange(len(years))

    plt.bar(x_axis - 0.2, vesterbro_peeps, 0.4, label='Vesterbro')
    plt.bar(x_axis + 0.2, easterbro_peeps, 0.4, label='Østerbro')

    plt.xticks(x_axis, years, rotation=45)
    plt.xlabel("Population")
    plt.ylabel("Number of Citizens")
    plt.title("Number of Students in Vesterbro and Østerbro")
    plt.legend()
    plt.show()


new_solution()