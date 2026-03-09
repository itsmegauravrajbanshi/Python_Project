board = [['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   ']]
def display_board(board):
    print('---+---+---')
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('---+---+---')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('---+---+---')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])
    print('---+---+---')

def get_move():
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2) "))
    return row, col

print("Welcome to Tic Tac Toe!")
display_board(board)
player = ' X '
while True: 
    print (f"Player {player}'s turn")
    row, col = get_move()
    if row >= 0 and row <= 2 and col >= 0 and col <= 2 and board[row][col] == '   ':
        board[row][col] = player
        display_board(board)
        
        if board[0][0] == board[0][1] == board[0][2] != '   ' and board[0][0] == player\
        or board[1][0] == board[1][1] == board[1][2] != '   ' and board[1][0] == player\
        or board[2][0] == board[2][1] == board[2][2] != '   ' and board[2][0] == player\
        or board[0][0] == board[1][0] == board[2][0] != '   ' and board[0][0] == player\
        or board[0][1] == board[1][1] == board[2][1] != '   ' and board[0][1] == player\
        or board[0][2] == board[1][2] == board[2][2] != '   ' and board[0][2] == player\
        or board[0][0] == board[1][1] == board[2][2] != '   ' and board[0][0] == player\
        or board[0][2] == board[1][1] == board[2][0] != '   ' and board[0][2] == player:
            print(f"{player} wins!")
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
    