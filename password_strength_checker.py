import string

password = input("Enter the password: ")
password_length = len(password)

upper_alpha = any([1 if char in string.ascii_uppercase else 0 for char in password])
lower_alpha = any([1 if char in string.ascii_lowercase else 0 for char in password])
other = any([1 if char in string.punctuation else 0 for char in password ])
digit = any([1 if char in string.digits else 0 for char in password])

character = [upper_alpha, lower_alpha, other, digit]
strength = 0        

if sum(character) > 1:
    strength +=1 
if sum(character) > 2:
    strength +=1
if sum(character) > 3:
    strength +=1

if password_length >= 6:
    strength += 1
if password_length >= 8:
    strength += 1
if password_length >= 12:
    strength += 1

print(strength)
if strength < 4:
    print("Weak Password")
elif strength == 4:
    print("Medium Password")
elif 4 < strength < 6:
    print("Strong Password")
else:
    print("Very Strong Password")

