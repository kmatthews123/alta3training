#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library
the prompt for this challenge is not to try and ask a user for information
instead the goal is to turn the very long print statements into their own function that can be called via the i in the for loop
"""

import netifaces

def find_mac(interface_name):
    """passed interface name (string), returns the MAC of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_LINK])[0]['addr']    # the MAC address

def find_ip(interface_name):
    """passed interface name (string), returns the IP of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_INET])[0]['addr']     # the IP address

def main():
     """runtime"""

     print(netifaces.interfaces())

     for i in netifaces.interfaces():
         print('\n****** details of interface - ' + i + ' ******')
         try:
        
            print('MAC:', find_mac(i)) # display MAC address information for adapter, in this case i is the interface name

            print('IP:', find_ip(i))   # display IP address information for adapter, in this case the i is the interface name
        
         except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

if __name__ == "__main__":
    main()
 