#!/usr/bin/env python3
'''
#given code
#!/usr/env python3

def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while true
        name= input(What is your name?\n>)
        num= input("Pick a number between 1 and 3: ")

        if name and num in words.keys():
            # Hi <name>! Welcome to Day 2 of Python Training!
            print("Hi " + name.capitalize + "! Have a " + words[num] + " day!")
            brake
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!
'''
"""
given solution
#!/usr/bin/env python3

def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:
        name= input('What is your name?\n>')
        num= int(input("Pick a number between 1 and 3: "))

        # input saves the returned value as a STRING
        # num = "2"

        if name and num in words.keys():
        # if the var name has a value
        # if num is one of the keys in the dict words
            # Hi <name>! Welcome to Day 2 of Python Training!
            print("Hi " + name.capitalize() + "! Have a " + words[num] + " day!")
            break
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!

main()

"""

#!/usr/env python3
#It looks as though I didnt need to throw quotes around the words dictonary keys and instead could have turned the num variable into an int
#I went with changing the dictionary values because I didnt think about how if that dictionary was massive it would have been a pain to do it that way
#I also was thinking that because things count from 0 if a user input a number 1 that it would be a 0 value that would have broken things
#this would not be the case as its checking key values not the position in a list. so the 1 key being the integer 1
#I fixed all the minor things aside from that but I did too much work :P
def main():

    words= {'1': "great",
            '2': "fabulous",
            '3': "super"}

    while True:
        name= input("What is your name?\n>")
        num= input("Pick a number between 1 and 3: ")

        if name and num in words.keys():
            # Hi <name>! Welcome to Day 2 of Python Training!
            print(f"Hi, {name.capitalize()}! Have a {words[num]} day!")
            break
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!
main()