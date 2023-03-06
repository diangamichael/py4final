import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def get_move(player):
    move = input(f"Player {player}, enter your move in the format 'row,column': ")
    while not valid_move(move):
        move = input(f"Invalid move. Player {player}, enter your move in the format 'row,column': ")
    return move

def valid_move(move):
    try:
        row, col = move.split(",")
        return row.isdigit() and col.isdigit() and int(row) in range(3) and int(col) in range(3)
    except:
        return False

def game_over(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return True
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != " ":
            return True
    if len(set([board[row][row] for row in range(3)])) == 1 and board[0][0] != " ":
        return True
    if len(set([board[row][2-row] for row in range(3)])) == 1 and board[0][2] != " ":
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = random.choice(players)
    print(f"Player {turn} will go first.")
    while not game_over(board):
        print_board(board)
        move = get_move(turn)
        row, col = move.split(",")
        board[int(row)][int(col)] = turn
        turn = players[(players.index(turn)+1)%2]
    print_board(board)
    print(f"Player {turn} wins!")

play_game()