# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:16:56 2022

@author: Liam
"""

import pandas as pd
jeopardy = pd.read_csv('jeopardy.csv')
pd.set_option('display.max_colwidth', -1)
jeopardy.rename(columns={'Show Number': 'show_number', ' Air Date': 'air_date', ' Round': 'round', ' Category': 'category', 
                         ' Value' : 'value', ' Question': 'question', ' Answer': 'answer'}, inplace=True)
print(jeopardy.head())

# function which searches the dataframe's question column for a keyword
def search(word):
    #appends entire rows which contain keyword
    search_result = jeopardy[jeopardy.question.str.contains(word) == True]
    #just prints questions column 
    print(search_result.question)

# initiates search - enter keyword here
# unhash this: search('King')

def filter_data(data, words):
  # Lowercases all words in the list of words as well as the questions. Returns true is all of the words in the list appear in the question.
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # Applies the labmda function to the Question column and returns the rows where the function returned True
  return jeopardy.loc[jeopardy["question"].apply(filter)]

# Testing the filter function
filtered = filter_data(jeopardy, ["King", "England"])
# unhash to test: print(filtered.question)

# creating float column of all cash values awarded for the correct answers. It uses [1:] to remove all dollar signs, it replaces all commas with nothing, and if the value is 'none' it uses a zero. 
jeopardy["floats"] = jeopardy["value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

#function which searches for a string, and returns the average value for getting a question containing that string correct
def avg_value(word):
    search_result = jeopardy[jeopardy.question.str.contains(word) == True]
    return print("$" + str(int(search_result.floats.mean())))

#add keyword here and average cash prize of questions containing keyword is returned
#unhash to test: avg_value(" ")

#function which returns number of unique answers
def unique_answers():
    unique = jeopardy['answer'].nunique()
    return print(unique)

unique_answers()

#function which returns number of answers in keyword, call with 'filtered' variable and edit keywords in there to change search
def keyword_counts(data):
    return data["answer"].value_counts()

print(keyword_counts(filtered))

#counting the number of instances of questions mentioning a computer pre and post year 2000
pre_2000 = jeopardy[(jeopardy.question.str.contains("computer") == True) &
                        (jeopardy.air_date < '2000-01-01')]
post_2000 = jeopardy[(jeopardy['question'].str.contains("computer") == True) &
                        (jeopardy.air_date > '2000-01-01')]
print('Pre-2000 mentions of computer: ' + str(len(pre_2000)) + \
                 ' Post-2000 mentions of computer: ' + str(len(post_2000)))
