# fix_the_functions.py


def print_header():

   """Display the report header."""

   print("=" * 30)

   print("LOGIN REPORT")

   print("=" * 30)
print_header()
 #The first error is a runtime error, because it involves a call to a function that has not been defined.
 # part 1 

def lock_minutes(failed, minutes=15):

  """Return failed * minutes if failed >= 3, else 0."""

  if failed >= 3:
   total = failed * minutes
# The second error is a semantic error, because if we always use `return 0`, it will always output 0.
   return total
  else: 

   return 0


def login_line(username, failed):

  """Return one line of the report."""

  minutes = lock_minutes(failed)

  return f"{username}: {failed} failed, locked {minutes} min"
print(login_line(username="sara", failed=4))
# The third error is a runtime error, because it attempts to print 'user', which is not defined.
print(login_line("omar", 1))
# It must be print in order to print





