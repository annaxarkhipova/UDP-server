# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:05:06 2019

@author: annaarkx
"""

import socket


add = '127.0.0.1'
udp_port = 6789
message = b'halo'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind(add, udp_port)


def server_sent_something_to_us():
    data, addr = sock.recvfrom(1024)

while True:
    sock.sendto(message, (add, udp_port))
    print('Sent a message to Server')