import curses      #To get key
import random   #To create random tile

def start_board():
    board = [[0] * 4 for _ in range(4)]
    board = refresh(board)
    board = refresh(board)
    return board

def refresh(board):
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 2 if random.random() < 0.7 else 4
    return board

def attach(row):
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False
    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_row) and new_row[i] == new_row[i+1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])
    merged_row += [0] * (4 - len(merged_row))
    return merged_row

"""
Instead of writing whole block for each move
transposing and mirroring the board methods are used 
"""

def mirror(board):
    return [row[::-1] for row in board]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_left(board):
    moved = False
    new_board = []
    for row in board:
        new_row = attach(row)
        if new_row != row:
            moved = True
        new_board.append(new_row)
    return new_board, moved

def move_right(board):
    reversed_board = mirror(board)
    new_board, moved = move_left(reversed_board)
    new_board = mirror(new_board)
    return new_board, moved

def move_up(board):
    transposed = transpose(board)
    new_board, moved = move_left(transposed)
    new_board = transpose(new_board)
    return new_board, moved

def move_down(board):
    transposed = transpose(board)
    new_board, moved = move_right(transposed)
    new_board = transpose(new_board)
    return new_board, moved

def check_move(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
    return True

def print_board(stdscr, board, move_count):
    stdscr.clear()
    stdscr.addstr("Move: {}\n".format(move_count))
    stdscr.addstr("-" * 25 + "\n")
    for row in board:
        line = ""
        for num in row:
            cell = str(num) if num != 0 else "."
            line += "{:^5}".format(cell)
        stdscr.addstr(line + "\n")
    stdscr.addstr("-" * 25 + "\n")
    stdscr.addstr("Press 'q' to quit.\n")
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)       
    stdscr.nodelay(0)        
    stdscr.keypad(True)      
    
    board = start_board()
    move_count = 0
    print_board(stdscr, board, move_count)
    
    while True:
        key = stdscr.getch()
        
        if key == curses.KEY_LEFT:
            new_board, moved = move_left(board)
        elif key == curses.KEY_RIGHT:
            new_board, moved = move_right(board)
        elif key == curses.KEY_UP:
            new_board, moved = move_up(board)
        elif key == curses.KEY_DOWN:
            new_board, moved = move_down(board)
        elif key == ord('q'):
            break  
        else:
            continue 

        if moved:
            board = refresh(new_board)
            move_count += 1
            print_board(stdscr, board, move_count)
            if check_move(board):
                stdscr.addstr("Game Over! Press 'q' to exit.\n")
                stdscr.refresh()
                while stdscr.getch() != ord('q'):
                    pass
                break

if __name__ == "__main__":
    curses.wrapper(main)
