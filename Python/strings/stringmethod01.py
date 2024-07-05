#!/usr/bin/env python3

#create a small string
lilstring = "Alta3 research offers classes on python coding"
newlist = lilstring.split(" ") #this returns a list
print(newlist)

#create a list of strings
myiplist = ["192", "168", "0", "12"]
#set single IP as the result of joining myiplist around the "."
singleip = ".".join(myiplist)
# display single ip
print(singleip)