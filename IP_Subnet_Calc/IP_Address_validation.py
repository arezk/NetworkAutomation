############# Application #2 - Part #1 #############

import paramiko
import threading
import os.path
import subprocess
import time
import sys
import re


# Checking IP address file and content validity
def ip_is_valid():
    # Creating a Flag with Boolean value to validate against a condition.
    check = False
    global ip_list

    while True:
        # Prompting user for input
        print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"
        ip_file = raw_input("# Enter IP file name and extension: ")
        print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #"

        # Changing exception message
        try:
            # Open user selected file for reading (IP addresses file)
            selected_ip_file = open(ip_file, 'r')

            # Starting from the beginning of the file
            selected_ip_file.seek(0)

            # Reading each line (IP address) in the file
            ip_list = selected_ip_file.readlines()

            # Closing the file
            selected_ip_file.close()

        except IOError:
            print "\n* File %s does not exist! Please check and try again!\n" % ip_file
        print ip_list
        # Checking octets
        for ip in ip_list:
            a = ip.split('.')

            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (
                            int(a[0]) != 169 or int(a[1]) != 254) and (
                                    0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                check = True
                break

            else:
                print '\n* There was an INVALID IP address! Please check and try again!\n'
                check = False
                continue

        # Evaluating the 'check' flag
        if check == False:
            continue

        elif check == True:
            break


ip_is_valid()
