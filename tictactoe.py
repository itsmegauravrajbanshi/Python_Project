board = [['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   ']]
def reset_board():
    for row in range(3):
        for col in range(3):
            board[row][col] = '   '
def display_board(board):
    print('---+---+---')
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('---+---+---')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('---+---+---')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])
    print('---+---+---')

def get_move():
    try:
        row, col = map(int, input("Enter the row, column (0-2): ").split())
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")
        return get_move()
    return row, col

print("Welcome to Tic Tac Toe!")
player = ' X '
count_X = 0
count_O = 0
while True: 
    print (f"Player {player}'s turn")
    row, col = get_move()
    if row >= 0 and row <= 2 and col >= 0 and col <= 2 and board[row][col] == '   ':
        board[row][col] = player
        display_board(board)
        
        if board[0][0] == board[0][1] == board[0][2] == player\
        or board[1][0] == board[1][1] == board[1][2] == player\
        or board[2][0] == board[2][1] == board[2][2] == player\
        or board[0][0] == board[1][0] == board[2][0] == player\
        or board[0][1] == board[1][1] == board[2][1] == player\
        or board[0][2] == board[1][2] == board[2][2] == player\
        or board[0][0] == board[1][1] == board[2][2] == player\
        or board[0][2] == board[1][1] == board[2][0] == player:
            print(f"{player} wins!")
            if player == ' X ':
                count_X += 1
            else:
                count_O += 1
            continue_game = input("Do you want to play again? (y/n): ")
            if continue_game.lower() == 'y':
                reset_board()
                continue
            break
        # elif all(board[row][col] != '   ' for row in range(3) for col in range(3)):
        #     print("It's a draw!")
        elif board[0][0] != '   ' and board[0][1] != '   ' and board[0][2] != '   ' and \
             board[1][0] != '   ' and board[1][1] != '   ' and board[1][2] != '   ' and \
             board[2][0] != '   ' and board[2][1] != '   ' and board[2][2] != '   ':
            print("It's a draw!")
            break
        if player == ' X ':
            player = ' O '
        else:
            player = ' X '
    else:
        print("Invalid move.")
print(f"Final score: Player X wins: {count_X}, Player O wins: {count_O}")