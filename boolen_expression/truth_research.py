# The file : truth_research.py 
# This program tests logical values ​​and logical operations, and prints the results.
# Source : https://docs.python.org/3/builtins/stdtypes.html

# Expectations : 
# bool("") ----> false, because the value is empty.
# bool("0") ----> true, because the string is not empty and contains the character '0'.
# bool(0) ----> false, because the value is zero.
# bool(0.0) ----> false, because the value is zero (even though it is a float).
# bool("False") ----> true, because the string is not empty and contains text.

print(bool(""))
print(bool("0"))
print(bool(0))
print(bool(0.0))
print(bool("False"))