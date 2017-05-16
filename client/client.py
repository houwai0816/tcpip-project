#!/usr/bin/python
import socket
import os
import sys
from progressbar import *
import time
from termcolor import colored
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)					                    #create a tcp socket

host = raw_input(colored('Please enter server address to connect : ','cyan'))		#give user insert server ip address
port = 12347										                                                #the port server used
x=0											                                                        #for the times in while loop

args = ['client.py','tcp.py','dns.py','http.py']					                      #for the use of execl() (pathname,self,new prog)
file_list= ['tcp_output.txt','dns_output.txt','http_output.txt']			          #the captured data and store in these files

time.sleep(2)										                                                #wait for 2 seconds
print colored('Ready to capture...','green')
try:
	forkpid1 = os.fork()								                                          #try to fork parent and child
except OSError as err:									                                        #execept the OS error occur
	print "Can't fork the process!\n",err

if forkpid1 != 0:								                                              	#if parent process
	forkpid2 = os.fork()								                                          #create second child
	if forkpid2 != 0:
		forkpid3 = os.fork()							                                          #create third child
		if forkpid3 != 0:							
			child1 = os.wait()[0]						                                          #wait for first child process
			child2 = os.wait()[0]						                                          #wait for second child process
			child3 = os.wait()[0]					                                          	#wait for third child process
		elif forkpid3 == 0:						                                            	#child process execute
			os.execl("/usr/bin/python",args[0],args[2])			                          #use execl() to execute new program
	elif forkpid2 == 0:								                                            #child process execute
		os.execl("/usr/bin/python",args[0],args[3])			                          	#use execl() to execute new program
elif forkpid1 == 0:								                                            	#child process execute
	os.execl("/usr/bin/python",args[0],args[1])				                          	#use execl() to execute new program

print 'Please wait checking connection with ',host,'...'
cmd = 'ping -w 5 192.168.0.9 > ping.txt'						                            #capture and pipe the information to txt file
os.system(cmd)										                                              #execute the command
files = open('ping.txt','rb')							                                    	#open ping.txt file
lines = files.readlines()							                                        	#read the content line by line
if lines:									                                                    	#if the line has content
	last_l = lines[-2]							                                            	#print the content
print '\n'
pbar=ProgressBar()								                                            	#display the loading bar
pbar.start()										                                                #start the progressbar2 function
for i in pbar(range(100)):							                                      	#run 5~6 seconds
	time.sleep(0.04)
print colored(last_l,'green')
print colored("Connecting to the server",'yellow')
s.connect((host,port))								                                        	#connect to the server
print s.recv(1024)							                                            		#print the data receive from server after connect
while x<3:								                                                  		#loop when x <3
	f=open(file_list[x],'rb')					                                        		#open file 
	l=f.read(1024)								                                              	#read the file content
	while(l):								                                                    	#while there is content to be read
		s.send(l)							                                                    	#send the content to the server
		if not l:break							                                              	#if there is no more data,break the loop
		l=f.read(1024)						                                              		#read the content again
	f.close()							                                                    		#close the file
	x=x+1									                                                      	#increment x by 1
print colored('The file is transferred','green')			                      		#print message

s.close()									                                                    	#close the connection
print colored('Connection terminate','red')
