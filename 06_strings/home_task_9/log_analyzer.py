# log_analyzer.py
# # This program analyzes log files to identify and report security events.

ALERT_LIMIT = 3
LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""


def get_field(line, name): 
    """Extracts a specific field value from a log line."""
    start = line.find("user", " ")
    if start == -1:
        return ""


def get_status(line):
    """Return the second word of the log line."""
    words = line.split()

    if len(words) >= 2:
        return words[1]

    return ""





def count_status(status):
    """Count the number of log entries matching the given status."""
    count = 0
    for line in LOG.splitlines():
        if get_status(line) == status:
            count += 1
    return count





def show_summary():
    """Print the total lines, failed attempts, and successful attempts."""
    print("Lines:", len(LOG.splitlines()))
    print("Failed:", count_status("FAILED"))
    print("OK:", count_status("OK"))





def search(keyword):
    """Search for a keyword and print matching lines."""
    matches = 0
    number = 1

    for line in LOG.splitlines():
        if keyword.lower() in line.lower():
            print(number, line)
            matches += 1

        number += 1

    print("Matches:", matches)



def ip_report(ip):
    """Report failed logins from an IP address."""
    count = 0
    for line in LOG.splitlines():
        if get_status(line) == "FAILED" and get_field(line, "ip") == ip:
            time_str = line.split()[0]
            user = get_field(line, "user")

            print(time_str, user)
            count += 1

    print(f"Failed logins from {ip}: {count}")

    if count >= ALERT_LIMIT:
        print("ALERT: possible password guessing.")

def mask(word):
    """Mask the middle letters of a word."""

    if len(word) <= 2:
     return "*" * len(word)
     return word[0] + "*" * (len(word) - 2) + word[-1]


def show_masked():
    """Print the log with every username maske"""

    for line in LOG.splitlines():
         user = get_field(line, "user")
         if user:
            updated = line.replace()
            "user=" + user,
            "user=" + mask(user),
           
            print(updated)

def show_menu():
    """Print the title and the five menu lines."""
    print("AUTH LOG ANALYZER")
    print("1. Summary")
    print("2. Search")
    print("3. IP report")
    print("4. Masked log")
    print("q. Quit")


show_menu()
while True:
        choice = input("Choice: ").strip().lower()

        if choice == "1":
            show_summary()

        elif choice == "2":
            keyword = input("Keyword: ")
            search(keyword)

        elif choice == "3":
            ip = input("IP: ").strip()
            ip_report(ip)

        elif choice == "4":
            show_masked()

        elif choice == "q":
            print("Bye.")
            break

        else:
            print("Unknown choice.")
             


    

    


   









