# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  MOSSSSSSSSSSSSSSSSSSSSSSSSSSSS
# Date:        9/28/2020

# Importing mean()
from statistics import mean

# Defining list
moss_list = [15.80, 19.60, 21.85, 33.61, 49.73, 51.27, 56.26, 63.06, 76.56, 76.57, 85.78, 90.74, 92.60, 99.71,
100.51, 101.12, 101.25, 102.19, 104.85, 110.59, 125.92, 131.25, 136.04, 141.15, 148.54, 150.02]

# Appending and inserting values to list
moss_list.append(162.76)
moss_list.insert(8,71.01)

# Creating lists for each week
week1 = moss_list[0:6]
week2 = moss_list[7:13]
week3 = moss_list[14:20]
week4 = moss_list[21:]

# Final print

print("There were {} days of data collected".format(len(moss_list)))
print("Average mass of week 1: {}g".format(round(mean(week1),2)))
print("Average mass of week 2: {}g".format(round(mean(week2),2)))
print("Average mass of week 3: {}g".format(round(mean(week3),2)))
print("Average mass of week 4: {}g".format(round(mean(week4),2)))