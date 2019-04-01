# created on python --version 3.5.4
# This programme create a socket client for chat
import socket, threading, os

# Af--> Address Format used for http protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.195.97.220'
port = 1729
clear = 'cls' if os.sys.platform == 'win32' else 'clear'

# Connect to server
s.connect((host, port))
os.system(clear)
print ('Connection Established')
print ('='*61)


def receiver(_):
    while True:
        # Wait unless client sent packet
        msg = s.recv(1024)
        if msg == b'exit':
            break
        # Byte-string to string
        msg = msg.decode('utf-8')
        while msg:
            temp = msg[:50].strip()
            print( ' '*(60-len(temp)) + temp )
            msg = msg[60:]

def sender(_):
    while True:
        msg = input()
        # Send msg to client but not wait
        s.sendall(msg.encode('utf-8'))
        if msg == 'exit':
            break

if __name__ == '__main__':
    p1 = threading.Thread(target=receiver, args=('',))
    p2 = threading.Thread(target=sender, args=('',))

    p1.start()
    p2.start()
