# username_policy.py
# This program checks if a username follows the required rules and policy.


MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    return username.strip().lower()


def bad_character(username):
    for char in username:
        if not (char.isalnum() or char == "_"):
            return char
    return ""


def policy_problem(username):
    if not MIN_LENGTH <= len(username) <= MAX_LENGTH:
        return "length must be 3 to 12."

    if not username[0].isalpha():
        return "it must start with a letter."

    bad = bad_character(username)

    if bad:
        return f"the character {bad} is not allowed."

    return ""



username = input("New username: ")
username = clean(username)

problem = policy_problem(username)

if problem:
    print(f"Rejected [{username}]: {problem}")
else:
    print(f"Accepted [{username}].")





