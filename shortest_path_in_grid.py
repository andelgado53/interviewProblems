# Shortest Path In 2D Grid With Keys And Doors
# Problem Statement:
# Given a 2D grid of size n * m, that represents a maze-like area, a start cell and a goal cell, 
# you have to find the shortest path from start to the goal.
# You can go up, down, left or right from a cell, but not diagonally.
# Each cell in the grid can be either land or water or door or key to some doors.
# You can only travel on land cells, key cells and door cells, and not on water cells.
# Each type of key will open only one type of door. There can be multiple identical keys of the same type. 
# There can also be multiple doors of the same type. You cannot travel through a door, unless you have picked 
# up the key to that door before arriving there. If you have picked up a certain type of key, 
# then it can be re-used on multiple doors of same kind.
# It is allowed to revisit a cell.
# Cells in the grid can be described as:
# '#' = Water.
# '.' = Land.
# 'a' = Key of type 'a'. All lowercase letters are keys.
# 'A' = Door that opens with key 'a'. All uppercase letters are doors.
# '@' = Starting cell.
# '+' = Ending cell (goal).


grid = [ 
    [".", ".", ".", "B"],
    [".", "b", "#", "."],
    ["@", "#", "+", "."]
]

def find_start(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                return row, col

def get_all_moves(row, col, grid):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    possible_moves = []
    for r_move, c_move in moves:
        new_ro = row + r_move
        new_col = col + c_move
        if (new_ro >= 0 and new_ro < len(grid))  and new_col >= 0 and new_col < len(grid[row]):
            possible_moves.append((new_ro, new_col))
    return possible_moves

def get_possible_moves(grid, row, col, current_keys):
    moves = get_all_moves(row, col, grid)
    doors = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    possible_moves = []
    for row, col in moves:
        cell_value = grid[row][col]
        if cell_value == "#" or cell_value in doors and cell_value.lower() not in current_keys:
            continue
        else:
            possible_moves.append((row, col))
    return possible_moves


def escape(grid):
    start_row, start_col = find_start(grid)
    my_keys = set()
    visited = set()
    path = []
    keys = {'a', 'b','c','d','e','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    # visited.add((start_row, start_col))
    def explore(grid, visited, row, col):
        if grid[row][col] == "+":
            path.append((row, col))
            return path
        else:
            pos_moves = get_possible_moves(grid, row, col, my_keys)
            for new_r, new_c in pos_moves:
                path.append((new_r, new_c))
                if grid[new_r][new_c] in keys:
                    my_keys.add(grid[new_r][new_c])
                explore(grid, visited, new_r, new_c)

                if grid[new_r][new_c] in keys:
                    my_keys.remove(grid[new_r][new_c])
                    path.pop(-1)



        # pos_moves = get_possible_moves(grid, row, col, my_keys)
        # # visited.add((row, col))
        # for new_r, new_col in pos_moves:
        #     if grid[new_r][new_col] == "+":
        #         path.append((new_r, new_col))
        #         found_path = True
        #         return (path, True)
        #     elif (new_r, new_col) not in visited and (new_r, new_col) != (row, col):
        #         if grid[new_r][new_col] in keys:
        #             my_keys.add(grid[new_r][new_col])
        #         path.append((new_r, new_col))
        #         explored_path, solved = explore(grid, visited, new_r, new_col)
        #         if solved:
        #             return (explored_path, solved)
        #         else:
        #             print("attempted path: " + str(path))
        #             if grid[new_r][new_col] in keys:
        #                 my_keys.remove(grid[new_r][new_col])
        #             path.pop(-1)
        # # visited.remove((row, col))
        # return (path, False)
    final_path = explore(grid, visited, start_row, start_col)[0]
    final_path.insert(0, (start_row, start_col))
    return final_path

# print(escape(grid))
# [[2 0],[1 0],[1 1],[0 1],[0 2],[0 3],[1 3],[2 3],[2 2]]

g = [
    ['+','B','.','.','.'],
    ['#','#','#','#','.'],
    ['#','#','b','#','.'],
    ['a','.','.','.','A'],
    ['#','#','@','#','#']
]
print(escape(g))
[(4, 2), (3, 2), (2, 2), (3, 2), (3, 1), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4),
(1, 4), 
(0, 4),
(0, 3),
(0, 2),
(0, 1),
(0, 0)
]
# print(get_all_moves(3, 2, g))
# print(get_possible_moves(g, 3, 1, set()))