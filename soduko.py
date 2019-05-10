def check_sudoku(sudo):
    
    number_of_rows = len(sudo)
    
    for column in sudo:
        if len(column) != number_of_rows:
            print ("Matrix is not square")
            return False
        for row in column:
            if type(row) != int:
                print(" Matrix not contain Integers")
                return False 
     
    for row in sudo:
      valid_values = list(range(1,number_of_rows+1))
      for column in row:
          if column in valid_values:
              valid_values.pop(valid_values.index(column))
          else:
              print ("Sudoku not Completed")
              return False
    print ("Sudoku Completed")
    return True


test1 = [[2,1,3],
         [2,3,1],
         [3,1,2]]

test2 = [[1,2,3,4],  
             [2,3,1,3], 
             [3,1,2,3],
             [4,4,4,4]]

test3 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

test4 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

test5 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

test6 = [ [1, 1.5],
               [1.5, 1]]
    
print("test1") 
print(check_sudoku(test1))
print("test2") 
print(check_sudoku(test2))
print("test3") 
print(check_sudoku(test3))
print("test4") 
print(check_sudoku(test4))
print("test5") 
print(check_sudoku(test5))
print("test6") 
print(check_sudoku(test6))