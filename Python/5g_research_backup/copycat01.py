#!/usr/bin/env python3

#import the tools used for this script
import shutil
import os


def main():
    # move into working directory
    os.chdir("/home/keithm/projects/Python-TLG/alta3training/")

    #copy file a to file b
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy the entire directery from directery a to directery b
    os.system("rm -rf /home/keithm/projects/Python-TLG/alta3training/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()