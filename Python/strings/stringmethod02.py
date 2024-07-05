#!/usr/bin/env python3


def main():
    """Run-time Code"""
    #create a small string
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ")
    print(newlist)

    #create a list of strings
    myiplist = ["192", "168", "0", "12"]
    #set single ip as result of joining the list my iplist around the "."
    singleip = ".".join(myiplist)
    # display singleip
    print(singleip)

#call your main function
main()