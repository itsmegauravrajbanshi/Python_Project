import random

def valid_digits(lst, guess_digits, number_of_digit):
    digits = len(guess_digits)  
    if digits != number_of_digit:
        print(f"{number_of_digit}-digits required !!!.")
        return False
    for digit in guess_digits:
        if digit in lst:
            print("Digit should not be repeated!!!")
            lst.clear()
            return False
        lst.append(digit)
    return True

def start_game():
    cows_counts = 0
    bulls_counts = 0
    lst = []
    while True:
        number_of_digit = int(input("How many digits? : "))
        if 1 < number_of_digit < 10:
            break
        else:
            print("Valid only between (2-9) digits!")
            continue 
    system_number = random.sample(range(10),number_of_digit)
    print(system_number)
    print(f"I have generate a {number_of_digit}-digits number try to guess it!")
    life = 5
    while life > 0:
        guess_digits = input(f"\nGuess {number_of_digit}-digits : ")
        is_valid = valid_digits(lst, guess_digits, number_of_digit)
        if not is_valid:
            continue
        else:
            for index in range(len(system_number)):
                if int(guess_digits[index]) in system_number:
                    if int(guess_digits[index]) == system_number[index]:
                        bulls_counts += 1
                        continue
                    cows_counts += 1
            print(f"{cows_counts} cows, {bulls_counts} bulls")
            if bulls_counts == number_of_digit:
                print(f"Congratulation !!! You won !")
                return
        cows_counts = 0
        bulls_counts = 0
        lst.clear()
        life -= 1
        print(f"Remains {life} attemps. ")
        if life == 0:
            print("-"*25)
            print("***Game over!***") 
    
if __name__ == "__main__":
    print("Starting game...")
    while True:
        start_game()
        play_again = input("\nPlay again? (y/n) :")
        if play_again.upper() == "N":
            break