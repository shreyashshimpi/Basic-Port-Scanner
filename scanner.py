#!/bin/python3

import sys
import socket
from datetime import datetime

#Define the target here
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	
else:
	print("-" * 25,"\nInvalid Arguments please use 'python3 scanner.py <IP or domain>'\n","-" * 25)

#Adding some response
print("-" * 50)
print("Scanning target: " +target)
print("Time Started: " +str(datetime.now()))
print("-" * 50)

#Trying to scan
try:
	for port in range (1,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print("checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\n Exiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname couldnt be resolved")

except socket.error:
	print("Error")
		
		
