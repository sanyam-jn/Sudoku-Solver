sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]

def board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i !=0:
            print("------------------------")

        for j in range(len(b[0])):
            if j % 3 ==0 and j!=0:
                print(" | ", end="")

            if j == 8:
                    print(b[i][j])
            else:
                    print(str(b[i][j]) + " " , end = "")


def find_emptysqr(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j) #ie the row and column // pos of the empty square
    return None
#pos[0] = row ka pos
#pos[1] = column ka pos

def valid(b, num, pos):
    #checking row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    #checking column
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3


    for i in range(box_y*3 , box_y*3 +3):
        for j in range(box_x*3 , box_x*3 +3):
            if b[i][j] == num and (i,j) != pos:
                return False
    return True


def solving(b):
    find = find_emptysqr(b)
    if not find:
        return True
    else:
        row,column = find

    for i in range (1,10):
        if valid(b,i,(row,column)):
            b[row][column] = i

            if solving(b):
                return True

            b[row][column] = 0 # backtracking

    return False





board(sudoku)
solving(sudoku)
print("_________________________________________")
print("_________________________________________")
print("")
board(sudoku)
