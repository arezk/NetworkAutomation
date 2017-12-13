

import paramiko
import sys
import re
import os.path
import threading
import time
import subprocess

#Validate the IP Address
def ip_add_valid():
    valid=False
    global ip_add_list
    
    while True:
        # User to input the IP Address file name
        print "\n # # # # # # # # # # # # # # # #\n"
        ip_file= raw_input("Enter The IP File Name: ")
        print "\n # # # # # # # # # # # # # # # #\n"
        
        # Validating the file with Try and Except
        
        try:
            # Open the IP Address File that has been entered
            entered_ip_file = open(ip_file, 'r')
            
            #start from the beginning of the file to read
            entered_ip_file.seek(0)
            
            # assign the global variable and read the file line by line
            
            ip_add_list = entered_ip_file.readlines()
            
            # Then closing the file
            
            entered_ip_file.close()
        except IOError:
            print "\n* File %s does not exist! Please check and try again!\n" % ip_add_file
        
        # Checking the validity of each IP Address FORMAT... This snippest can be used
        
        for ip in ip_add_list:
            octects=ip.split('.') # splitting the IP address into octets.
           # print octects
            
            #Criteria for IP Address validation using each octect
            if (len(octects) == 4) and (1 <= int(octects[0]) <= 223) and (int(octects[0]) != 127) and (int(octects[0]) != 169 or int(octects[1]) != 254) and (0 <= int(octects[1]) <= 255 and 0 <= int(octects[2]) <= 255 and 0 <= int(octects[3]) <= 255):
                print '\n* The IP Address(s) is/are Valid!\n'
                valid = True
                break
            else:
                print '\n* There was an INVALID IP address! Please check and try again!\n'
                valid = False
                continue
            
        if valid == True:
            break
        elif valid == False:
            break

ip_add_valid()

      ################### Testing the Reachability of the IP addresses ################

