#!/usr/bin/python
import os

cmd = "sed -n -e '201,300p' result.txt > dns_info.txt"
os.system(cmd)
