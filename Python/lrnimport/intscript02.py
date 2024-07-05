#!/usr/bin/env python3
#this time were importing the whole subprocess module
#this will mean we need to use the subprocess.call method to use the call method like we did before
#this is so we can use other methods of the subprocess module
import subprocess  ## <-------- changed
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed
