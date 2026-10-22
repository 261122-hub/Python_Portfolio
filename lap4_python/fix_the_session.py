
# This program reports a user's session time.

username = input("Username: ")

#runtime--------لازم احط int
total_seconds = int(input("Session length in seconds: "))


#semantic------لازم احط كمان \
minutes = total_seconds // 60

seconds = total_seconds % 60
print("=" * 30)

#semantic------ f ناسي احط 
print(f"User: {username}")

#runtime------- كان في +بين نص ورقم 
print(f"Session: {minutes} min {seconds} s")

print("=" * 30)