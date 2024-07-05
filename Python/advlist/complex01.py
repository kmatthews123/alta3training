#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display the first item in the list 1
    print(list1[1])

    #create a second list with juniper as the one item
    list2 = ["juniper"]

    #extend the first list with the contents of the second list (combine the two)
    list1.extend(list2)
    
    #print combined lists
    print(list1)

    #create list3 
    list3 =  ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # use the append operation to append list 1 by list 3
    list1.append(list3)

    #disp;ay the complex list 1
    print(list1)

    #print the list of ip addresses (this works because the 4 value of the list is a list itself so it will print all values inside that 4 value)
    print(list1[4])

main()
