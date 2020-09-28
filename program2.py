# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Collatz Conjecture
# Date:        9/28/2020

from matplotlib import pyplot as pyp

list1 = [int(input("Enter a number: "))]
list2 = []
counter = 0
while list1[-1] != 1:
    if (list1[-1] % 2) == 1:
        list1.append(int(list1[-1] * 3 + 1))
    else:
        list1.append(int(list1[-1] / 2))
    list2.append(counter)
    counter += 1
list2.append(counter)
print(list1)
print(list2)

pyp.plot(list2, list1)
pyp.show()