import socket
import artnet
from artnet import packet, daemon,  STANDARD_PORT, OPCODES, STYLE_CODES

UDP_IP = "127.0.0.1"
UDP_PORT = 6454
 
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
