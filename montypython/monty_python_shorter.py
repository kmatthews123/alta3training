#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

## this script diverges from the other montypython program by the following
## 1. instead of having the answer inside the while loop we declare it outside
## 2. for the while loop we are also checking if round is less than three and ..
## we are also checking if the answer is not equeal to brian
## this streamlines the program because it prevents us having to break out of the while loop
## this is better practice
##
