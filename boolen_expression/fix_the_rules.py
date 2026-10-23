# fix_the_rules.py
 # This program checks a connection against three rules.

role = input("Role: ")

# (semantic) int() as a number, so we need to put a port.
port = int(input("Port: "))
# (semantic) So I also need to add an equals sign to make it a question: Is it equal to admin? The code will work fine, but the value is assigned to
is_admin = role =="admin"

# (syntax) The "less than" symbol must come before the equals sign.
is_system_port = port <= 1023

is_web_port = port == 80 or 443

print(f"Admin: {is_admin}")

print(f"System port: {is_system_port}")

print(f"Web port: {is_web_port}")