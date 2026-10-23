MAX_FAILED = 5

role = input("role: ")
mfa_passed = input("MFA passed (yes/no) : ")
Failed_attempts = int(input("Failed attempts : "))

mfa_ok = mfa_passed == "yes"

# If one of the answers is 'admin' or 'root', then it is 'true'.
is_privileged = role == "admin" or role == "root"

can_log_in = mfa_ok and Failed_attempts < MAX_FAILED

print(f"MFA OK: {mfa_ok}  Can log in: {can_log_in}  Privileged role: {is_privileged}")
