#!/usr/bin/python3
#this is the even more sane way to open and read this big file
#this way of doing this avoids having to worry about closing the file when your done
# parse keystone.common.wsgi and return number of succsessful POSTs for the user
# parse keystone.common.wsgi and return number of failed login attempts
postsuccess = 0 # counter for fails
loginfail = 0 # counter for fails

# open the file for reading
with open("/workspaces/alta3training/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
         if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print("IP of authorization failure: ", line.split(" ")[-1])

         elif "POST" in line:
            postsuccess+= 1 # this is the same as postsuccess = postsuccess +1

print("The number of failed log in attempts is", loginfail)
print("The number of successful POSTS is", postsuccess)
