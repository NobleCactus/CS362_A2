# Andrew Eppinger
# CS362 Software Engineering II - Spring 2021
# A2: TDD Hands On - Check password code

def check_pwd(password):
    lowercase_letter_present = 0
    if len(password) < 8:
        return False
    if len(password) > 20:
        return False
    for char in password:
        if char.islower():
            lowercase_letter_present = 1
    if lowercase_letter_present == 0:
        return False
    return True
