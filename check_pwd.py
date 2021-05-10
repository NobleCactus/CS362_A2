# Andrew Eppinger
# CS362 Software Engineering II - Spring 2021
# A2: TDD Hands On - Check password code

def check_pwd(password):
    lowercase_letter_present = 0
    uppercase_letter_present = 0
    number_present = 0
    special_char_present = 0
    special_chars = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
                     '(', ')', '_', '+', '-', '=']
    if len(password) < 8:
        return False
    if len(password) > 20:
        return False
    for char in password:
        if char.islower():
            lowercase_letter_present = 1
        elif char.isupper():
            uppercase_letter_present = 1
        elif char.isdigit():
            number_present = 1
        elif char in special_chars:
            special_char_present = 1
    if lowercase_letter_present == 0 or uppercase_letter_present == 0 \
            or number_present == 0 or special_char_present == 0:
        return False
    return True
