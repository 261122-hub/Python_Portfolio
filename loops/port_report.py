# port_report.py
# Program to report and classify network ports into system, user, or dynamic ranges.

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

count = 0

for port in range(start_port, end_port + 1):
    # I added +1 because the question asks for the last endpoint of the interval.
    count += 1
    if 0 <= port <= 1023: 
        print (f"{port}: system")
    elif 1024 <= port <= 49151: 
        print (f"{port}: user")
    elif 49152 <= port <= 65535:
        print (f"{port}: dynamic")
print (f"Ports checked: {count} ")

# 