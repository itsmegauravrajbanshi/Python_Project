
X = " X  |"
O = " O  |"

def game_board(size : int) -> list:
    board = [[" -  |" for _ in range(size)] for _ in range(size)]
    return board

def display_board(board):
    print()
    print("   | ",*[f"{i+1}  | " for i in range(len(board))])
    print("---+"+"-----+"*len(board)+"---")
    for index, i in enumerate(board):
        print(f" {index+1} |",*i)
        if index == len(board)-1:
            break
        print("---+"+"-----+"*len(board)+"---")
    print()

def diagonal_win(size: int, board : list) -> tuple:
    count_x = count_o = 0
    for row in range(size):
        for col in range(size):
            # print(f"[{row}{col}]{board[row][col]}", end=" ")
            if row == col :
                # print(f"\n[{row}{col}]{board[row][col]}", end=" ")
                if board[row][col] == X:
                    count_x+=1
                if board[row][col] == O:
                    count_o+=1
        
        if count_x == size:
            return (True, X)
        
        if count_o == size:
            return (True, O)
    
    return (False, None)

def anti_diagonal_win(size : int, board : list) -> tuple:
    count_x = count_o = 0
    for row in range(size):
        for col in range(size):
            # print(f"[{row}{col}]{board[row][col]}", end=" ")
            if col == (size-1) - row :
                # print(f"\n[{row}{col}]{board[row][col]}", end=" ")
                if board[row][col] == X:
                    count_x+=1
                if board[row][col] == O:
                    count_o+=1
        if count_x == size:
            return (True, X)
        
        if count_o == size:
            return (True, O)
    
    return (False, None)
    
#horizontal win
def horizontal_win(size: int, board : list) -> tuple:
    for row in range(size   ):
        count_x = count_o = 0
        for col in range(size):
            # print(f"[{row}{col}]{board[row][col]}", end=" ")
            if row == row :
                if board[row][col] == X:
                    count_x += 1
                if board[row][col] == O:
                    count_o += 1 
        if count_x == size:
            return (True, X)
        
        if count_o == size:
            return (True, O)
    
    return (False, None)
        
# vertical wins
def vertical_win(size : int, board : list)  -> tuple :
    for row in range(size):
        count_x = count_o = 0
        for col in range(size):
            # print(f"[{row}{col}]{board[row][col]}",end=" ")
            if row == row:
                if board[col][row] == X:
                    count_x += 1
                if board[col][row] == O:
                    count_o += 1
        if count_x == size:
            return (True, X)
        
        if count_o == size:
            return (True, O)
    return (False, None)

def play_game(board_size : int, board : list) -> None:
    mark = O
    no_of_turn = 0
    row, col = 0, 0
    
    display_board(board)
    while True:
        print(f"Player '{mark[1]}' turn")
        try:
            str_row, str_col = map(str, input("Enter row, col ('qq' for exit): "))
            
            if str_row == 'q' or str_col =='q':
                return True
            row = int(str_row)-1 
            col = int(str_col)-1
            
            if row > board_size-1 or col > board_size-1 or row < 0 or col < 0:
                print("-"*40) 
                print("Error Message : Invalid row or col!\n")
                continue 
            
            if board[row][col] == X or board[row][col] == O:
                print("-"*40)
                print(f"Error Message : Not allowed! Already Exist '{board[row][col][1]}'\n")
                continue
        
        except ValueError as error:
            print(f"Error Message : {error}")
            continue

        board[row][col] = mark        
        
        mark = X if mark == O else O
            
        display_board(board)
        no_of_turn +=1
        if no_of_turn == board_size * board_size:
            display_board(board)
            print("!!! Match Draw !!!")
            print("!!! Try Again !!!")
            break

        if no_of_turn >= board_size:
            
            win, player = horizontal_win(board_size, board)
            if win:
                print(f"Player '{player[1]}' win by Horizontal line!" )
                print("!!! Thank you for Playing !!!")
                break

            win, player = vertical_win(board_size, board)
            if win:
                print(f"Player '{player[1]}' win by Vertical line!" )
                print("!!! Thank you for Playing !!!")
                break
            
            win, player = diagonal_win(board_size, board)
            if win:
                print(f"Player '{player[1]}' win by Diagonal line!" )
                print("!!! Thank you for Playing !!!")
                break
            
            win, player = anti_diagonal_win(board_size, board)
            if win:
                print(f"Player '{player[1]}' win by Anit-Diagonal line!" )
                print("!!! Thank you for Playing !!!")
                break
        print(f"-> {no_of_turn} Move\n")

if __name__ == "__main__":
    board_size = int(input("Enter size (n x n) : "))
    if 0 < board_size < 10:
        board = game_board(board_size)
        while True:
            game_over = play_game(board_size, board)
            if game_over:
                print("\n!!! Thank you for Playing !!!\n")
                break
            print()
            play_again = input("Play Again (y/n) : ")
            board = game_board(board_size)
            if play_again == 'n':
                break
    else:
        print("!!! Invalid board size !!!")