# challenge to work with dictionarys


def main():
    #  Save a user's input to the variable char_name from the following question:
    #  Which character do you want to know about? Starlord, Mystique, Hulk
    char_name = input("which characther do you want to know about? (Starlord, Mystique, Hulk)").capitalize()
    
    # save the users input to the variable char_stat from the following question
    # What statistic do you want to know about? (real name, powers, archenemy)
    char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")

    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

    print(char_name.capitalize(),"'s ", char_stat.capitalize(), " is ", marvelchars[char_name][char_stat].capitalize() ,sep="")
# call our main function
if __name__ == "__main__":
    main()