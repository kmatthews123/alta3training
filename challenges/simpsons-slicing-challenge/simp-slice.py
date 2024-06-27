#!/usr/bin/env python3
#challenge to slice and dice the simpsons eyes buring scene
#The goal is to 1. pull from the challenge list the strings 'eyes'googles' and nothing
def main():
    
    #provided list
    challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]
    #provided list with dictionary in it
    trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    #provided dictionary with a nested dictionary I think
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    # prints "my eyes! The goggles do nothing!" but with one value from each of the lists. didnt read the task for this one.
    #print("my ", challenge[2][1], "! The ", trial[2]["eyes"], " do ", nightmare[0]["d"],"!", sep="")

    #print "my eyes! The googles do nothing!" from the challenge list
    print("my ", challenge[2][1], "! The ", challenge[2][0], " do ", challenge[3], "!", sep="")

    #print "my eyes! The googles do nothing!" from the trial list
    print("my ", trial[2]["goggles"], "! The ", trial[2]["eyes"], " do ", trial[3], "!", sep="")

    #print from the nightmare list
    print("my ", nightmare[0]["user"]["name"]["first"], "! The ", nightmare[0]["kumquat"], " do ", nightmare[0]["d"], "!" ,sep="")


# call our main function
if __name__ == "__main__":
    main()