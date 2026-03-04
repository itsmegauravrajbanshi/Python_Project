import random

if __name__ == "__main__":
    ROCK = "r"
    PAPER = "p"
    SCISSORS = "s"

    print("Welcome to the Rock, Paper, Scissors Game!")
    choices = [ROCK, PAPER, SCISSORS]
    life = 3
    counter = 0
    while True and life > 0:
        your_choice = input("Enter your choice (r, p, s): ").lower()
        computer_choice = random.choice(choices)

        if your_choice not in choices:
            print("Invalid choice. Please enter r, p, or s.")
            continue
        elif your_choice == computer_choice:
            print(f"Both you and the computer chose {your_choice}. It's a tie!")
            counter -= 1
        elif (your_choice == "ROCK" and computer_choice == "SCISSORS") or\
                (your_choice == "PAPER" and computer_choice == "ROCK") or\
                (your_choice == "SCISSORS" and computer_choice == "PAPER"):
            print(f"You chose {your_choice} and the computer chose {computer_choice}. You win!")
            counter += 1
        else:
            print(f"You chose {your_choice} and the computer chose {computer_choice}. You lose!")
        life -= 1
        if life > 0:
            continue
        yes_no = input("Press ANY KEY to continue or 'n' to quit: ").lower()
        if yes_no == 'n':
            print("Thanks for playing. Goodbye!")
            break
        counter = 0
        life = 3