#!/usr/bin/env python3

# parse keystone.common.wsgi and return the number of failed login attempts
loginfail = 0
# open the file for reading
keystone_file = open("/workspaces/alta3training/attemptlogin/keystone.common.wsgi","r")
#turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()
#loop over the list of lines
for line in keystone_file_lines:
    #if this "failpattern" appears in th eline...
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # this is the same as the loginfail = loginfail + 1
print(f'the number of failed logi in attempts is {loginfail}')
keystone_file.close()