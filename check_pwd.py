# Andrew Eppinger
# CS362 Software Engineering II - Spring 2021
# A2: TDD Hands On - Check password code

def check_pwd(password):
    if len(password) < 8:
        return False
    if len(password) > 20:
        return False
    return True

st = "HhjroOhjdsfRkdfhSkjergE"
