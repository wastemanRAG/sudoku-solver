def is_valid(board, r, c, k):
    return (
        k not in board[r] and
        k not in [board[i][c] for i in range(9)] and
        k not in [board[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3) for j in range(c // 3 * 3, c // 3 * 3 + 3)]
    )

def solve_sudoku(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for k in range(1, 10):
                    if is_valid(board, r, c, k):
                        board[r][c] = k
                        if solve_sudoku(board):
                            return True
                        board[r][c] = 0
                return False
    return True

def input_sudoku_board():
    game_board = []
    row_amount = 0
    while row_amount < 9:
        row_inputs = input(f"Please enter row {row_amount+1} values (0 = empty space): ")
        if len(row_inputs) == 9:
            row = [int(x) if x.isdigit() and int(x) != 0 else 0 for x in row_inputs]
            game_board.append(row)
            row_amount += 1
        else:
            print('Please enter 9 digits')
    return game_board

def eliminate_duplicates(board):
    for col in range(9):
        column_values = [board[row][col] for row in range(9)]
        for value in set(column_values):
            if value != 0 and column_values.count(value) > 1:
                for row in range(9):
                    if board[row][col] == value:
                        board[row][col] = 0

game_board = input_sudoku_board()
eliminate_duplicates(game_board)
solve_sudoku(game_board)
print(*game_board, sep='\n')
