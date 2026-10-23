MAX_FAILED = 5

role = input("role: ")
mfa_passed = input("MFA passed (yes/no) : ")
Failed_attempts = int(input("Failed attempts : "))

mfa_ok = mfa_passed == "yes"

#  true بكون الجواب  (admin او root)  اذا احد الاجوبة بكون
is_privileged = role == "admin" or role == "root"

can_log_in = mfa_ok and Failed_attempts < MAX_FAILED

print(f"MFA OK: {mfa_ok}  Can log in: {can_log_in}  Privileged role: {is_privileged}")
