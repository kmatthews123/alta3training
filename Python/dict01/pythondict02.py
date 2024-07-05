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

    ## request a 'fake' key pair this will fail using this method
    ##print(switch[lynx])         #this will cause the program to fail

    ## request a fake key with the .get() method
    print("first test - .get()")
    print(switch.get("lynx")) #alternative to switch ["lynx"]
    #print(switch.get("lynx", None))    #this is what is actualy eing run...
                                        #by default dict.get()returns "None"

    # if you want to customize what is returned when the key is not found
    print("second test - .get()")
    print(switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!"))

    print("Third test - .get()")
    print(switch.get("version"))    #altertative to switch['version']
                                    #this key exists so wit will return a value of "1.2"



# call our main function
if __name__ == "__main__":
    main()
