#!/usr/bin/env python3

#this function reads in the dracula.txt and opens a file to dump lines that include the word vampire 
def main():
    with open("/workspaces/alta3training/challenges/dracula/dracula.txt", "r") as vamp:
        with open("/workspaces/alta3training/challenges/dracula/vampytimes.txt", "w") as bats:
            vampcount = 0
            for line in vamp:
                #originaly I treid making the "vampire" word a varible, and applying the .lower() method against it to check for upper case Vampire in the line
                #this did not work because "vampire" is already lower case, what I needed to do was to use the .lower method in the line thats being read at the time
                #Doing that removes the upper cases in each line as its read in and compares it against the "vampire" keyword
                if "vampire" in line.lower():
                    print(line)
                    vampcount += 1
                    bats.write(line)
            print("the word 'vampire' appears:", vampcount, "times")

main()