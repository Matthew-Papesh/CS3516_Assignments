import socket as s

def client():
	# define server host name
	host = "127.0.0.1"
	# define network entry point for traffic
	port = 8451

	# open communication via udp
	with s.socket(s.AF_INET, s.SOCK_DGRAM) as udp_socket:
		while True:
			# input data from user
			msg = input("transmitting msg: ")
			# end client if told to exit
			if msg == "exit":
				print("exiting; ending service...")
				break
			# temporarily connect for single transmission by udp
			udp_socket.sendto(msg.encode(), (host, port))
	print("client ended")
if __name__ == "__main__":
	# run udp client
	client()
