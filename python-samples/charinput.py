#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

import datetime

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

td = datetime.date.today()
currentYear = td.year
print('Current year: ', currentYear)
hundredAgeYear = int(currentYear) + (100 - age)

print('Hi ',name,' ! you will be hubdered in ', str(hundredAgeYear))