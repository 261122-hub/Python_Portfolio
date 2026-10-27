# device_card.py - stores and displays device information
MAX_CONNECTIONS = 100

device_name = "MacBook pro"
service = "HTTPS"
device_ip = "192.0.2.20"
open_port= 443
print("Name:", device_name) 
print("IP:", device_ip)
print("OpenPort:", open_port)
print( "Service:", service)
print("Max connctions:", MAX_CONNECTIONS)

service = "SSH"
open_port = 22
print("Update service:", service, "on Part:", open_port)