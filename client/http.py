#!/usr/bin/python
import os
from termcolor import colored


cmd ='tshark -i enp0s3 -c100 -f "src port 443" -Nn -T fields -e ip.src_host > http_output.txt'
os.system(cmd)

print colored("HTTPS information is captured.\n",'yellow')
