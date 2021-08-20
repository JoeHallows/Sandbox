MINIMUM_LENGTH = 6

password = input("Add password: ")
if len(password) < MINIMUM_LENGTH:
    print("Invalid password!")
    password = input("Add password: ")
for i in password:
    print("*", end="")