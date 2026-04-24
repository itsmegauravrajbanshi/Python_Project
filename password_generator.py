import random
import string
import secrets

all_characters= string.ascii_letters + string.digits + string.punctuation
file_name = "save_password.txt"

length = int(input("Enter password length: "))
isUppercase = input("Include uppercase letters? (y/n): ")
isNumber = input("Include numbers? (y/n): ")
isSpecial = input("Include special characters? (y/n): ")

password_list = []
number_of_password = int(input("How many password? : "))
for i in range(number_of_password):
    while True:
        password = "".join(secrets.choice(all_characters) for _ in range(length))
        if isUppercase == isNumber == isSpecial == "y":
            if (any(c.islower() for c in password) \
                and any(c.isupper() for c in password) \
                and any(c.isdigit() for c in password) \
                and any(c in string.punctuation for c in password)):
                print(password)
                break
        elif isUppercase == isNumber == "y":
            if (any(c.isupper() for c in password) \
                and any(c.isdigit() for c in password)\
                and not any(c in string.punctuation for c in password)):
                print(password)
                break
        elif isUppercase == isSpecial == "y":
            if (any(c.isupper() for c in password) \
                and not any(c.isdigit() for c in password)\
                and any(c in string.punctuation for c in password)):
                print(password)
                break
        elif isNumber == isSpecial == "y":
            if (any(c.isdigit() for c in password) \
                and not any(c.isupper() for c in password) \
                and any(c in string.punctuation for c in password)):
                print(password)
                break
        elif isUppercase == "y":
            if (not any(c.isdigit() for c in password) \
                and any(c.isupper() for c in password) \
                and not any(c in string.punctuation for c in password)):
                print(password)
                break
        elif isNumber == "y":
            if (any(c.isdigit() for c in password) \
                and not any(c.isupper() for c in password) \
                and not any(c in string.punctuation for c in password)):
                print(password)
                break
        elif isSpecial == "y":
            if (not any(c.isdigit() for c in password) \
                and not any(c.isupper() for c in password) \
                and any(c in string.punctuation for c in password)):
                print(password)
                break
        else:
            password = "".join(secrets.choice(string.ascii_lowercase) for _ in range(length))
            print(password)
            break
    password_list.append(password)

save_file = input("Want to save the password in text file? (y/n) : ")
if save_file == 'y':
    file_name = input("Enter file name: ")
    with open(file_name, 'a') as file:
        file.writelines(line+"\n" for line in password_list)

            


    
    
     
    # elif isNumber == "y" and isUppercase == "y":
    #     if (any(c.isupper() for c in password) \
    #         and any(c.isdigit() for c in password)):
    #         print(password)
    #         break
        
    # else:
    #     password = "".join(secrets.choice(string.ascii_lowercase) for _ in range(length))
    #     print(password)
    #     break