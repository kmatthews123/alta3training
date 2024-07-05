# challenge to work with dictionary
# I modified this script to catch spelling errors, thanks tyler for pointing out that is a thing i should do
# I need to figure out how to bring the user back to the current thing if they mess up
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

def main():
  while True:
    #  Save a user's input to the variable char_name from the following question:
    #  Which character do you want to know about? Starlord, Mystique, Hulk
    char_name = input("which characther do you want to know about? (Starlord, Mystique, Hulk)").capitalize()
    if char_name in marvelchars.keys():

        # save the users input to the variable char_stat from the following question
        # What statistic do you want to know about? (real name, powers, archenemy)
        char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")
        if char_stat in marvelchars[char_name].keys():
          print(char_name.capitalize(),"'s ", char_stat.capitalize(), " is ", marvelchars[char_name][char_stat].capitalize() ,sep="")
        else:
          print("bad spelling, try again")
    else:
      print("bad spelling, try again")
          
# call our main function
if __name__ == "__main__":
    main()