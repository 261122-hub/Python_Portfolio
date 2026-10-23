MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("Username: ")
failed_attempts = int(input("Failed attempts so far:"))
password = input("Password: ")

attempts_left = MAX_FAILED - failed_attempts -1
#جبتهن من المثال الي جنب السؤال  print  الاجوبة الي في 
if failed_attempts >= MAX_FAILED:
    print("Account locked")
elif username != KNOWN_USER:
    print("Unknown user")
elif password == STORED_PASSWORD:
    print("Access granted")
elif password != STORED_PASSWORD:
    print(f"Access denied. Attempts left: {attempts_left}")

# بس في المثال الجواب في نقطة \t  الاخيرة كنت بدي احط  print في
   
   
