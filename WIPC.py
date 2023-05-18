import socket
from threading import Thread
import threading
import time
import os
import subprocess

"""Dear me you need to upgrade this to include sqlite stuff.
I mean come on dude, chat history is amazing.
Also remember to load the latest working version to saves, incase of murphy's law"""
HOST = "10.101.129.29" ##This is school
##HOST = "192.168.1.123" ##This is home
##HOST = socket.gethostbyname('1000D') 
PORT = 8080
TAG = input("Enter screenname:")
global stuff
stuff = ""
Enter = TAG + " has entered the chat!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
text = set()
inputLock = threading.Lock()
c = threading.Condition()
##Temp solution for recv data
def get():
    while True:
        data = s.recv(1024).decode()
        print(f"{data!r}")
def inputL():
    global stuff ##took me forever to figure out
    while True:
        time.sleep(1/1000)
        ##input doesn't cause pause in program
        stuff = input("")
        if stuff == "quit()":
            s.sendall(stuff.encode())
            s.close()
            thread.join()
            the.join()
            break
s.connect((HOST, PORT))
s.sendall(Enter.encode())
data = s.recv(1024).decode()
print(f"{data!r}")
print("To exit type in quit()")
thread = Thread(target=inputL)
## Temp solution for now.
the = Thread(target=get)
the.start()

thread.start()
while True:
    if stuff == "quit()":
        s.sendall(stuff.encode())
        s.close()
        thread.join()
        the.join()
        break
    mess = TAG + ': ' + stuff
    if stuff != "":
        ##sending stuff
        s.sendall(mess.encode())
        stuff = ""
