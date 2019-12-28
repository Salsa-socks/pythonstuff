import socket
from threading import *
import sys
from _thread import *

server = "10.0.0.11" # IP aaddress of wherever server is being run
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            
            conn.sendallstr.encode(reply)
        except:
            print("something went wrong")
            break


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn,))