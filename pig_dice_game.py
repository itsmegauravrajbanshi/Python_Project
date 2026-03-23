import random

def game_play(player, points, target_points):
    while True:
            print(f"Player {player}'s turn")
            roll_dice = random.randint(1,6)
            print(f"You rolled a {roll_dice}")      
            if roll_dice == 1:
                points = 0
                break
            points += roll_dice
            print("points.. ",points)
            
            if points >= target_points:
                return True
            roll_again = input("Roll again? (y/n): ")
            if roll_again.upper() == 'Y': 
                continue
            else:
                break
def show_score(points, score_board):
    print(f"\nYou scored {points} points this turn.")
    print(f"Current scores:",end=" ")
    for i in range(len(score_board)):
        if i == len(score_board)-1:
            print(f"Player {i+1}: {score_board[i]} ", end="")
            break
        print(f"Player {i+1}: {score_board[i]}, ", end="")

def start_game(number_of_player, target_points):
    print("\nGame Starting...")
    n = number_of_player
    score_board = [0] * n    
    points = 0

    for player in range(1, n+1): 
        is_winner = game_play(player, points, target_points)
        if is_winner:
            print(f"\nPlayer {player} is winner.")
            return
        show_score(points, score_board)
        print("\n")
    print("Draw!!!")

if __name__ == "__main__":
    print("Enter '0' for exit.")
    while True:
        try:
            number_of_player = int(input("Number of Player? "))
            target_points = int(input("Set winning target? "))
            if 0 == number_of_player or 0 == target_points  :
                break
            elif 0 > number_of_player:
                print("Please Only enter positve integer value.")
            elif 5 < number_of_player:
                print("Only 5 player allowed!!!")
            elif 10 <= target_points <=50:
                start_game(number_of_player, target_points)
                try_again = input("\nDo you want to play Again? (y/n): ")
                if try_again.upper() == "Y":
                    continue
                break
            else:
                print("Invalid target!!!\n Only allowed (10-50).")
        except ValueError:
            print("Please enter number only!!!")
    