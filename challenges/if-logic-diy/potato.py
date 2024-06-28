#!/usr/bin/env python3

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

#this should be a thing to break out of the while loop but it only kind of does that
def goagain():
    i = str.capitalize(input("would you like to try again? yes or no: "))
    if i == "Yes":
        main()
    elif i == "No":
        print("thanks for playing!")
        exit()

#the user is a potato
def your_a_potato():
    print("You are a potato!")
    goagain()

#the user is acting like a goober and is therefore a potato
def acting_goober():
    print("You're acting like a goober tuber")
    your_a_potato()


#are you sure line of questioning
def areyousure():
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
        yousureq2 = str.capitalize(input("Please enter either 1 or 2: "))
        if yousureq2 == "1":
            acting_goober()
        #handle the root vegtable question
        elif yousureq2 == "2":
            rootq = str.capitalize(input("You're so quirky, one last question, what is the best root vegtable? "))
            if rootq == "Potato":
                print("That's exactly what a potato would say!")
                your_a_potato()
            elif rootq in rootveggies[1:22]:
                print("Ok thats weird, I guess you're not a potato though")
                goagain()
            elif rootq == "":
                noinput()
            elif rootq not in rootveggies[1:22]:
                print("That's not a root veggie, you dont know how to read, or you dont know how to type")
                your_a_potato()
   
    #space potato
    elif yousureq1 == "3":
        print("I think you're a space potato")
        goagain()
    #no input function call
    elif yousureq1 == "":
        noinput()
    else:
        print("Do you not know how to read? Potatos struggle with that sometimes.")
        your_a_potato()



#potatos cant spell, this is this things version of error correction
def potatoscantspell():
        print("Potatos cant spell! You must be a potato!")
        your_a_potato()

#potatos cannot talk, this function is to see if the user is a silent potato
def noinput():
    you_silent_1 = input("Potatos cannot talk or type, I think your a potato, say something if your not a potato. ")
    if you_silent_1 != "":
        areyousure()
    else:
        you_silent_2 = input("you are almost certainly a potato, last chance: ")
        if you_silent_2 != "":
            areyousure()
        else:
            your_a_potato()

#main function, initiates all others
def main():
    #begin by asking user if they are a potato
    user_potato = str.capitalize(input("Are you a potato? yes or no: "))
    #print(user_potato)

    #if user says yes
    if user_potato == "Yes":
        your_a_potato()
    
    #if user says no
    elif user_potato == "No":
        sure_1 = str.capitalize(input("Are you sure? yes or no: "))
        #is the user a potato?
        if sure_1 == "Yes":
            sure_2 = str.capitalize(input("You do look a bit like a potato, are you really sure you aren't a potato? yes or no: "))
            if sure_2 == "Yes":
                acting_goober()
            elif sure_2 == "No":
                areyousure()
            elif sure_2 == "":
                noinput()
            else:
                potatoscantspell()
        elif sure_1 == "No":
            areyousure()
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
go_again = True
while go_again == True:
    main()