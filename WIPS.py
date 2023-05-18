import socket
from threading import Thread
import threading
import os

HOST = "0.0.0.0"
print(socket.gethostname())
PORT = 8080
clients = set()
clientLock = threading.Lock()
def on_new_client(cs, addr):
    while True:
        data = cs.recv(1024)
        if not data:
            break
        with clientLock:
            for c in clients:
                c.sendall(data)
    cs.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    with clientLock:
        clients.add(conn)
    print("New connection from {addr}" )
    thread = Thread(target=on_new_client, args=(conn, addr))
    thread.start()
    
conn.close()
thread.join()        


