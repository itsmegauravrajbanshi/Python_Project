from ast import Constant
import random
round = total_win = total_tie = total_loss = 0

def get_choice():
    your_choice = input("-> Enter your choice (R, P, S): ").lower()
    computer_choice = random.choice(choices)
    return your_choice, computer_choice

def display_score(life, win, loss, tie)-> bool:
    global round, total_win, total_loss, total_tie
    if life == 3:
        round += 1
        if win >= 2:
            score(win, loss, tie)
            print("Congratulations! You won the round!")
            total_win += 1
        elif loss >= 2:
            score(win, loss, tie)
            print("Sorry! You lost the round!")
            total_loss += 1
        else:
            score(win, loss, tie)
            print("It's a tie round!")
            total_tie += 1
        # print(f"Total Wins: {total_win}, Losses: {total_loss}, Total tie: {total_tie}")
        should_continue = input("Press 'any key' to Play Again or 'q' to quit/total score: ").lower()
        if should_continue == 'q':
            print(f"-------------Total {round} Round Score------------")
            print(f"Total Wins: {total_win}, Losses: {total_loss}, Total tie: {total_tie}")
            print ("------------------------------------")
            print("Thanks for playing! Goodbye!")
            return
        return True
    
def score(win, loss, tie):
    print(f"---------{round} Round Score--------")
    print(f"Wins: {win}, Losses: {loss}, Ties: {tie}")
    print(f"--------------------------------")

def play_game()-> None:
    life = win = loss = tie = 0
    while True and life < 3:
        your_choice, computer_choice = get_choice()

        if your_choice not in choices:
            print("Invalid choice. Please enter R/P/S.")
            continue

        elif your_choice == computer_choice:
            print("It's a tie!")
            tie += 1
        elif (your_choice == ROCK and computer_choice == SCISSORS) or\
                (your_choice == PAPER and computer_choice == ROCK) or\
                (your_choice == SCISSORS and computer_choice == PAPER):
            print("You win!")
            win += 1
        else:
            print("You lose!")
            loss += 1
        life += 1
        reset_counter = display_score(life, win, loss, tie)
        if reset_counter:
            life = win = loss = tie = 0
            
        
if __name__ == "__main__":
    ROCK : Constant = "r"
    PAPER : Constant = "p"
    SCISSORS : Constant = "s"
    choices = [ROCK, PAPER, SCISSORS]
    print("Welcome to the Rock, Paper, Scissors Game!")
    play_game()
    
    
        

        