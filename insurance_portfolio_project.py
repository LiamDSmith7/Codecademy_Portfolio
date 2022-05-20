# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:54:45 2022

@author: Liam
"""

import csv
with open('insurance.csv', newline='') as insurance:
    #reads csv into dictionary
    output = csv.DictReader(insurance, delimiter=',')
    #creating variables to analyse
    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    
    #sorting csv dictionary data into variables
    for row in output:
        for k, v in row.items():
            if k == 'age':
                age.append(v)
            elif k == 'sex':
                sex.append(v)
            elif k == 'bmi':
                bmi.append(v)
            elif k == 'children':
                children.append(v)
            elif k == 'smoker':
                smoker.append(v)
            elif k == 'region':
                region.append(v)
            elif k == 'charges':
                charges.append(v)
    
    #function for calculating average insurance cost
    charge_sum = 0 
    charge_count = 0
    for i in charges:
        charge_count += 1
        value = float(i)
        charge_sum += value
    average_cost = charge_sum // charge_count
    print("The average cost on insurance is: " + str(average_cost) + " dollars. ")
    
    #function which finds average age of patients
    def average_age():
        age_sum = 0
        age_count = 0 
        for i in age:
            age_count += 1
            current_value = int(i)
            age_sum += current_value
        age_avg = age_sum // age_count
        return print(age_avg)
    average_age()
    
    
    
    #function that finds number of males, females, and their ratio
    def sex_count():
        males = 0
        females = 0
        for i in sex:
            if i == 'male':
                males += 1
            elif i == 'female':
                females += 1
        ratio = males / females
        return print("Males: " + str(males) + " Females: " + str(females) + " Male/Female Ratio: " + str(ratio))
    
    sex_count()
    
    def print_dictionary():
        output = csv.DictReader(insurance, delimiter=',')
        print(output)
        for row in output:
            for k, v in row.items():
                print(k, v)
                
        
    print_dictionary()
    
    #counting the dataset's number of smokers and non smokers
    #calculating the average cost of the insurance costs for smokers and non smokers
    def smoking_cost():
        smokers = 0
        non_smokers = 0
        for i in smoker:
            if i == 'yes':
                smokers += 1
            elif i == 'no':
                non_smokers += 1
        ratio = smokers / non_smokers
        print("Smokers: " + str(smokers) + " Non-Smokers: " + str(non_smokers) + " Smoker/Non-Smoker Ratio: " + str(ratio))
        smoker_list = []
        non_smoker_list = []
        for k,v in zip(smoker, charges):
            current_key = k
            current_value = v
            if current_key == "yes":
                smoker_list.append(float(current_value))
            elif current_key == "no":
                non_smoker_list.append(float(current_value))
        smoker_sum = 0
        non_smoker_sum= 0 
        for i in smoker_list:
            current_value = i
            smoker_sum += current_value
        for i in non_smoker_list:
            current_value = i
            non_smoker_sum += current_value
        average_smoker_cost = smoker_sum // smokers
        average_non_smoker_cost = non_smoker_sum // non_smokers
        print("Average smoker cost: " + str(average_smoker_cost) + " Average non-smoker cost: " + str(average_non_smoker_cost))
    smoking_cost()
    