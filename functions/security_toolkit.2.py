MIN_LENGTH = 8


def border(width):
    """Print the top or bottom border of a box."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Print text inside a border box."""
    width = len(text)
    border(width)
    print(f"| {text} |")
    border(width)


def show_menu():
    """Print the program title and menu options."""
    print("SECURITY TOOLKIT")
    print("1. Check port")
    print("2. Check password")
    print("3. Check PIN")
    print("q. Quit")


def port_range(port):
    """Return the range category for a given port number."""
    if port < 0 or port > 65535:
        return "invalid"
    elif port <= 1023:
        return "system"
    elif port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Ask for a port number and display its range in a box."""
    port = int(input("Port: "))
    category = port_range(port)
    show_box(f"Port {port}: {category}")


def password_problem(password, username):
    """Return the first problem found with the password, or empty string."""
    if password == username:
        return "same as username"
    if len(password) < MIN_LENGTH:
            return "too short"
    return ""


def check_password():
    """Ask for username and password and show if it is accepted or rejected."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem != "":
        show_box(f"Rejected: {problem}")
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Calculate whole days needed to guess all PIN combinations."""
    return (10 ** digits) // per_second // 86400


def check_pin():
    """Ask for PIN details and show days to guess in a box."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")


def main():
    """Run the security toolkit menu loop."""
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


if __name__ == "__main__":
    main()
