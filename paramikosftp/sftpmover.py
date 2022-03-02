#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port
## how to connect (see other labs on using id_rsa private/public keypairs)
#t.connect(username="bender", password="alta3")
username=input("please enter your username")
password=input("please enterpassword")

## Make an sftp connection object
if username=="bender" and password =="alta3":
    t.connect()
    sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location
try:
    if(fi) :
        raise ValueError ('Invalid month')
except ValueError as msg:
    print('The program found an ',msg, "error")
## close the connections
sftp.close() # close the connection
t.close()

