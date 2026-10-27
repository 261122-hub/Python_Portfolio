#fix_the_record.py
# This program prints a short record about a network device.

# runtime error -----> The variable name is misspelled.
device_name = "edge-router"

#syntax erorr ------> Variable names cannot start with a number
backup_ip = "192.0.2.1"

#syntax erorr -----> class' is a reserved keyword in Python
device_class = "router"

#runtime erorr --------> Because int() cannot convert the string "twenty-two" into an integer.
port = int(22)

print("Device:", device_name) 
print("Backup IP:", backup_ip)

#syntax erorr
print("Type:", device_class)

print("Port:", port)
#Python detects syntax errors first,
# because it must parse the code before it can execute it and discover other types of errors.

