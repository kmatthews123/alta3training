#!/usr/bin/env python3
#
#for refactor I fixed the folowing,
#alphabetised fucntions except for main()
#removed the "go again" function
#renamed "areyousure" function to are_you_sure
#replaced the str.capitalise(input("something")) with input(something)
#
#list of root veggies
#sourced list of veggies from https://americangardener.net/types-of-root-vegetables/
rootveggies = ["Potato", 
    "Ginger",
    "Jerusalem artichoke",
    "Garlic",
    "Radish",
    "Rutabaga",
    "Celery root",
    "Carrot",
    "Daikon",
    "Onion",
    "Parsnip",
    "Jicama",
    "Beet",
    "Kohlrabi",
    "Sweet potato",
    "Burdock root",
    "Cassava",
    "Shallot",
    "Galangal",
    "Horseradish",
    "Turnip",
    "Fennel",
    "Turmeric",
    "Yam"]

#begin definitions of functions

#the user is acting like a goober and is therefore a potato
def acting_goober():
    print("You're acting like a goober tuber")
    your_a_potato()

def are_you_sure():
    print("Since you're not sure if your a potato, why don't we do a personality quiz? How do you feel about dirt?")
    print("1. Love it!")
    print("2. Hate it.")
    print("3. What is dirt?")
    yousureq1 = (input("Please enter 1, 2, or 3: "))
    #decision tree for are you sure 1, 2 or 3
    if yousureq1 == "1":
        print("That's probably what a potato would say!")
        your_a_potato()
    #user hates it
    elif yousureq1 == "2":
        print("What do you think of the term 'tuber goober'?")
        print("1. That's stupid")
        print("2. That very funny, it also describes me perfectly")
        #take input on tuber goober
        yousureq2 = input("Please enter either 1 or 2: ").capitalize
        if yousureq2 == "1":
            acting_goober()
        #handle the root vegtable question
        elif yousureq2 == "2":
            rootq = input("You're so quirky, one last question, what is the best root vegtable? ").capitalize
            if rootq == "Potato":
                print("That's exactly what a potato would say!")
                your_a_potato()
            elif rootq in rootveggies[1:22]:
                print("Ok thats weird, I guess you're not a potato though")
            elif rootq == "":
                noinput()
            elif rootq not in rootveggies[1:22]:
                print("That's not a root veggie, you dont know how to read, or you dont know how to type")
                your_a_potato()
 
    #space potato
    elif yousureq1 == "3":
        print("I think you're a space potato")
    #no input function call
    elif yousureq1 == "":
        noinput()
    else:
        print("Do you not know how to read? Potatos struggle with that sometimes.")
        your_a_potato()

#potatos cannot talk, this function is to see if the user is a silent potato
def noinput():
    you_silent_1 = input("Potatos cannot talk or type, I think your a potato, say something if your not a potato. ")
    if you_silent_1 != "":
        are_you_sure()
    else:
        you_silent_2 = input("you are almost certainly a potato, last chance: ")
        if you_silent_2 != "":
            are_you_sure()
        else:
            your_a_potato()

#potatos cant spell, this is this things version of error correction
def potatoscantspell():
        print("Potatos cant spell! You must be a potato!")
        your_a_potato()

#the user is a potato
def your_a_potato():
    print("You are a potato!")

#main function, initiates all others
def main():
    while True:
        #begin by asking user if they are a potato
        #
        user_potato = input("Are you a potato? yes or no, type q to exit: ").capitalize()
        #user_potato = input("Are you a potato? yes or no: ").capitalise()
                        #this returns a string              .this is a method for the string object
        #print(user_potato)
        if user_potato == "Q":
            break
        #if user says yes
        elif user_potato == "Yes":
            your_a_potato()
        
        #if user says no
        elif user_potato == "No":
            sure_1 = input("Are you sure? yes or no: ").capitalize
            #is the user a potato?
            if sure_1 == "Yes":
                sure_2 = input("You do look a bit like a potato, are you really sure you aren't a potato? yes or no: ").capitalize
                if sure_2 == "Yes":
                    acting_goober()
                elif sure_2 == "No":
                    are_you_sure()
                elif sure_2 == "":
                    noinput()
                else:
                    potatoscantspell()
            
            elif sure_1 == "No":
                are_you_sure()

            #instead use if not sure_1:
            # do it this way because it checks if a string is true, thats 
            elif sure_1 == "":
                noinput()
            else:
                potatoscantspell()

        #if user enters no input
        elif user_potato == "":
            noinput()

        #if user enters something that is not given as an answer
        else: 
            potatoscantspell()

#got rid of extraneous while logic
main()