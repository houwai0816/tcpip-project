#!/usr/bin/python
from progressbar import *
import socket
import sys
import time
import os
from progressbar import ProgressBar 					                #for the display of the loading bar
from termcolor import colored						                      #for changing the print function's color

try:
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	  # try to establish socket
except:
	print "Cannot create socket"
	sys.exit(1)

host="192.168.0.9"							                              #server ip address
port=12347							                                    	#the port server used
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)		#for solving the error :addresss is in use
server.bind((host,port))					                          	#bind the server ip address and port
server.listen(10)						                                 	#maximum amount server that can listen
file_list = ['server.py','tcp_info.py','dns_info.py','http_info.py']	#for execl() purpose

conn,addr = server.accept()						                                #server accept request from client,establish connection 
print "Get the connection from ",addr
conn.send("Connect server successfully")				                      #send message via tcp socket (server->client)
with open('result.txt','wb') as f:					                          #open a file
	while True:							                                            #while loop	(success open file)
		l=conn.recv(1024)				                                        	#receive data sent from client, buffer size :1024
		if not l:break				                                        		#break the loop when no data is received
		f.write(l)					                                            	#write the data to the file
	f.close()							                                              #close file

print colored("Server received the file","yellow")
time.sleep(1)								                                          #sleep for 1 sec
print colored("Connection closed!!","red")				
conn.close()								                                          #terminate the connection
server.close()								                                        #terminate the service
time.sleep(1)							                                          	#sleep for 1 sec
print "The server is processing data!Wait for 5 second"		
time.sleep(5)

try:
	forkpid1=os.fork()							                                    #try to fork a parent and child
except OSError as err:                                                #except the OS error
	print "Cannot fork process :",err

if forkpid1 != 0:								                                      #parent
	try:
		forkpid2 = os.fork()						                                  #try to create a second child
	except OSError as err:
		print "Cannot fork process :",err
	if forkpid2 !=0 :
		try:
			forkpid3 = os.fork()					                                  #try to create a third child
		except OSError as err:
			print "Cannot fork process :",err
		if forkpid3 != 0:
			child1 = os.wait()[0]					                                  #wait first child finish its program
			child2 = os.wait()[0]					                                  #wait second child finish its program
			child3 = os.wait()[0]				                                  	#wait third child finish its program
		elif forkpid3 == 0:					                                    	#child process
			os.execl("/usr/bin/python",file_list[0],file_list[1])	          #execl() to execute new program (pathname,self prog,new prog)
	elif forkpid2 == 0:							                                    #child process
		os.execl("/usr/bin/python",file_list[0],file_list[3])		          #execl() to execute new program
elif forkpid1 == 0:								                                    #child process
	os.execl("/usr/bin/python",file_list[0],file_list[2])			          #execl() to execute new program

cmd = "python filter.py > filter.txt"
os.system(cmd)									                                      #to execute the command
print colored("Server is analysing data","cyan")

pbar=ProgressBar()								                                    #sudo apt install python-pip
pbar.start()									                                        #pip install progressbar2
for i in pbar(range(100)):							                              #then can use the progressbar2 module to create loading bar
	time.sleep(0.05)
print "Data is analyzed!"

while True:
	answer = raw_input("Do you want to display the result?(y/n) :")		  #ask for user input to display the result
	if answer == 'y':							#y for open the file
		result=open('filter.txt').read()
		print result
		print "Finished"
		break
	elif answer == 'n':
		print "See you again"
		break
	print color("Invalid input.Try again","red")
