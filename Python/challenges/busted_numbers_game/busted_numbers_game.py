#!/usr/bin/env python3
"""
#below is the original broken version of the code

#!/usr/bin/env python3
Number guessing game! User has 5 chances to guess a number between 1 and 100!

def main():
    num= random.randint(1,100)

    rounds= 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds + 1

        if guess < num:
            print("Too low!")
            rounds + 1

        else:
            print("Correct!")
"""
"""
#this is the recomended solution
#!/usr/bin/env python3

Number guessing game! User has 5 chances to guess a number between 1 and 100!
import random

def main():
    num= random.randint(1,100)

    guess= ""
    rounds= 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next fourlines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds += 1

        elif guess < num:
            print("Too low!")
            rounds += 1

        else:
            print("Correct!")

main()
"""

#fixed version of code that I did
#things I did diffrent
#basicly the only thing is the rounds = rounds + 1
#these lines could also be rounds += 1, this is more consise but for me less readable
#everything else appears to be the same
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():
    num= random.randint(1,100)

    rounds= 0
    guess= 0

    while rounds < 5 and int(guess) != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds = rounds + 1

        if guess < num:
            print("Too low!")
            rounds = rounds + 1

        else:
            print("Correct!")
main()