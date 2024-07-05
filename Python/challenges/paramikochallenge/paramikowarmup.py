#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
   
    with open("/workspaces/alta3training/challenges/paramikochallenge/credz.txt", "r") as cred_txt:
        for line in cred_txt:
            credz = line.split()
            print(credz)
            # harvest private key for all 3 servers
            mykey = paramiko.RSAKey.from_private_key_file("/workspaces/alta3training/paramikosshrsa/.ssh/id_rsa")
                ## create a session object
            sshsession = paramiko.SSHClient()

            ## add host key policy
            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ## display our connections
            print("Connecting to... " + credz[0]+ "@" + credz[1])

            ## make a connection
            sshsession.connect(hostname=credz[1], username=credz[0], pkey=mykey)

            ## touch the file goodnews.everyone in each user's home directory
            sshsession.exec_command("touch /home/" + credz[0] + "/goodnews.everyone")

            ## list the contents of each home directory
            sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + credz[0])

            ## write output to log file
            with open("results.log", "a") as logfile:
                print(sessout.read().decode('utf-8'), file=logfile)

            ## close/cleanup SSH connection
            sshsession.close()

    print("Thanks for looping with Alta3!")

main()
