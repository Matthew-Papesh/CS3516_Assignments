import socket as s

def client():
	# define server host name
	host = "127.0.0.1"
	# define network entry point for traffic
	port = 8450

	# open communication via tcp
	with s.socket(s.AF_INET, s.SOCK_STREAM) as tcp_socket:
		# connect to specified entry point port on server network
		tcp_socket.connect((host, port))
		while True:
			# transmit data from input
			msg = input("transmitting msg: ")
			tcp_socket.sendall(msg.encode()) # encode data
			# end client if told to exit
			if msg == "exit":
				print("exiting; ending service...")
				break
			# retrieve returned message from tcp 10240bit buffer size
			data = tcp_socket.recv(1024)
			# print data
			print("Received data: " + str(data))
	print("client ended")
if __name__ == "__main__":
	# run tcp client
	client()
