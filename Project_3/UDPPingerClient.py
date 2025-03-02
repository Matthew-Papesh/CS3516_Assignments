#please note that you only need to run the server on your local host, or on a different device on the same local network as the client. The wpi server will not allow you to have a port open for test. 

import sys, time
from datetime import datetime
import calendar
from socket import *
import socket

# get weekday in short-hand format
def get_weekday() -> str:
	day = calendar.day_name[datetime.today().weekday()]
	if day == "Sunday":
		return "SUN"
	elif day == "Monday":
		return "MON"
	elif day == "Tuesday":
		return "TUE"
	elif day == "Wednesday":
		return "WED"
	elif day == "Thursday":
		return "THUR"
	elif day == "Friday":
		return "FRI"
	elif day == "Saturday":
		return "SAT"
	
# get month in short-hand format
def get_month(index: int) -> str:
	index = min(12, max(0, index-1))
	months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
	return months[index]

# get formatted date and time 
def get_datetime() -> str:
	weekday, month = get_weekday(), get_month(int(datetime.now().strftime("%m"))) 
	day, date_time = datetime.now().strftime("%d"), datetime.now().strftime("%H:%M:%S 20%y")
	return f"{weekday} {month} {day} {date_time}"

# Get the server hostname and port as command line arguments
server_host =  sys.argv[1]
server_port = int(sys.argv[2])
server_address = (server_host, server_port)
timeout = 1 # in second
 
# Create UDP client socket, note the use of SOCK_DGRAM for UDP datagram packet
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set socket timeout as specified
client_socket.settimeout(1) # set for 1 second

# Sequence number of the ping message
ptime = 0  
# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent
    ping = f"PING {ptime} {get_datetime()}".encode()

    try:
        # Get the message sent time
        initial_time = time.time() # begin timing echoed ping
        client_socket.sendto(ping, server_address) # send ping message
        sender_reply, sender_address = client_socket.recvfrom(1024) # wait to receive reply
        elapsed_time = time.time() - initial_time # get elapsed time from echoed ping
        rtt = elapsed_time if ping.decode() == sender_reply.decode() else None # get time for echo
        # Display the server response as an output with RTT
        print(f"Reply from {server_host}: {sender_reply.decode()}\nRTT: {elapsed_time}\n")
    except socket.timeout: # exception thrown; ping timed out
        # Server has no response and assume the packet is lost
        print("Request timed out.\n")
    continue

# Close the client socket
client_socket.close()
