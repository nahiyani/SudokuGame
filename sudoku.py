def checkEmpty(sudoku, x, y):
    if sudoku[x - 1][y - 1] == "0":
        return True
    return False

def replace(sudoku, x, y):
    x = int(input("What x-position do you want to replace? "))
    y = int(input("What y-position do you want to replace? "))
    z = int(input("What number do you want to replace it with? "))

    temp = sudoku[x]
    sudoku[x] = ""

    for i in range(0, x):
        sudoku[i] += str(temp[i])
    sudoku[i] = str(z)
    
    
sudoku = ["080600010", "000008256", "001000000", "000904603", "009070500", "407502000", "000000800", "713400000", "050009030"]

for i in range(len(sudoku)):
    print(sudoku[i])
print(checkEmpty(sudoku, 1, 2))

'''
    for i in range(1, 10):
        for j in range(1, 10):
            if sudoku[i][j] == "0":
                return True
    return False
    '''