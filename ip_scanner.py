# created on python --version 3.5.4
# This programme serch for all ip in given range using multithreading

import  os, threading

sys_d = 'TTL' if os.sys.platform == 'win32' else 'ttl'

def f(n):
	for i in range(n, n+4):
		ip = '10.195.97.{}'.format(i)
		if sys_d in os.popen('ping ' + ip + ' -n 1 -w 1 -b').read():
			print (ip)

# create 64 thread, each thread check 4 ip
if __name__ == '__main__':
	for j in range(0, 256, 4):
		p = threading.Thread(target = f, args = (j,))
		p.start()