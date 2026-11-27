
# fix_the_parser.py
LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
    return line[0:5]
# There is a logical error in the answer at 09:01–09:02; the value 4 should be included in the interval.
def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    return user.lower()

# Without storing it, user.lowe() is a logical error. It was set
def is_failed(line):
    """Return True if the line reports a failed login."""
    return "failed".upper() in line
# To make the entire word uppercase, I used the upper() function—that was a logic error.
def hide_first(user):
    """Return user with its first letter replaced by *."""
    user = user[1:5]
    return "*" + user
# A runtime error occurs because you cannot modify a string directly.


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
print(f"Length: {len(LINE)}")

# Runtime error: The len() function is externally inserted; the LINE variable inside the len(0) function is incorrect.

