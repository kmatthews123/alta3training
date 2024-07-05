#!/usr/bin/env python3

ipcheck = input("Apply an IP address: ")    # line prompts user for an ip address

# first check if user input the ip address of the imaginary gateway
if ipcheck == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipcheck + " This is not recomended.")
#if the user did not put in the gateway ip, check if they input anything
elif ipcheck:
    print("looks like the IP address was set: "+ ipcheck) 
#if they didnt put in anything at all, tell the user they didnt do anything
else:
    print("you did not provide any input.")