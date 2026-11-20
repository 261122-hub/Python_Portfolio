# security_toolkit.py
# This program provides basic cybersecurity tools for ports, passwords, and PINs.


MIN_LENGTH = 8
def border(width): 
    """Prints a border of asterisks of the specified width."""

    print("+" + "-" * (width + 2) + "+")

def show_box(text):
    """Prints text inside a border box."""

    width = len(text)
    border(width)
    print(f"| {text} |")
    border(width)

def show_menu():
    """Displays the main menu for the security toolkit."""

    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")  
    print("3. PIN guessing time")
    print("q. Quit")

def port_range(port):
    """Prints a range of ports from start to end."""
    if port < 0 or port > 65535: 
      return "invalid"
    elif 0 <= port <= 1023:
        return "system"
    elif 1024 <= port <= 49151:
        return "user"
    elif 49152 <= port <= 65535:
        return "dynamic"
    

def check_port():
    """Prompts the user for a port number and checks its range."""
    port = int(input("Port: "))
    port_type = port_range(port)
    show_box(f"Port {port}: {port_type}")


def password_problem(password, username):
    """Checks if the password is valid."""

    if password == username:
        return " same as username"
    if len(password) < MIN_LENGTH:
            return " too short."
    else:
        return ""

def check_password():
    """Prompts the user for a username and password and checks its validity."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem:
        show_box(f"Password rejected: {problem}")
    else:
        show_box("Password accepted.")

def days_to_guess(digits, per_second):
    """Calculates the number of days it would take to guess a PIN."""
    return (10 ** digits) // per_second // 86400

def check_pin():
    """Prompts the user for the number of digits in a PIN and the number of guesses per second, then calculates the time to guess."""
    digits = int(input("digits "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")


show_menu()
checks_done = 0
while True:
        choice = input("Choice (1, 2, 3, or q): ")
        if choice == "1":
            check_port()
            checks_done += 1
        elif choice == "2":
            check_password()
            checks_done += 1
        elif choice == "3":
            check_pin()
            checks_done += 1
        elif choice == "q":
            show_box(f"Checks done: {checks_done}")
            break
        else:
            print("Invalid choice. Please try again.")




    



   

    

    




   


    