def create(mat, row, col):
    list1= set()
    for i in range(9):
        if mat[row][i] != '0':
            list1.add(mat[row][i])
        if mat[i][col] != '0':
            list1.add(mat[i][col])
    for i in sub_matrix(mat, row, col):
        if i != '0':
            list1.add(i)
    return list1

def sub_matrix(mat, row, col):
    list2 = []
    if row >= 0 and row <= 2 and col >= 0 and col <= 2 :
        for i in range(0, 3):
            for j in range(0, 3):
                list2.append(mat[i][j])
        return list2

    if row >= 0 and row <= 2 and col >= 3 and col <= 5 :
        for i in range(0, 3):
            for j in range(3, 5):
                list2.append(mat[i][j])
        return list2

    if row >= 0 and row <= 2 and col >= 6 and col <= 8 :
        for i in range(0, 3):
            for j in range(6, 9):
                list2.append(mat[i][j])
        return list2

    if row >= 3 and row <= 5 and col >= 0 and col <= 2 :
        for i in range(3, 6):
            for j in range(0, 3):
                list2.append(mat[i][j])
        return list2
    
    if row >= 3 and row <= 5 and col >= 3 and col <= 5 :
        for i in range(3, 6):
            for j in range(3, 6):
                list2.append(mat[i][j])
        return list2

    if row >= 3 and row <= 5 and col >= 6 and col <= 8 :
        for i in range(3, 6):
            for j in range(6, 9):
                list2.append(mat[i][j])
        return list2

    if row >= 6 and row <= 8 and col >= 0 and col <= 2 :
        for i in range(6, 9):
            for j in range(0, 3):
                list2.append(mat[i][j])
        return list2

    if row >= 6 and row <= 8 and col >= 3 and col <= 5 :
        for i in range(6, 9):
            for j in range(3, 6):
                list2.append(mat[i][j])
        return list2

    if row >= 6 and row <= 8 and col >= 6 and col <= 8 :
        for i in range(6, 9):
            for j in range(6, 9):
                list2.append(mat[i][j])
        return list2

def possibilities(matrix):
    for i in range(9):
        for j in range(9):
            result = ""
            set1 = set()
            if matrix[i][j] == '0':
                set1 = create(matrix, i, j)
                # print(s)
            if len(set1) != 0:
                for each in "123456789":
                    if each not in set1:
                        result += each
                print(result)


def main():
    
    matrix = [['0' for x in range(9)] for y in range(9)] 
    # print(matrix)
    input1 = input()
    k = 0
    if (len(input1) < 81):
        print("Invalid input")
    else:
        count=0
        for i in range(9):
            for j in range(9):
                # print(k)
                if input1[k] != '.':
                    matrix[i][j] = input1[k]
                else:
                    count += 1
                k += 1
        # print(matrix)
        # if (k < 81):
        #     print("Invalid input")
        if (count != 0 and k ==81):
            # print("123")
            possibilities(matrix)
        else:
            print("Given sudoku is solved")
        # else:
        #     print("Invalid input")


if __name__=="__main__":
    main()
      

