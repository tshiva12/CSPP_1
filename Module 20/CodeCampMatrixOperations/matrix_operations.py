'''Matrix operations'''
import copy
def mult_matrix(matrix1, matrix2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(matrix1) != len(matrix2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    else:
        list1 = []
        for i in range(0, len(matrix1), 1):
            list2 = []
            for j in range(0, len(matrix2[0]), 1):
                result = 0
                for k in range(0, len(matrix2), 1):
                    result += int(matrix1[i][k]) * int(matrix2[k][j])
                list2.append(result)
            list1.append(list2)
        return list1
    # print("matrix m1 is :")
    # for r in matrix1:
    #   print(r)
    # print("matrix m2 is :")
    # for r in matrix2:
    #   print(r)
    # print("matrix multiply is :")
    # for r in result:
    #   print(r)

def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    len1 = len(matrix1)
    len2 = len(matrix2)
    if len1 != len2:
        print("Error: Matrix shapes invalid for addition")
        return None

    result = copy.deepcopy(matrix1)
    for i in range(0, len2, 1):
        for j in range(0, len(matrix2[i]), 1):
            result[i][j] = int(result[i][j])
            result[i][j] += int(matrix2[i][j])
    return result

def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows = int(size[0])
    columns = int(size[1])
    total = 0
    matrix = []
    for _ in range(0, rows, 1):
        row = input().split()
        matrix.append(row)
        total += len(row)
    if total != rows * columns:
        print("Error: Invalid input for the matrix")
def main():
    '''main function of matrix operations'''
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    num1 = input().split(',')
    matrix1 = read_matrix(num1)
    # print(matrix1)
    num2 = input().split(',')
    matrix2 = read_matrix(num2)
    # print(matrix2)
    if matrix1 is None or matrix2 is None:
        return None
    print(add_matrix(matrix1, matrix2))
    print(mult_matrix(matrix1, matrix2))

if __name__ == '__main__':
    main()
