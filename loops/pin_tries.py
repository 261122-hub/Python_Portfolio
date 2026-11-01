# pin_tries.py 
# # Program to simulate a PIN entry system with a maximum number of tries and card blocking feature.

MAX_TRIES = 3
CORRECT_PIN = "2580"
tris = 0

while tris < MAX_TRIES: 
    PIN = input ("PIN: ")
    tris += 1
    if PIN == CORRECT_PIN:
        print ("Access granted.")
        break
    else:
        tries_left = MAX_TRIES - tris
        print (f"Wrong PIN. Tries left: {tries_left}")
        if tris == MAX_TRIES:
           print ("Card blocked.")

