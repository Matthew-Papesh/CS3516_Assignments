import socket as s

# Runs a TCP server when called. 
def server():
	# define client host name
	host = "127.0.0.1"
	# define network entry point for traffic
	port = 8450

	# open communication via tcp
	with s.socket(s.AF_INET, s.SOCK_STREAM) as tcp_socket:
		# enter specified entry point port and listen
		try:
			tcp_socket.bind((host, port))
			print("Binded to " + str(host) + ":" + str(port))
		except Exception as e:
			print(f"Error binding to socket: {e}")
		print("Server has began listening...")
		tcp_socket.listen()
		print("Server is still listening...")

		# confirm connection
		connection, address = tcp_socket.accept()
		# open connection and listen/receive data by tcp
		with connection:
			print("Connected TCP socket by address: " + str(address))
			while True:
				# listen for tcp data of 1024-bit buffer size
				data = connection.recv(1024)
				# contribute hosting server-side tcp as long as
				# client is still using service (not data == False)
				if not data:
					break
				# return data to client
				print("Sending data back to client: data == " + str(data))
				connection.sendall(data)

if __name__ == "__main__":
	# run tcp server
	server()
