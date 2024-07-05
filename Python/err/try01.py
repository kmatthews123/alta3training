#!/usr/bin/env python3

#start an infinite loop
while True:
    try:
        print("enter a filename: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("no Problems with that file name.")
        break
    except:
        print("Error with that file name! Try agian...")