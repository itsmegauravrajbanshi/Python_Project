# Guess the number game
import random

def fun():
    pass

if __name__ == "__main__":
    print ("Welcome to the Guess the Number Game!")
    min_value = input("Enter the minimum value: ")
    max_value = input("Enter the maximum value: ")
    guessed_number = random.randint(int(min_value), int(max_value))
    count = 1
    life = 3
    while True and life > 0:
        try:
            number = int(input(f"Guess a number between {min_value} and {max_value}: "))
            if number < guessed_number:
                print("Too low! Try again.")
            elif number > guessed_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {count} attempts.")
                print(f"Best Score: {life}")
                # print("Congratulations! You guessed the number in {} attempts.".format(count + 1))
                break
            count += 1
            life -= 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    if life == 0:
        print("The correct number was: ", guessed_number)