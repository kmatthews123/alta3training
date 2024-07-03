#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import crayons

import json


#function to reboot all devices found on the network
def devicereboot(ipaddrs):

    for ipaddress in ipaddrs:
        print(f'Connecting to.. {ipaddress} ..... REBOOTING NOW')
    #print(ipaddrs)



# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile) # decode the JSON from the file to pythonic data


    print(f"Welcome to the {crayons.blue('Network')} device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    ## generate a list of ip address to send reboot commands to
    #create empty list
    ipaddrs= []
    #itterate though the devicecmd.keys to pull out the ip addresses
    for ip in devicecmd.keys():
        ipaddrs.extend({ip})
    #once the ipaddrs list is filled out, ship that off to the devicereboot function
    devicereboot(ipaddrs)

# call our main function
main()
 