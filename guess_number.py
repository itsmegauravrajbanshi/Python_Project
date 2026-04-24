# Guess the number game
import random

def player_vs_computer(*args):
    count = 0
    min_value = args[0]
    max_value = args[1]

    my_guess = int(input("My guess number: "))
    computer_guess = int(random.randint(int(min_value), int(max_value)))
    # print("-"*35)
    # print("My guess number : ", my_guess)
    # # print("Computer guess number : ", computer_guess)
    print("-"*35)
    print("Let's start the game...")
    count = 0
    while True:
        count +=1
        try:
            player_guess = int(input(f"Your Guess : "))
            if player_guess < computer_guess:
                print("Too low!")
            elif player_guess > computer_guess:
                print("Too High!")
            else:
                print("Correct Guess : ", player_guess)
                print("-"*40)    
                print(f"Congratulations! You Won, guessed in {count} attempts.")
                break
            
            com_guess = int(random.randint(int(min_value), int(max_value)))
            print(f"System Guess : {com_guess}")
            if com_guess < my_guess:
                print("Too low! ")
                min_value = com_guess+1
            elif com_guess > my_guess:
                print("Too High! ", com_guess)
                max_value = com_guess-1
            else:
                print("Correct Guess : ", com_guess)
                print("-"*40)
                print(f"Congratulations! Computer Won, guessed in {count} attempts.")
                break
            print("-"*40)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")        

def computer_player(*args):
    count = 0
    min_value = args[0]
    max_value = args[1]
    guess_number = args[2]
    lives = args[3]
    while lives > 0:
        system_guess_number = random.randint(int(min_value), int(max_value))
        count += 1
        if system_guess_number < guess_number:
            print("Too low! ", system_guess_number)
            min_value = system_guess_number+1
        elif system_guess_number > guess_number:
            print("Too High! ", system_guess_number)
            max_value = system_guess_number-1
        else:
            print("Correct Guess : ", system_guess_number)
            print(f"Congratulations! System guessed the number in {count} attempts.")
            break
        lives -= 1
        if lives == 0:
            print("***Game Over***")
            print("Correct Guess is: ", guess_number)
    
def single_player(min_value : int, max_value : int, guess_number, lives) -> None:
    count = 0
    while lives > 0:
        try:
            my_guess = int(input(f"Guess a number between {min_value} and {max_value}: "))
            count += 1
            if my_guess < guess_number:
                print("Too low!")
            elif my_guess > guess_number:
                print("Too high!")
            else:
                print("Correct Guess : ", my_guess)
                print(f"Congratulations! You guessed the number in {count} attempts.")
                break
            lives -= 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    if lives == 0:
        print("***Game Over***")
        print("Correct Guess is: ", guess_number)

def game_play():
    lives = 5
    while True:
        try:
            min_value, max_value = map(str, input("Enter min, max value: ").split())
            if min_value.isdigit() and max_value.isdigit():
                # print(type(min_value),min_value, type(max_value), max_value)
                guess_number = random.randint(int(min_value), int(max_value))
                break
        except ValueError as error:
            print("Invalid input! Note: Keep space after number you enter! example: 10 100 ")
            continue
    return min_value, max_value, guess_number, lives

if __name__ == "__main__":
    
    print("*** Welcome to 'Guess the Number' Game ***")
    print("    1. Single Player")
    print("    2. Computer Player")
    print("    3. Player vs Computer")
    print("********************************************")
    select = input("Choose 1-3: ")
    min_value, max_value, guess_number, lives = game_play()
    if select == '1':
        single_player(min_value, max_value, guess_number, lives)
    elif select == '2':
        computer_player(min_value, max_value, guess_number, lives)
    elif select == '3':
        player_vs_computer(min_value, max_value)
    else:
        print("Invalid Input!!")
    
    
