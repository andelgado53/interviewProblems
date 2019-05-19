from pprint import pprint


class board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [["="]*cols for row in range(rows)]
    
    def mark_board_at(self, row, col, marker ="Q"):
        self.board[row][col] = marker
        # pprint(self.board)
    
    def is_safe_at(self, row, col):
        is_safe = self.is_diagonal_safe(row, col) and self.is_row_safe(row, col) and self.is_col_safe(row, col)
        # if is_safe:
        #     self.mark_board_at(row, col)
        return is_safe
    
    def is_diagonal_safe(self, row, col):
        diagonal_point = set()
        current_row = row + 1
        current_col = col + 1

        safe = True

        while ((current_col >= 0 and current_col < self.cols) and (current_row >= 0 and current_row < self.rows)):
            # self.mark_board_at(current_row, current_col, "*")
            diagonal_point.add((current_row, current_col))
            if self.board[current_row][current_col] == "Q":
                return False
            current_row +=1
            current_col +=1
    
        current_row = row - 1
        current_col = col - 1
        while ((current_col >= 0 and current_col < self.cols) and (current_row >= 0 and current_row < self.rows)):
            # self.mark_board_at(current_row, current_col, "*")
            diagonal_point.add((current_row, current_col))
            if self.board[current_row][current_col] == "Q":
                return False
            current_row -=1
            current_col -=1
        
        current_row = row + 1
        current_col = col - 1
        while ((current_col >= 0 and current_col < self.cols) and (current_row >= 0 and current_row < self.rows)):
            # self.mark_board_at(current_row, current_col, "*")
            diagonal_point.add((current_row, current_col))
            if self.board[current_row][current_col] == "Q":
                return False
            current_row +=1
            current_col -=1
        
        current_row = row - 1
        current_col = col + 1
        while ((current_col >= 0 and current_col < self.cols) and (current_row >= 0 and current_row < self.rows)):
            # self.mark_board_at(current_row, current_col, "*")
            diagonal_point.add((current_row, current_col))
            if self.board[current_row][current_col] == "Q":
                return False
            current_row -=1
            current_col +=1
        
        return safe
    
    def is_row_safe(self, row, col):
        c = 0
        row_points = set()
        while (c < self.cols):
            if c != col:
                row_points.add((row, c))
                if self.board[row][c] == "Q":
                    return False
                # self.mark_board_at(row, c, "*")
            c +=1
        return True
    
    def is_col_safe(self, row, col):
        r = 0
        col_points = set()
        while r < self.rows:
            if r != row:
                col_points.add((r, col))
                if self.board[r][col] == "Q":
                    return False
                # self.mark_board_at(r, col, "*")
            r += 1
        return True
    
                
def place_eight_queens(board, queens):
    out = list()
    place_eight_queens_helper(board, queens, 0, out)


def place_eight_queens_helper(board, queen, col, out):
    if queen == 0:
        out.append(board.board)
        print('solution ' + str(len(out)))
        pprint(board.board)
        return 

    for r in range(board.rows):
        if col < board.cols and board.is_safe_at(r, col):
            board.mark_board_at(r, col)
            place_eight_queens_helper(board, queen - 1, col + 1, out)
        board.mark_board_at(r, col, "=")
            

b = board(8, 8)

place_eight_queens(b, 8)
