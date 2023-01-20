# Name: Aiden Teal
# SID: 1724406
# CCID: ateal
# AnonID: 1000332190
# CMPUT274, Fall 2022 - Winter 2023
#
# Weekly Assignment #1: Password Validator
#


def validate(password):
    # The validate function takes an input(password) and checks various
    # conditions including capitals, lowercases, special characters,
    # and spaces to see if the password is secure, insecure,
    # or invalid. Depending on the password, it will display
    # one of the three outputs "Invalid", "Valid", or "Secure".
    characters = password[0:len(password)]
    specials = "!-$%&'()*+,./:;<=>?_[]^`{|}~"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    I = 0
    S = 0
    IS = 0

    for characters in password:
        if len(password) < 8 or characters == " " or characters == "@" \
             or characters == "#":
             I += 1 

        elif characters.isdigit() and any(characters in specials for characters 
        in password) and any(characters in capital_letters for characters in password) \
            and any(characters in lowercase_letters for characters in password):
            S += 1         

        else:
            IS += 1
    
    if I >= 1:
        return "Invalid"
    elif S >= 1:
        return "Secure"
    elif IS >= 1:
        return "Insecure"

    pass 

def generate(n):
    # The function generate() takes an input n and generates a secure
    # password of length n. Uses various techniques including random
    # selection and the shuffle function to pseudo randomize the password.
    import random
    from random import randint
    i = 0
    specials = "!-$%&'()*+,./:;<=>?_[]^`{|}~"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    secure_password = ""

    if n < 8:
        n = 8

    while i < n:
         secure_password = secure_password + specials[randint(0,len(specials) - 1)] \
            + capital_letters[randint(0,len(capital_letters) - 1)] \
                 + lowercase_letters[randint(0,len(lowercase_letters) - 1)] \
                    + str(randint(0,9))
         i += 4

    if i == n:
        secure_password = list(secure_password)
        random.shuffle(secure_password)
        secure_password = ''.join(secure_password)
        return "Your secure password is: " + secure_password

    elif i == n + 1:
        secure_password = list(secure_password)
        del secure_password[randint(0, len(secure_password) - 1)]
        random.shuffle(secure_password)
        secure_password = ''.join(secure_password)
        return "Your secure password is: " + secure_password

    elif i == n + 2:
         secure_password = list(secure_password)
         del secure_password[randint(0, len(secure_password) - 1)]
         del secure_password[randint(0, len(secure_password) - 1)]
         random.shuffle(secure_password)
         secure_password = ''.join(secure_password)
         return "Your secure password is: " + secure_password
    
    elif i == n + 3:
         secure_password = list(secure_password)
         del secure_password[randint(0, len(secure_password) - 1)]
         del secure_password[randint(0, len(secure_password) - 1)]
         del secure_password[randint(0, len(secure_password) - 1)]
         random.shuffle(secure_password)
         secure_password = ''.join(secure_password)
         return "Your secure password is: " + secure_password


pass

if __name__ == "__main__":
   pass
