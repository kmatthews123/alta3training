#!/usr/bin/env python3

#import random library utils
import random

#exercise for lists, input, print, and variables
wordbank= ["indentation", "spaces"] 

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping', 'Keith']

#append number 4 to wordbank
wordbank.append(4)

#primary function
print("primary function")
#get number from user for list index
num = int(input("please enter a number between 0 and 20: "))
student_name = tlgstudents[num]
print(student_name , "always wanted to use", wordbank[2], wordbank[1], "to indent" )


#bonus 1 is a function that picks a random student
print("bonus1")
#ask user for input between 0 and number of students and turn it to a number
student_namebonus1 = random.choice(tlgstudents)
print(student_namebonus1 , "always wanted to use", wordbank[2], wordbank[1], "to indent" )


#bonus 2 is a function that lets a user pick a student by an entered number
print("bonus2")
numbonus2 = int(input("please enter a number between 1 and "+ str(len(tlgstudents)) + ": ")) - 1
student_namebonus2 = tlgstudents[numbonus2]
print(student_namebonus2 , "always wanted to use", wordbank[2], wordbank[1], "to indent" )