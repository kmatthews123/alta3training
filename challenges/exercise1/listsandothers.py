#!/usr/bin/env python3

#import random library utils
import random

#exercise for lists, input, print, and variables
wordbank= ["indentation", "spaces"] 

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

#append number 4 to wordbank
wordbank.append(4)

#ask user for input between 0 and 20 and turn it to a number
#num = int(input("please enter a number between 0 and 20: "))

student_name = random.choice(tlgstudents)

print(student_name , "always wanted to use", wordbank[2], wordbank[1], "to indent" )