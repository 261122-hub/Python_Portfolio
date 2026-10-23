# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# syntax ----> I forgot the :
if len(password) < MIN_LENGTH: 
    print("- Too short.")
# semantic ----> The first one printed, but in the answer shown to the right of the question, the result for both conditions appears—as if it were an `elif`.
if password == username: 
    print("- Same as the username.") 

# semantic
if len(password) >= 16:
    strength = "long"  
# Let’s assume this takes 12 days—or any number greater than 16.
# You will print the first condition because the number is greater than 12, and therefore the second condition is unnecessary.

elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
print(f"Length: {len(password)} ({strength})")    

# semantic -----> Because if any one of the three conditions above is met, nothing will be printed; we must remove the preceding spaces.