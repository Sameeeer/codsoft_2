def initialize_board():
    return [' '] * 9
#board
def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

#winning combinations
def winner(board, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]           
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

#checking if board is full
def board_full(board):
    return all(cell != ' ' for cell in board)

#apply minimax algorithm
def minimax(board, depth, maximizing_player):
    if winner(board, 'X'):
        return 1
    if winner(board, 'O'):
        return -1
    if board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = -1
    best_eval = float('-inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move
#game function
def play_game():
    board = initialize_board()
    display_board(board)
       
    while True:
        move = int(input("Enter your move (0-8): "))
        if board[move] == ' ':
            board[move] = 'O'
        else:
            print("Invalid move! Cell is already occupied.")
            continue
        
        display_board(board)
        
        if winner(board, 'O'):
            print("You win!")
            break
        if board_full(board):
            print("It's a tie!")
            break
        
        ai_move = find_best_move(board)
        board[ai_move] = 'X'
        print("AI's move:")
        display_board(board)
        
        if winner(board, 'X'):
            print("AI wins!")
            break
        if board_full(board):
            print("It's a tie!")
            break
play_game()

#want to play again?
while True:
    a= input("do you want to play again?[y/n]")
    if a=="y":
        play_game()
    else:
        print("thank you or playing")
        break
