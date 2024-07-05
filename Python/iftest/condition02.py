#!/usr/bin/env python

#ask the user to enter a hostname
hostname =  input("what should the value be for the hostname?")

#test logicwith the 'if' statement 
# check if user input mtg in lower case, this is fragile and will break if looked at wrong
if hostname == "mtg":
    print("the hostname was found to be mtg")