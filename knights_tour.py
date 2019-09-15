
dial_path = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['-', '0', '-']
]

def get_moves(row, col, dial):
    pos = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2), (2, -1), (2, 1)]
    valid_moves = []
    for n_r, n_c in pos:
        pos_r = n_r + row
        pos_c = n_c + col
        if (pos_r < len(dial) and pos_r >= 0)  and (pos_c < len(dial[0]) and pos_c >= 0):
            if dial[pos_r][pos_c] != '-':
                valid_moves.append((pos_r  , pos_c))
    return valid_moves

def numPhoneNumbers_rec(startdigit, phonenumberlength):
    digits_to_row_col = {
        0: (3, 1),
        1: (0, 0),
        2: (0, 1), 
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
        }
    dial_path = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['-', '0', '-']
    ]
    row, col = digits_to_row_col[startdigit]
    out = []
    def helper(row, col, pn):
        if pn == phonenumberlength:
            return 1
        moves = get_moves(row, col, dial_path)
        if len(moves) == 0:
            return 0
        else:
            phones = 0
            for m in moves:
                phones += helper(m[0], m[1], pn+1)
            return phones
    return helper(row, col, 1)
    # return len(out)

print(numPhoneNumbers_rec(0, 3))
# print(get_moves(1, 2, dial_path))