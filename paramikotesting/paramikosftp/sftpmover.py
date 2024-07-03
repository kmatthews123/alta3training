#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

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
