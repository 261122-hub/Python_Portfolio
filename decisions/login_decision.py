#login_decision.py
#Handles user authentication flow and makes decisions to grant or deny.
MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("Username: ")
failed_attempts = int(input("Failed attempts so far:"))
password = input("Password: ")

attempts_left = MAX_FAILED - failed_attempts -1
#I got them from the example next to the question. Print the answers that are in
if failed_attempts >= MAX_FAILED:
    print("Account locked")
elif username != KNOWN_USER:
    print("Unknown user")
elif password == STORED_PASSWORD:
    print("Access granted")
elif password != STORED_PASSWORD:
    print(f"Access denied. Attempts left: {attempts_left}")

# But in the example, the answer is in the last point \t; I wanted to put print in   
   
