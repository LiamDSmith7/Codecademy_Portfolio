# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:45:48 2022

@author: Liam
"""

import pandas as pd
import glob
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#### GENERAL DATA PREPERATION ####
#takes all csv files in folder beginning with 'states' and ending in a digit (*).
#a for loop loops through all of the files and appends them to a list, which then
# is concatonated into one dataframe named states
files = glob.glob('states*.csv')

df_list = []
for filename in files:
    data = pd.read_csv(filename)
    df_list.append(data)
    
states = pd.concat(df_list)

print(states.columns)
print(states.dtypes)
print(states.head(5))

#### END ####

#### EDITING INCOME DATA FOR CALCULATION ####

#converting income values to numbers
#string parsing away income dollar signs in new column
states['Income_Num'] = states['Income'].str[1:]
#replacing commas
states['Income_Num'] = states['Income_Num'].replace(',', '', regex=True)
#converting to number
states['Income_Num'] = pd.to_numeric(states.Income_Num)
#average income
avg_income = states['Income_Num'].mean()


#### EDITING GENDER CENSUS DATA FOR CALCULATION AND VISUALISATION ####

#splitting the gender pop column into numeric data
#splitting the GenderPop into two strings in list 
states['GenSplit'] = states.GenderPop.str.split('_')

#Retreiving each population as string
states['MalePop'] = states.GenSplit.str.get(0)
states['FemalePop'] = states.GenSplit.str.get(1)

#Removing M and F from strings
states['MalePop'] = states['MalePop'].replace('M', '', regex=True)
states['FemalePop'] = states['FemalePop'].replace('F', '', regex=True)
#converting three empty female pop values to zeroes for conversion to int
states['FemalePop'] = states['FemalePop'].replace('', 'NaN', regex=True)

#converting malepop and total pop columns to integers for calculations
states['MalePop'] = states.MalePop.astype(int)
states['TotalPop'] = states.TotalPop.astype(int)

#converting Female Population nan values to the total population of that state minus the male population of that state, otherwise just
#female population values
states['FemalePopNoNan'] = states.apply(lambda x: x['TotalPop'] - x['MalePop'] if x['FemalePop'] == 'NaN' else x['FemalePop'], axis=1)

print(states['FemalePop'])
print(states['FemalePopNoNan'])

#Converting to integers
states['FemalePopNoNan'] = states.FemalePopNoNan.astype(int)
print(states.dtypes)

#plotting male vs female population
plt.scatter(states['MalePop'], states['FemalePopNoNan'])
plt.show()

#removing duplicates which contain the same state name from the dataframe
states = states.drop_duplicates(subset=['State'])
#plotting male vs female population once duplicates removed
plt.scatter(states['MalePop'], states['FemalePopNoNan'])
plt.show()

#### END  ####

#### VISUALISING  RACE CENSUS DATA ####
print(states.columns)
#adding race data to new dataframe to check contents
race_data = states[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']]
print(race_data)
# Removing percentage symbols from columns
states[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']] = states[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']].replace('%', '', regex=True)
#converting to integers
states[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']] = states[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']].astype(float)
print(states[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']])

#Changing figure size
figure(figsize = (10, 6), dpi = 80)
#Making bar chart of all white population percentages of every state in dataset
plt.bar(states.State, states.White)
plt.title('White population share by state')
plt.xlabel('State', rotation='vertical')
plt.xticks(rotation='vertical')
plt.ylabel("Percentage (%)")

plt.show()

#Making bar chart of all black population percentages of every state in dataset
figure(figsize = (10, 6), dpi = 80)
plt.bar(states.State, states.Black, color=(0.2, 0.4, 0.6, 0.6))
plt.title('Black population share by state')
plt.xlabel('State', rotation='vertical')
plt.xticks(rotation='vertical')
plt.ylabel("Percentage (%)")

plt.show()

#Making bar chart of all native population percentages of every state in dataset
figure(figsize = (10, 6), dpi = 80)
plt.bar(states.State, states.Native, color=('springgreen'))
plt.title('Native population share by state')
plt.xlabel('State', rotation='vertical')
plt.xticks(rotation='vertical')
plt.ylabel("Percentage (%)")

plt.show()

####  END  ####