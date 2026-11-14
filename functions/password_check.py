# password_check.py
# # This program checks password validity.

def long_enough(password, minimum=8): 
    """Checks if the password is long enough."""
    if len(password) >= minimum: 
        return True

def differs_from_username(password, username):
    """Checks if the password is different from the username."""
    if password != username: 
        return True


def password_ok(password, username):
    """Checks if the password is valid."""

    return long_enough(password, minimum=8) and differs_from_username(password, username)

username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")
    
        
  

