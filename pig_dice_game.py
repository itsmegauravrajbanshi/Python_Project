import random

def game_play(player, points,game_score, target_points):
    while True:
        print(f"\nPlayer {player+1}'s turn")
        roll_dice = random.randint(1,6)
        print(f"You rolled a {roll_dice}")      
        
        if roll_dice == 1:
            input("!!! Turn Over !!! \nPress 'ENTER' to continue...")
            points = 0
            break

        points += roll_dice
        game_score[player] = points
        
        if points >= target_points:
            print(f"\nWinner : Player {player+1}")
            return True, player, show_score(points, game_score)
    
        roll_again = input("Roll again? (y/n): ")
        if roll_again.upper() == 'Y': 
            continue
        else:
            break
    player = -1
    return False, player, show_score(points, game_score)

def show_score(points, game_score):
    print("-"*41)
    print(f"You scored {points} points this turn.")
    print(f"Current scores:",end=" ")
    for i in range(len(game_score)):
        if i == len(game_score)-1:
            print(f"Player {i+1}: {game_score[i]} ", end="")
            break
        print(f"Player {i+1}: {game_score[i]}, ", end="")
    print()
    print("-"*41)
    return game_score

def show_score_history(score_history):
    # flat = [item for sublist in score_history for item in sublist]
    for index, item in enumerate(score_history):
        print(f"### Round {index+1} ###")
        for i, score in enumerate(item[1]):
            print(f"Player {i+1} score : {score} points")
        if item[0] >= 0:
            print(f"### Player {item[0]+1} won ###")
        else: 
            print("### Draw ###")
        print("-"*41)
            
def start_game(number_of_player, target_points, score_history):
    print("\nGame Starting...")   
    game_score = [0] * number_of_player
    points = 0
    for player in range(0, number_of_player):
        win_result, win_player, game_score = game_play(player, points, game_score, target_points)
        if win_result:
            break
    score_history.append([win_player, game_score])
    
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
                exit = None
                score_history = []
                while True:
                    start_game(number_of_player, target_points, score_history)
                    # print("-"*41)
                    is_exit = input("Press 'P' Play Again next round.\nPress 'H' Score history.\nPress 'Any key' to Exit.")
                    if is_exit.upper() == "P":
                        continue
                    elif is_exit.upper() == 'H':
                        print()
                        print("-"*13+" Score History "+"-"*13)
                        show_score_history(score_history)
                        if "B" == input("Press 'b' for Back to Game or 'Enter' for exit: ").upper():
                            continue
                        else:
                            exit = True
                            break
                    else:
                        exit = True
                        break
                if exit:
                    break
            else:
                print("Invalid target!!!\n Only allowed (10-50).")
        except ValueError:
            print("Please enter number only!!!")
    