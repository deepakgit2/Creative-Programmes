# created on python --version 3.5.4
# This programme create a socket server for file transfer
import socket, threading, os, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 1729
clear = 'cls' if os.sys.platform == 'win32' else 'clear'
# receiving file directory
recv_dir = r'C:\Users\deepak.singh\Documents\flask_test'

s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
os.system(clear)
print('Connection Established')


def receiver(_):
    while True:    
        f_size, f_name = conn.recv(1024).decode('utf-8').split()
        if f_name == 'exit':
            break
        print ('', end='\r')
        print(f_name + ' '*20)

        f_size = int(f_size)
        d_size, count, tic = 0, 0, time.time()
        with open(os.path.join(recv_dir, f_name), 'wb') as f:
            while d_size < f_size:
                data = conn.recv(1024)
                f.write(data)
                d_size += len(data)
                p = int(d_size/f_size*20)
                if p >= count:
                    print('|' + '|'*p + ' '*(20-p) + '|', end='\r')
                    count += 1
            print('|' + '|'*p + ' '*(20-p) + '| Received ({:.2f})'.format(time.time()-tic) )

def sender(_):
	while True:
		file_dir = input('sending_file_dir: ' )
		if file_dir == 'exit':
			conn.sendall(b'0 exit')
			break
		f_size = os.stat(file_dir).st_size
		conn.sendall(str(f_size).encode('utf-8') + b' ' + os.path.basename(file_dir).encode('utf-8'))
		
		temp = 0
		print ('', end='\r')
		print(file_dir + ' '*20)

		d_size, count = 0, 0
		tic = time.time()
		with open(file_dir, 'rb') as f:
			chunk = f.read(1024)
			tic = time.time()
			while chunk:
				conn.sendall(chunk)
				d_size += len(chunk)
				p = int(d_size/f_size*20)
				if p >= count:
					print('|' + '|'*p + ' '*(20-p) + '|', end='\r')
					count += 1
				chunk = f.read(1024)
			
			print('|' + '|'*p + ' '*(20-p) + '| Sent ({:.2f})'.format(time.time() - tic) )

if __name__ == '__main__':
	p1 = threading.Thread(target=receiver, args=('',))
	p2 = threading.Thread(target=sender, args=('',))

	p1.start()
	p2.start()
