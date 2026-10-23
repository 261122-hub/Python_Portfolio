# fix_the_rules.py
 # This program checks a connection against three rules.

role = input("Role: ")

# (semantic)  int() كرقم فلازم احط  port  احنا بدنا 
port = int(input("Port: "))

# (semantic) فلازم احط كمان يساوي عشان يصير سؤال هل تساوي admin  هو راح يشتغل الكود تمام بس القيمة مسندة ل 
is_admin = role =="admin"

# (syntax)  لازم اشارة الاصغر تيجي قبل ال يساوي 
is_system_port = port <= 1023

is_web_port = port == 80 or 443

print(f"Admin: {is_admin}")

print(f"System port: {is_system_port}")

print(f"Web port: {is_web_port}")