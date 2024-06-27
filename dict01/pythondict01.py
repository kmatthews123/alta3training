#!/usr/bin/env python3

"""Understanding dictionaries
   {key: value, key:value, ...} """


def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display the entire dictionary
    print(switch)

    #proove tthat swith is indeed a dictioanry
    print(type(switch))

    ## display parts of the dicitionary
    print(switch["hostname"])   #displays the hostname sw1
    print(switch["ip"])         #displays the ip address 10.0.1.1

    ## request a 'fake' key pair
    ## print(switch[lynx])          #this will cause the program to fail
                                    #commented out for my sanity

#call the main function

if __name__ == "__main__":
    main()