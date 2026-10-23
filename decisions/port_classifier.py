port = int(input("Port: "))


if 0 <= port <= 1023:
    print("Range: system")
elif 1024 <= port <= 49151:
    print("Range: user")
elif 49152 <= port <= 65535:
    print("Range: dynamic or private")   
else:
    print ("Invalid port: use a number from 0 to 65535.")

if port == 22:
    print("Service: ssh")
elif port == 80:
    print("Service: http")
elif port == 443:
    print("Service: https")
