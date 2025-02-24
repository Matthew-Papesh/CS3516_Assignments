from socket import *
import socket
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
	
# Create a server TCP socket 
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = sys.argv[1], 5665
# Bind the socket to a port and start listening
tcpSerSock.bind((host, port))
tcpSerSock.listen()

while True:
	# Start receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	message = ""

	try:
		message = tcpCliSock.recv(1024).decode()
	except UnicodeDecodeError:
		print("Received binary data, skipping decoding.")
		message = None

	print('xy:message', message, '\r\n')
	if not message or len(message.split()) < 2:
		print("Invalid HTTP request received.")
		tcpCliSock.close()
		continue

	# Extract the filename from the given message
	print('xy:message_split', message.split()[1], '\r\n')
	filename = ""

	try:
		filename = message.split()[1].partition("/")[2]
	except IndexError as e:
		print("Malformed request. Closing connection.")
		tcpCliSock.close()
		continue

	print('xy:filename', filename)
	
	fileExist = "false"
	filetouse = "/" + filename
	print('xy:filetouse', filetouse, '\r\n')

	try:
		# Check wether the file exist in the cache
		f = open(filetouse[1:], "rb")                      
		outputdata = f.read()                        
		fileExist = "true"
		# ProxyServer finds a cache hit and needs to generate a response message
		#Fill in start
		tcpCliSock.send("HTTP/1.1 200 OK\r\n".encode())
		#Fill in end
		tcpCliSock.send("Content-Type:text/html\r\n".encode())
		# Socket then needs to send the file data to the original client
		#Fill in start
		tcpCliSock.send("\r\n".encode())
		tcpCliSock.sendall(outputdata)
		#Fill in end
		print('Read from cache')     
			
	# Error handling for file not found in cache
	except IOError:
		if fileExist == "false": 
			# Create a socket on the proxyserver to connect with original server
			c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			hostn = filename.replace("www.", "", 1)
			print('xy:hostn', hostn, '\r\n')       

			try:
				# Connect to the socket to port 80
				#Fill in start
				c.connect((hostn, 80))
				#Fill in end
				# Create a temporary file on this socket so that later the socket can be used to read data
				fileobj = c.makefile('rb', buffering=0)    
				#send a request to original server to get the file requested by original client
				#Fill in start
				c.sendall((f"GET /{filename} HTTP/1.1\r\nHost: {hostn}\r\n\r\n").encode())
				#Fill in end          
  
				# Read the response into buffer
				print('xy:begin to read response into buffer \r\n')    
				#print("S1\n")                               
				buff = fileobj.readlines()
				#print("TRET\n")
				# Create a new file in the cache for the requested file. 
				tmpFile = open("./" + filename,"wb")  
				print(f"BUFF: {buff}\n")
				#Also send the response in the buffer to client socket and the corresponding file in the cache
				#Fill in start
				data = b""
				for line in buff:
					tmpFile.write(line)
					data += line
				tcpCliSock.sendall(data)
				#Fill in end
			except:
				print("Illegal request: requested URL is probably wrong and 404 message will be sent")  
				#if the requested webpage does not exist, send back a 404 response message to the original client  
				#Fill in start
				tcpCliSock.send("HTTP/1.1 404 Not Found\r\n".encode())
				#Fill in end                           
				tcpCliSock.send("Content-Type:text/html\r\n".encode())
				tcpCliSock.send("\r\n".encode())                                           
		else:
			# HTTP response message for file not found
			#Fill in start
			tcpCliSock.send("HTTP/1.1 404 Not Found\r\n".encode())
			#Fill in end  
			tcpCliSock.send("Content-Type:text/html\r\n".encode())
			tcpCliSock.send("\r\n".encode())
	# Close the connection socket connected to the original client
	#Fill in start
	tcpCliSock.close()
	#Fill in end  
# Close the welcoming server socket   
tcpSerSock.close()