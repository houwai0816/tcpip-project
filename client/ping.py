#!/usr/bin/python


import os

os.system('ping -w 5 8.8.8.8  > ping.txt')

files = open('ping.txt','rb')
lines = files.readlines()
if lines:
	last_l = lines[-2]	

print last_l


