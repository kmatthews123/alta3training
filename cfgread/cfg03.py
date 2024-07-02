#!/usr/bin/env python3
## create file object in "r"ead mode
user_file = input("please input the name of a file you wish to see: ")
newlines = 0
with open(user_file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    for i in configlist:
            newlines += 1

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(newlines)


## you havent figured out how to add the count of new lines yet. 
##brain fried