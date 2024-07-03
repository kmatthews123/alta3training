#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP
   
the recommended way of completing this challenge script is to do the following
#!/usr/bin/python3 
#Alta3 Research | rzfeeser@alta3.com
#Use Paramiko to create an SFTP session and transport files into a directory determined by the user

# python3 -m pip install paramiko
import paramiko # allows Python to ssh


# standard library
import os # low level operating system commands
import getpass # we need this to accept passwords


def transfer_to_this_remote_dir():
    #ask user for full path of directory to be created
    while True:
        what_dir = input("What directory on the remote host would you like to transfer files to (default: /tmp/)? ")
        if what_dir == "":   # if they just hit "enter" we can assume they want the default
            what_dir = "/tmp/"
            break  # escape the infinite loop
        elif what_dir[0] == "/" and what_dir[-1] == "/":
            break  # escape the infinite loop
        print("You must enter a full path for the remote host. Full paths must begin and end with '/'.")
    return what_dir  # this should be a full path


def movethemfiles(sftp):
    #a simple function that moves files across an SFTP paramiko channel
    what_dir = transfer_to_this_remote_dir()  # nested function call to determine the full path to transfer to

    # iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, what_dir+x) # sftp.put("from_path_local", "to_path_remote") - move file to target location
    return

def main():
    #runtime
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender

    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass

    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    # call function that moves files
    movethemfiles(sftp)  # we must pass the sftp connection channel to the function

    ## close the connection
    sftp.close() # close the sftp connection
    t.close()    # close the transport channel

if __name__ == "__main__":
    main()

The ways in which my solution differ are that I dont create an independant function for main and the move the files command
this would have been good practice but I wanted to figure out if I could do everything this way.
If I was to make a function to actualy move these files around with their own function...
we would nest the portion of main that is the for loop into its own function
we would pass the varible sftp into the function for the sftp connection details
we would also put the what_dir = transfer_to_remote_dir() in the move files function
this would have the main function call the move files function call which would call the transfer_to_remote_dir function
   """

# import paramiko so we can talk SSH
# python3 -m pip install paramiko
import paramiko

# standard library
import os

#import get pass
import getpass

#this function check what a directery a user wants to  send files to
#it check for user not entering anything
#it checks for full path
#if not full path it has the user try again
def transfer_to_remote_dir():
  #setup infinite loop
  while True:
    #get remote directery the user wants
    remote_dir = input("please enter the full path of the remote directery you wish to send files to: ")
    #if user just mashed enter
    if remote_dir == "":
      #assume user wants default tmp and lets them know thats whats gonna happen
      print("sending files to /tmp/")
      remote_dir = "/tmp/"
      return remote_dir
    #check the user put in a path with a / on both ends
    elif remote_dir.startswith("/") and remote_dir.endswith("/"):
        return remote_dir
    # if user fails at that then have them loop back to the top
    else:
        print("that was not a full path")
   
   

def main():
    """runtime"""

    # "Where to connect to" - An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates,
    # and then creates stream tunnels, called channels, across the session. 
    t = paramiko.Transport("10.10.2.3", 22) # IP and port

    # "How to connect (see other labs on using id_rsa private/public keypairs)" - Negotiate an SSH2 session, and optionally verify the server’s host key
    # and authenticate using a password or private key. This is a shortcut for start_client, get_remote_server_key, and Transport.auth_password
    # or Transport.auth_publickey. Use those methods if you want more control.
    #
    # You can use this method immediately after creating a Transport to negotiate encryption with a server. If it fails, an exception will be thrown.
    # On success, the method will return cleanly, and an encrypted session exists. 
    t.connect(username="bender", password=getpass.getpass(f'please enter password for user bender: ')) #this has the user enter the password

    ## "Make an sftp connection object" - Setting the window and packet sizes might affect the transfer speed. The default settings in the
    # Transport class are the same as in OpenSSH and should work adequately for both files transfers and interactive sessions.
    sftp = paramiko.SFTPClient.from_transport(t)

    whatdir = transfer_to_remote_dir()

    ## iterate across the files within directory
    for x in os.listdir("/workspaces/alta3training/paramikotesting/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/workspaces/alta3training/paramikotesting/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/workspaces/alta3training/paramikotesting/filestocopy/"+x, whatdir+x) # sftp.put("from_path_local", "to_path_remote") - move file to target location

    ## close the connections
    sftp.close() # close the connection
    t.close()

if __name__ == "__main__":
    main()
