#fix_the_record.py
# This program prints a short record about a network device.
device_name = "edge-router"

#syntax erorr
end_ip = "192.0.2.1"

#syntax erorr
device_class = "router"

#runtime erorr
port = int(22)

print("Device:", device_name) 
print("Backup IP:", end_ip)

#syntax erorr
print("Type:", device_class)

print("Port:", port)
#Python detects syntax errors first,
# because it must parse the code before it can execute it and discover other types of errors.

