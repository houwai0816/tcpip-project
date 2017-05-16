#!/usr/bin/python
import os
from termcolor import colored

cmd = 'tshark -i enp0s3 -c 200> tcp_output.txt'
os.system(cmd)

print colored("Source and Destination information is captured.\n",'yellow')
