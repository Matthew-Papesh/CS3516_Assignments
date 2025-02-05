import socket as s

# Runs a UDP server when called. 
def server():
	# define client host name
	host = "127.0.0.1"
	# define network entry point for traffic
	port = 8451

	# open communication via udp
	with s.socket(s.AF_INET, s.SOCK_DGRAM) as udp_socket:
		# enter specified entry point port and bind
		try:
			udp_socket.bind((host, port))
			print("Bounded to " + str(host) + ":" + str(port))
		except Exception as e:
			print(f"Error binding to socket: {e}")
		# open connection by udp
		while True:
			# retrieve any received data from various clients by address
			data, address = udp_socket.recvfrom(1024)
			print("Received from client " + str(address) + ": " + str(data))

if __name__ == "__main__":
	# run udp server
	server()

