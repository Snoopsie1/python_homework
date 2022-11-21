import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale

# TODO: Part 1
# TODO: 1) Feature space from csv file. Read data/ds_salaries.csv into a pandas dataframe
data = pd.read_csv('../../data/ds_salaries.csv')

# TODO: 2) Prune the dataset to only have columns:
#  "work_year", "experience_level", "salary_in_usd", "job_title", "company_location", "company_size".
pruned_data = data[['work_year', 'experience_level', 'salary_in_usd', 'job_title', 'company_location', 'company_size']]
print("To prove pruning worked.")
print(f"Amount of columns in csv data: {len(data.columns)}")
print(f"Amount of columns in pruned data: {len(pruned_data.columns)}")

# TODO: 3) Onehot Encode "experience_level".
#  Hint: look up pandas: get_dummies() method.
one_hotted_pd = pd.get_dummies(pruned_data['experience_level'], prefix='experience_level')
print(one_hotted_pd.head())

# TODO: 4) Label Encode "company_location"
label_pd = pruned_data[['company_location']].apply(LabelEncoder().fit_transform)
print(label_pd)

# TODO: 5) Normalize the company_location number (relative value between 0-1)
#  X_norm = (x - x_Min) / (x_Max - x_Min) // Or just use preprocessing.MinMaxScaler()
scaler = preprocessing.MinMaxScaler()
names = label_pd.columns
d = scaler.fit_transform(label_pd)
scaled_df = pd.DataFrame(d, columns=names)
print(scaled_df)

# TODO: 6) Make binning of the salary column (both cut and qcut methods).
# cut()
pruned_data['cut'] = pd.cut(pruned_data['salary_in_usd'], bins=5)
print(pruned_data['cut'].value_counts())
# qcut()
bin_labels = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']

results, bin_edges = pd.qcut(pruned_data['salary_in_usd'],
                             q=[0, .2, .4, .6, .8, 1],
                             labels=bin_labels,
                             retbins=True)

results_table = pd.DataFrame(zip(bin_edges, bin_labels),
                             columns=['Salary', 'Bins'])
print(results_table)


# TODO: 7) Make a barplot with binned salaries to show the company size count for each of the bins.
# Made method because: I needed to know how many times an employee hit the specified bin in each company_size.

def binned_salary_in_company_size(size):
    _data = pruned_data.loc[pruned_data['company_size'] == size]
    _data['cut'] = pd.cut(_data['salary_in_usd'], bins=5)

    return _data['cut'].value_counts().tolist()


small_company_bin_salary = binned_salary_in_company_size('S')
medium_company_bin_salary = binned_salary_in_company_size('M')
large_company_bin_salary = binned_salary_in_company_size('L')
index = bin_labels

plot_df = pd.DataFrame({'S': small_company_bin_salary,
                        'M': medium_company_bin_salary,
                        'L': large_company_bin_salary}, index=index)

ax = plot_df.plot(kind='bar')
plt.xticks(rotation=45)


# plt.show()

# TODO: PART 2
# TODO: 8) Make it into a function that can take either company_size or experience_level as arguments.
def task_8(company_size=None, experience_level=None):
    if company_size:
        _data = pruned_data.loc[pruned_data['company_size'] == company_size]
        _data['cut'] = pd.cut(_data['salary_in_usd'], bins=5)
        return _data['cut'].value_counts().tolist()
    elif experience_level:
        _data = pruned_data.loc[pruned_data['experience_level'] == experience_level]
        _data['cut'] = pd.cut(_data['salary_in_usd'], bins=5)
        return _data['cut'].value_counts().tolist()
    else:
        return None


exp_levels = ['EN', 'EX', 'MI', 'SE']

exp_en_salary = task_8(experience_level=exp_levels[0])
exp_ex_salary = task_8(experience_level=exp_levels[1])
exp_mi_salary = task_8(experience_level=exp_levels[2])
exp_se_salary = task_8(experience_level=exp_levels[3])

plot_df = pd.DataFrame({exp_levels[0]: exp_en_salary,
                        exp_levels[1]: exp_ex_salary,
                        exp_levels[2]: exp_mi_salary,
                        exp_levels[3]: exp_se_salary}, index=bin_labels)

ax = plot_df.plot(kind='bar')
plt.xticks(rotation=45)
# plt.show()

# TODO: 9) Change the experience_level column to be numeric using this dictionary:
#  experience = {'EN':10,'EX':20,'MI':30,'SE':40}
dict_experience = {'EN': 10, 'EX': 20, 'MI': 30, 'SE': 40}
pruned_data.replace({"experience_level": dict_experience}, inplace=True)
print(pruned_data)

# TODO: 10) Use seaborn pairplot to see if there is an
#  approximately linear relationship between experience_level and salary
sb.pairplot(pruned_data)
# plt.show()

# TODO: 11) scatter Plot the 2d feature
#  space of 'experience_level' and 'salary_in_usd'
scatter_ax = pruned_data.plot(kind='scatter', x='experience_level', y='salary_in_usd', color='r')
# plt.show()

# TODO: 12) Use sklearn to find the best possible linear relationship
#  between experience_level and salary_in_usd using linear regression.
x = pruned_data[['experience_level']]
y = pruned_data[['salary_in_usd']]

regressor = LinearRegression()
regressor.fit(x, y)
y_pred = regressor.predict(x)

plt.scatter(x, y, color='red')
plt.plot(x, regressor.predict(x), color='blue')
plt.title('experience level vs salary in usd')
plt.xlabel('experience level')
plt.ylabel('salary in usd')
#plt.show()

# TODO: PART 3
# TODO: ?) Given the below dictionaries find out where each of the
#  4 people find the cheapest shopping according to their needs.

shoppers = {
    'Paula': {'Is': 4, 'Juice': 2, 'Kakao': 3, 'Lagkager': 2},
    'Peter': {'Is': 2, 'Juice': 5, 'Kakao': 0, 'Lagkager': 4},
    'Pandora': {'Is': 5, 'Juice': 3, 'Kakao': 4, 'Lagkager': 5},
    'Pietro': {'Is': 1, 'Juice': 8, 'Kakao': 9, 'Lagkager': 1}
}
shop_prices = {
    'Netto': {'Is': 10.50, 'Juice': 2.25, 'Kakao': 4.50, 'Lagkager': 33.50},
    'Fakta': {'Is': 4.00, 'Juice': 4.50, 'Kakao': 6.25, 'Lagkager': 20.00}
}

shoppers_df = pd.DataFrame(shoppers).T # Turns the matrix from 4x2 to 2x4 to match shoppers_df shape
shop_prices_df = pd.DataFrame(shop_prices)

shoppers_df = shoppers_df.to_numpy() # Turns data into int64
shop_prices_df = shop_prices_df.to_numpy()

prices = shoppers_df.dot(shop_prices_df)
print(prices)
# COL: Shops
# #ROW: People
#   |N      |F    |
#   |127    |83.75| #Fakta is cheapest!
#   |166.25 |110.5|
#   osv.


