user = "analyst"
role = "viewer"
failed = 3
port = 22 

# true 
print("\ntest1 : i predict true")
print(user != "admin")
print("\ntest2 : i predict true")
print(role == "viewer")
print("\ntest3 : i predict true")
print(failed < 5)
print("\ntest4 : i predict true")
print(port == 22 and port > 15)
print("\ntest5 : i predict true")
print(failed <= 4 or role == "viewer")

# false
print("\ntest6 : i predict false")
print(user == "admin")
print("\ntest7: i predict false")
print(user != "analyst")
print("\ntest8: i predict false")
print(role == "admin")
print("\ntest9 : i predict false")
print(failed >= 5 or port < 15)
print("\ntest10 : i predict false")
print(not (port == 22))
