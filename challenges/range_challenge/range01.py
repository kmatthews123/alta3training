#!/usr/bin/env python3


def main():
    while True:
        bobwall = int(input("How many bottles of beer are on the wall?: "))
        if bobwall <= 99:
            for i in range(bobwall):
                print(f'{bobwall} bottles of beer on the wall!')
                print(f'{bobwall} bottles of beer on the wall! {bobwall} bottles of beer! You take one down, pass it around!')
                bobwall -= 1
        if bobwall > 99:
            print(f'please pick a more reasonable number of bottles')
        if bobwall <= -1:
            print("Thats not a real number, goodbye!")
            break
main()    