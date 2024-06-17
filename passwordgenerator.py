import random
import string
def generate_password(length,numbers=True,special_char=True):
    letter = string.ascii_letters
    digit = string.digits
    special = string.punctuation
    characters = letter
    if numbers:
        characters += digit
    if special_char:
        characters += special
    pwd = ""
    meets_criteria =  False
    has_number = False
    has_special =  False
    while not meets_criteria or len(pwd)<length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digit:
            has_number = True
        elif new_char in special:
            has_special = True
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special
    return pwd
length = int(input("Enter a maximum length of password:"))
has_number = input("Do you want a numbers(y/n)?:").lower() == "y"
has_special = input("Do you want a special characters(y/n)?:").lower() == "y"
password = generate_password(length,has_number,has_special)
print("The generated password is :",password)
