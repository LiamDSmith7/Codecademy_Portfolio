# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 13:11:20 2022

@author: Liam
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')

print(df.head(5))

#Renaming life expectancy columns as its far too long for calling in script
df.rename(columns={
        'Life expectancy at birth (years)': 'LifeExpectancy'
        },inplace=True)
print(df.columns)

#table = pd.crosstab(df.LifeExpectancy, df.GDP)
#print(table)

#creating individual country dataframes
ChileData = df[df.Country == 'Chile']
ChinaData = df[df.Country == 'China']
GermanyData = df[df.Country == 'Germany']
MexicoData = df[df.Country == 'Mexico']
USData = df[df.Country == 'United States of America']
ZimbabweData = df[df.Country == 'Zimbabwe']

#setting the seaborn style
sns.set_style("darkgrid")

#This combined line plot shows a trend across the dataset, of rising life expectancy over time, with Zimbabwe being an anomolous example, 
#it will be useful to see if this is related to its GDP, next I will plot every country's GDP and life expectancy relationship
plt.plot(USData.Year, USData.LifeExpectancy)
plt.plot(ZimbabweData.Year, ZimbabweData.LifeExpectancy)
plt.plot(ChileData.Year, ChileData.LifeExpectancy)
plt.plot(ChinaData.Year, ChinaData.LifeExpectancy)
plt.plot(GermanyData.Year, GermanyData.LifeExpectancy)
plt.plot(MexicoData.Year, MexicoData.LifeExpectancy)
plt.legend(['USA', 'Zimbabwe', 'Chile', 'China', 'Germany', 'Mexico'], loc='best')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.show()
plt.clf()


#From these subplots, we can see that China is anomolous in regards to its relation of GDP and life expectancy compared to the other 
#examples we have in this dataset. It appears the other have linear relationship, china's is logarithmic. It may be useful to examine
#this more closely. Its also interesting to note that despite Zimbabwe's anomolous time series, the relationship between GDP and 
#life expectancy is still the same as the others in the dataset

sns.set(rc = {'figure.figsize':(15,12)})
#define plotting region (2 rows, 3 columns)
fig, axes = plt.subplots(2, 3)
#creates scatterplots in each subplot
sns.scatterplot(data=ChileData, x='GDP', y='LifeExpectancy', ax=axes[0,0]).set(title='Chile')
sns.scatterplot(data=ChinaData, x='GDP', y='LifeExpectancy', ax=axes[0,1]).set(title='China')
sns.scatterplot(data=GermanyData, x='GDP', y='LifeExpectancy', ax=axes[0,2]).set(title='Germany')
sns.scatterplot(data=MexicoData, x='GDP', y='LifeExpectancy', ax=axes[1,0]).set(title='Mexico')
sns.scatterplot(data=USData, x='GDP', y='LifeExpectancy', ax=axes[1,1]).set(title='USA')
sns.scatterplot(data=ZimbabweData, x='GDP', y='LifeExpectancy', ax=axes[1,2]).set(title='Zimbabwe')
plt.show()
plt.clf()

#We can conclude from this line plot that in China, life expectancy rose first, while GDP is barely affected, and then GDP rose after, 
#implying some other factor improved life expectancy first (e.g. agricultural output increasing caloric availability, thus reducing disease), 
#and GDP followed this, possibly as the population became more productive
plt.subplot(1, 2, 1)
plt.plot(ChinaData.Year, ChinaData.GDP, marker='o')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.title('China Life Expectancy over time')

plt.subplot(1, 2, 2)
plt.plot(ChinaData.Year, ChinaData.LifeExpectancy, marker='*')
plt.ylabel('Life Expectancy')
plt.title('China GDP over time')
plt.xlabel('Year')
plt.show()
plt.clf()

#while zimbabwe lies very var outside the interquartile range of the datgaset, it is approaching it more closely every year
sns.boxplot(data=df, x="Year", y="LifeExpectancy")
plt.show()