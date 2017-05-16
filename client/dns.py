import os
from termcolor import colored
cmd ='tshark -i enp0s3 -f "src port 53" -n -T fields -e dns.qry.name -c100 -a duration:30 > dns_output.txt'

os.system(cmd)
print colored("DNS information is captured.\n",'yellow')
