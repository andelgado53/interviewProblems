# Knight's Tour On A Chess Board
# Problem Statement:
# You are given a rows * cols chessboard and a knight that moves like in normal chess. 
# Currently knight is at starting position denoted by start_row th row and start_col th col, 
# and want to reach at ending position denoted by end_row th row and end_col th col.  
# The goal is to calculate the minimum number of moves that the knight needs to take to get
#  from starting position to ending position.
import pprint


def get_possible_movers(row, col, rows, cols):
    moves = []
    if row + 2 < rows and col + 1 < cols:
        moves.append((row + 2, col + 1))
    if row + 2 < rows and col - 1 >= 0:
        moves.append((row + 2, col - 1))
    if row + 1 < rows and col + 2 < cols:
        moves.append((row + 1, col + 2))
    if row + 1 < rows and col - 2 >= 0:
        moves.append((row + 1, col - 2))

    if row - 2 >= 0 and col + 1 < cols:
        moves.append((row - 2, col + 1))
    if row - 2 >= 0 and col - 1 >= 0 :
        moves.append((row - 2, col - 1))
    if row - 1 >= 0 and col + 2 < cols:
        moves.append((row - 1, col + 2))
    if row - 1 >= 0 and col - 2 >= 0 :
        moves.append((row - 1, col - 2))

    if col + 2 < cols and row + 1 < rows:
        moves.append((row + 1, col + 2))
    if col + 2 < cols and row - 1 >= 0:
        moves.append((row - 1, col + 2))
    if col + 1 < cols and row + 2 < rows:
        moves.append((row + 2, col + 1))
    if col + 1 < cols and row - 2 >= 0:
        moves.append((row - 2, col + 1))

    if col - 2 >= 0 and row + 1 < rows:
        moves.append((row + 1, col - 2))
    if col - 2 >= 0 and row - 1 >= 0:
        moves.append((row - 1, col - 2,))
    if col - 1 >= 0 and row + 2 < rows:
        moves.append((row + 2, col - 1, ))
    if col - 1 >= 0 and row - 2 >= 0:
        moves.append((row - 2, col - 1))
    return set(moves)

def trace_steps(end, start, parents):
    current = end
    path = []
    while current != start:
        path.insert(0, current)
        current = parents[current]
    path.insert(0, start)
    return path
        

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    if start_row == end_row and start_col == end_col:
        return 0
    queue = [] 
    queue.append((start_row, start_col))
    seen = set()
    parents = {}
    steps = 0
    while len(queue) > 0:
        current_move = queue.pop(0)
        seen.add(current_move)
        for move in get_possible_movers(current_move[0], current_move[1], rows, cols):
            if move not in seen:
                parents[move] = current_move
                if move[0] == end_row and move[1] == end_col:
                    return len(trace_steps(move, (start_row, start_col), parents)) - 1
                else:
                    queue.append(move)
                    seen.add(move)
    return -1

print(find_minimum_number_of_moves(5, 5, 0, 0, 4, 1))
# print(get_possible_movers(0, 0, 5, 5))
# print(get_possible_movers(1, 2, 5, 5))
# print(get_possible_movers(3, 3, 5, 5))
# print(get_possible_movers(4, 3, 8, 8))