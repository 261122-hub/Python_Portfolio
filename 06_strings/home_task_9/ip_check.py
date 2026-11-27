# ip_check.py 
# This script checks if the given IP address is valid and whether it is a public or private IP address.

def is_valid_part(part): 
    """Check if a part of the IP address is valid (0-255)."""
    return part.isdecimal() and  0 <= int(part) <= 255
        
    

def ip_problem(address): 
    """Check if the given IP address is valid and whether it is public or private."""
    
    if address.count(".") != 3:
        return "Invalid: it needs exactly 3 dots."
    parts = address.split('.')

    for part in parts:
        if part == "":
            return "Invalid: a part is empty."

        if not is_valid_part(part): 
         return f"Invalid: {part} Is Not a number From 0 to 255."
    
    return ""

address = input("IPv4 address: ").strip()
problem = ip_problem(address)

if problem:
        print(problem)
else:
        print(f"{address} is valid.")









        
        


    