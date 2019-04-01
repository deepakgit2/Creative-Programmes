# created on python --version 3.5.4
# This programme create a socket server for chat
import socket, threading, os

# Af--> Address Format used for http protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 1729
clear = 'cls' if os.sys.platform == 'win32' else 'clear'

# Crete server at given ip and port
s.bind((host, port))
# It start listen to n+1 clients (n=0 by default )
s.listen()

# wait unless client online or connect to this server
conn, addr = s.accept()
os.system(clear)
print('Connection Established')
print('='*61)

def receiver(_):
    while True:
        # Wait unless client sent packet
        msg = conn.recv(1024)
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
        conn.sendall(msg.encode('utf-8'))
        if msg == 'exit':
            break

if __name__ == '__main__':
    p1 = threading.Thread(target=receiver, args=('',))
    p2 = threading.Thread(target=sender, args=('',))

    p1.start()
    p2.start()
