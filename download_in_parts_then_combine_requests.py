# This programme download a file in parts then combine them 

import requests, os

url = 'https://www.sample-videos.com/zip/50mb.zip'
file_name = 'abc_xyz.zip'
limit = 10*1024*1024 # 10mb
chunk_s = 512*1024 # 0.5mb
root_dir = os.getcwd()
os.chdir( root_dir )

r = requests.get(url, stream=True)
file_size = int(r.headers['content-length'])
# Ceil function using floor function
file_num = -(-file_size//limit)

itr = r.iter_content(chunk_s)
print(file_num)
for j in range(1, file_num+1):
	loop_c = 0
	loop_e = limit if j<file_num else file_size-(j-1)*limit
	temp_file = 'temp__file_{}'.format(j)
	with open(temp_file, 'wb') as f:
		while loop_c < loop_e:
			f.write(itr.__next__())
			loop_c += chunk_s
	print ('file_{} downloaded'.format(j))

with open('temp__file_1', 'ab') as f1:
	for i in range(2, file_num+1):
		t_file = 'temp__file_{}'.format(i)
		with open(t_file, 'rb') as f2:
			data = f2.read()
		f1.write(data)
		os.remove(t_file)

os.rename('temp__file_1', file_name)

