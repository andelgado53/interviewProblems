# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

def in_grid(row, col, grid):
    if (row >= 0 and row < len(grid)) and (col >= 0 and col < len(grid[0])):
        return True
    else:
        return False

def get_neighbors(row, col, grid):
    neighbors = []
    if in_grid(row -1, col, grid) and grid[row -1][col] == 1:
        neighbors.append((row - 1, col))
    if in_grid(row + 1, col, grid) and grid[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    if in_grid(row, col - 1, grid) and grid[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    if in_grid(row, col + 1, grid) and grid[row][col + 1] == 1:
        neighbors.append((row, col + 1))
    return neighbors


grid = [[1,1,0,0,0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]

def get_number_of_islands(grid):
    row_index = 0
    col_index = 0
    islands = []
    while row_index < len(grid):
        col_index = 0
        while col_index < len(grid[0]):
            if grid[row_index][col_index] == 1:
                islands.append((row_index, col_index))
            col_index += 1
        row_index += 1
    q = []
    cnt = 0
    seen = set()
    for island in islands:
        if island not in seen:
            cnt +=1
            q. append(island)
            while len(q) > 0:
                current = q.pop(0)
                if current not in seen:
                    seen.add(current)
                    for n in get_neighbors(current[0], current[1], grid):
                        if n not in seen:
                            q.append(n)

    print(cnt)
    return islands

grid1 = [[1,1,1,1,0],[1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]

print(get_number_of_islands(grid1))
print(get_number_of_islands(grid))