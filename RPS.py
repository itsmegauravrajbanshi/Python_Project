import random

if __name__ == "__main__":
    ROCK = "r"
    PAPER = "p"
    SCISSORS = "s"

    print("Welcome to the Rock, Paper, Scissors Game!")
    choices = [ROCK, PAPER, SCISSORS]
    life = 3
    won = loss = tie = 0
    total_win = total_loss = total_tie = 0
    total_rounds = 1
    print("\n")
    while True and life > 0:
        your_choice = input("Enter your choice (r, p, s): ").lower()
        
        computer_choice = random.choice(choices)

        if your_choice not in choices:
            print("Invalid choice. Please enter r/p/s.")
            continue

        elif your_choice == computer_choice:
            print("It's a tie!")
            tie += 1
            
        elif (your_choice == ROCK and computer_choice == SCISSORS) or\
                (your_choice == PAPER and computer_choice == ROCK) or\
                (your_choice == SCISSORS and computer_choice == PAPER):
            print("You win!")
            won += 1
        else:
            print("You lose!")
            loss += 1
        life -= 1
        if life > 0:
            continue
        if won >= 2:
            print(f"{total_rounds} round You won. Well done!")
            total_win += 1
        elif loss >= 2:
            print(f"{total_rounds} round You lost. Better luck next time!")
            total_loss += 1
        else:
            print(f"{total_rounds} round It's a tie. Try again!")
            total_tie += 1
        # total_loss += loss
        # total_win += won
        # total_tie += tie
        yes_no = input("Press ANY KEY to continue or 'n' to quit: ").lower()
        if yes_no == 'n':
            print("Thanks for playing. Goodbye!")
            print(f"Total wins: {total_win}")
            print(f"Total losses: {total_loss}")
            print(f"Total ties: {total_tie}")
            print(f"Total rounds: {total_rounds}")
            break
        total_rounds += 1
        counter = 0
        life = 3
        won = 0
        loss = 0
        tie = 0