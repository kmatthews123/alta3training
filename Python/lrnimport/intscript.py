#!/usr/bin/env python3


from subprocess import call

#this shows interfaces that are currently up
call(["ip", "link", "show", "up"])
print("this program will check your interfaces.")

interface = input("Enter an interface, like, ens3s: ")

# this issues the linux command " ip addr show dev " with the interface you asked for eariler
call(["ip", "addr", "show", "dev", interface])

# this issues the command ip route show dev command with the interface specified above
call(["ip", "route", "show", "dev", interface])
