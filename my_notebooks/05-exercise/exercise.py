import pandas
import pandas as pd
import matplotlib.pyplot as plt

divorced_data = pd.read_csv("../../data/divorced_danes_time.csv", sep=";")
divorced_df = pandas.DataFrame(divorced_data)


# What is the change in percent of divorced danes from 2008 til 2020?
def get_all_danes(period):
    if isinstance(period, int):
        period = str(period)

    num_of_danes = 0
    for index, row in divorced_df.iterrows():
        if row['TID'] == period + "K1" or row['TID'] == period + "K2" or row['TID'] == period + "K3" or row[
            'TID'] == period + "K4":
            if row['CIVILSTAND'] == "I alt":
                num_of_danes += row['INDHOLD']

    return num_of_danes


def divorced_in_period(period):
    # checks if param is int, to make it into a string
    if isinstance(period, int):
        period = str(period)

    divorced = 0
    for index, row in divorced_df.iterrows():
        if row['TID'] == period + "K1" or row['TID'] == period + "K2" or row['TID'] == period + "K3" or row[
            'TID'] == period + "K4":
            if row['CIVILSTAND'] == "Fraskilt":
                divorced += row['INDHOLD']

    return divorced


danes_2008 = get_all_danes(2008)
divorced_2008 = divorced_in_period(2008)

danes_2020 = get_all_danes(2020)
divorced_2020 = divorced_in_period(2020)

print(f"Number of danes in 2008: {danes_2008}")
print(f"Number of divorced danes in 2008: {divorced_2008}")
percentage_of_divorced_2008 = '{0:.3g}'.format((divorced_2008 * 100) / danes_2008)
print(f"% Divorced: {percentage_of_divorced_2008}%")

print(f"\nNumber of danes in 2020: {danes_2020}")
print(f"Number of divorced danes in 2020: {divorced_2020}")
percentage_of_divorced_2020 = '{0:.3g}'.format((divorced_2020 * 100) / danes_2020)
print(f"% Divorced: {percentage_of_divorced_2020}%")

# Todo: Visualize the difference


# Which of the 5 biggest cities has the highest percentage of ‘Never Married’ in 2020?
unmarried_data = pd.read_csv("../../data/danes_area_civil_status.csv", sep=";")
unmarried_df = pandas.DataFrame(unmarried_data)

# TODO: 1. Get the number of all unmarried in 2020
def unmarried_danes_in_period(period):
    # checks if param is int, to make it into a string
    if isinstance(period, int):
        period = str(period)

    unmarried_danes = 0
    for index, row in unmarried_df.iterrows():
        if row['TID'] == period + "K4":
            if row['OMRÅDE'] != "Hele landet":
                if row['CIVILSTAND'] == 'Ugift':
                    unmarried_danes += row['INDHOLD']

    return unmarried_danes


# TODO: 2. Get a data-collection of un-married citizens in every city
def all_unmarried_cities(period):
    # checks if param is int, to make it into a string
    if isinstance(period, int):
        period = str(period)

    unmarried_cities = []
    for index, row in unmarried_df.iterrows():
        if row['TID'] == period + "K4":
            if row['OMRÅDE'] != "Hele landet":
                if row['CIVILSTAND'] == 'Ugift':
                    unmarried_cities.append(row)

    return pandas.DataFrame(unmarried_cities)


# TODO: 3. Compare the difference and do percentage math and find the top 5
def find_percentage_of_unmarried(_unmarried_df, overall_unmarried):
    _percentage_df = []
    for index, row in _unmarried_df.iterrows():

        result = '{0:.3g}'.format((row['INDHOLD'] * 100) / overall_unmarried)
        row['INDHOLD'] = result
        _percentage_df.append(row)

    _percentage_df = pandas.DataFrame(_percentage_df)
    _percentage_df['INDHOLD'] = _percentage_df['INDHOLD'].astype(float)

    return _percentage_df


unsorted_unmarried_cities_2020 = all_unmarried_cities(2020)


def top_n_populated_city(cities_df, n=5):
    return cities_df.nlargest(n=n, columns=['INDHOLD'])


percentage_df = find_percentage_of_unmarried(unsorted_unmarried_cities_2020, unmarried_danes_in_period(2020))

top_5_unmarried = top_n_populated_city(percentage_df, 5)
print(top_5_unmarried)

