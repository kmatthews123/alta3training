#!/usr/bin/env python

#ask the user to enter a hostname
hostname =  input("what should the value be for the hostname?")

#test logicwith the 'if' statement 
#using str.lower() to avoid issues of the user not inputing all lower case letters by forcing the value to be lower case
if hostname.lower() == "mtg":
    print("the hostname was found to be mtg")