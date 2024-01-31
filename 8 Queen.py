def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def print_solution(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")
def solve_queens(board, row):
    if row == len(board):
        print_solution(board)
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1)
board_size = int(input("Enter the number of queens : "))
chessboard = [0] * board_size
solve_queens(chessboard, 0)
