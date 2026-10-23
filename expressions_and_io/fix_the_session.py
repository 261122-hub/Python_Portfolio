
# This program reports a user's session time.

username = input("Username: ")

#runtime--------I must include 'int'
total_seconds = int(input("Session length in seconds: "))


#semantic------I need to add more \
minutes = total_seconds // 60

seconds = total_seconds % 60
print("=" * 30)

#semantic------ f I forgot to put
print(f"User: {username}")

#runtime------- There was a '+' between text and a number.
print(f"Session: {minutes} min {seconds} s")

print("=" * 30)