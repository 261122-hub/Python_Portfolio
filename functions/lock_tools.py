# lock_tools.py
# # This program checks account status and manages login attempts.

def is_locked(failed, max_tries=3):
   """Checks if the account is locked."""

   if failed >= max_tries: 
      return True
   else: 
     return False


def tries_left(failed, max_tries=3):
    """Calculates the number of remaining login attempts."""

    if is_locked(failed, max_tries): 
       return 0
    else: 
      return max_tries - failed
    

def status(failed):
     """Returns the current account status."""
     if is_locked(failed):
        return "locked"
     else: 
        tries = tries_left(failed)
        return f"active {tries} tries left"


print(is_locked(2))

print(is_locked(3))

print(is_locked(3, 5))

print(tries_left(1))

print(tries_left(7))

print(status(1))

print(status(4))



    




    

     
   
