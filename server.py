# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:10:44 2019

@author: annaarkx
"""

import socket
import time

add = '127.0.0.1'
udp_port = 6789


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet; UDP

# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
server.bind((add, udp_port))
    
def recieved():
    data, addr = server.recvfrom(1024)
    print('Got from client this - ', data)
        
def proccess():
    print('Starting something special')
    time.sleep(5)
    res = 900
    print('it is the end')
    print('Reply to client - ', res)

    
while True:
    recieved()
    proccess()