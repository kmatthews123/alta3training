#!/usr/bin/env python3

"""
it seems like it would be a good idea to select the fruit as there is less of it to filter out
in this case thats true but it is more common to have lots of diffrent kinds of fruit and veggies on diffrent farms
there are only so many farm animals so in the end to make the tool more resiliant, it makes more sense to filter out things that are animals,
as opposed to things that are not fruit
#original farms list
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


#fruitveg = ["carrots","celery"]         
"""
farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
#count = 0
def main():
    while True:
        count = 0
        #NE_animals = farms[0]["agriculture"]
        #have user select farm
        #setup a for loop to print the name of the farm and add a number
        for farm in farms:
            count += 1
            print(f'{count}. {farm["name"]}')
        count += 1
        print(f'{count}. to quit')
        user_input = int(input("please enter the number of the farm you wish to know about: "))
        if user_input == count:
            print("goodbye!")
            break
        print(f'You chose: {farms[user_input - 1]["name"]}')
        for i in farms[user_input - 1]["agriculture"]:
            if i in animals:
                print(i)
            else:
                continue

main()