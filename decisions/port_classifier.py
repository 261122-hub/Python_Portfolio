#port_classifier.py
#Classifies and analyzes network ports to identify traffic types or security states

port = int(input("Port: "))


if 0 <= port <= 1023:
    print("Range: system")
    if port == 22:
     print("Service: ssh")
    elif port == 80:
     print("Service: http")
    elif port == 443:
     print("Service: https")
elif 1024 <= port <= 49151:
    print("Range: user")
elif 49152 <= port <= 65535:
    print("Range: dynamic or private")   
else:
    print ("Invalid port: use a number from 0 to 65535.")


# For problem 4, my initial approach was to use an `if` statement separate from the one above it; however, I realized that all three numbers fall within the range (0–1023) covered by the first `if` statement.

# if port == 22:
#   print("Service: ssh")
# elif port == 80:
#   print("Service: http")
# elif port == 443:
#    print("Service: https")

# That’s how I had them, but I changed them back.

