#!/usr/bin/env python3
#this is a script to move a file
import shutil
import os


def main():
    #set working directery (really wish this wasnt static)
    os.chdir("/home/keithm/projects/Python-TLG/alta3training")

    #move command example
    shutil.move('raynor.obj','ceph_storage/')

    #get new name for kerrigan.obj
    xname = input("what is the new name for kerrigan.obj? ")

    #rename the current kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


main()  #calls the main function