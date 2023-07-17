import random
import string
def get_random_password(length=8):  # it genarates the password with the length 8 if no arguments will given
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
password = get_random_password ()
print(password)
