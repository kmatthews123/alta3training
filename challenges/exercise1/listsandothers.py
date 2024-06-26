#!/usr/bin/env python3

#import random library utils
import random

#exercise for lists, input, print, and variables
wordbank= ["indentation", "spaces"] 

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping', 'Keith']

#append number 4 to wordbank
wordbank.append(4)

#ask user for input between 0 and number of students and turn it to a number
num = int(input("please enter a number between 1 and "+ str(len(tlgstudents)) + ": ")) - 1
student_name = tlgstudents[num]

#uncomment below if you want to chose a random student
#student_name = random.choice(tlgstudents)

print(student_name , "always wanted to use", wordbank[2], wordbank[1], "to indent" )