def Sudoku(sudoku):
    row, column = 0, 0
    for i in range(len(sudoku)):
        if len(set(sudoku[i])) == 9:
            row += 1
    for i in range(len(sudoku)):
        columnlist = []
        for j in range(len(sudoku)):
            columnlist.append(sudoku[j][i])
        if len(set(columnlist)) == 9:
            column += 1
    if row == 9 & column == 9:
        print("Given sudoku is solved")

def main():
    sudoku = []
    for i in range(9):
        row = input()
        sudoku.append(row)
        for i in row:
            return row
    Sudoku(sudoku)

if __name__ == '__main__':
    main()