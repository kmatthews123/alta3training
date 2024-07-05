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


    #this returns all the keys of the dictionary
    print("forth test - .keys()")
    print( switch.keys())       #dict.keys() returnes all the keys in a "list like" structure

    # this returns all the values in the dictionary
    print("fith test - .values()")
    print(switch.values())      #dict.values() returns all the values in a "list like" structure

    #remove a value from our dicctionary using del
    del switch["vendor"]        #this removes the key/value pair and returns nothing
    # del switch ["pizza"]      #this will fail because pizza isnt a key that exists
                                #this will return an error

    # remove a value from our dictionary using a method
    print("seventh test - .pop()")
    print(switch.pop("version"))        #removes this key and als returns the value "1.2"
    print(switch.keys())                #notice the value of version is gone
    print(switch.values())              #notice the valye 1.2


    # add a value to the dictionary
    print("eighth test - ADD a new value")
    switch["adminlogin"] = "karl08"
    print(switch.keys())
    print(switch.values())

    #add another value to the dictionary 
    print("ninth test - add a new value")
    switch["password"] = "qwerty"
    print(switch.keys())
    print(switch.values())

    # select a value from the results
    # firs twe must convert ethis "list like" strurue into an actual list
    # using the list()
    print(list(switch.values())[2]) # this selects the second position (3rd item) from the list

    


# call our main function
if __name__ == "__main__":
    main()
