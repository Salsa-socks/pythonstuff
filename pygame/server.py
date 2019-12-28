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

def read_pos(str1):
    str1 = str1.split(",")
    return int(str1[0]), int(str1[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048*2).decode())
            pos[player] = data
            
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(make_pos(reply)))
        except:
            print("something went wrong")
            break

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer += 1