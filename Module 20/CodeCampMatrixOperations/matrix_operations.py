import copy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1) != len(m2[0]):
    	print("Error: Invalid input for the matrix")
    	return none
    result = copy.deepcopy(m1)
    for i in range(0,len(m1),1):
    	for j in range(0,len(m2[0]),1):
    		result[i][j] = 0
    		for k in range(0,len(m2),1):
    			result[i][j] = int(result[i][j])
    			result[i][j] += int(m1[i][k]) * int(m2[k][j])
    return result
    # print("matrix m1 is :")
    # for r in m1:
    # 	print(r)
    # print("matrix m2 is :")
    # for r in m2:
    # 	print(r)
    # print("matrix multiply is :")
    # for r in result:
    # 	print(r)

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    len1 = len(m1)
    len2 = len(m2)
    if len1 != len2:
    	return "Error"
    else:
    	result = copy.deepcopy(m1)
    	for i in range(0,len2,1):
    		for j in range(0,len(m2[i]),1):
    			result[i][j] = int(result[i][j])
    			result[i][j] += int(m2[i][j])
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
    for i in range(0,rows,1):
    	row = input().split()
    	matrix.append(row)
    	total += len(row)
    if total != rows * columns:
    	print("error")
    else:
    	return matrix


def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    num1 = input().split(',')
    m1 = read_matrix(num1)
    num2 = input().split(',')
    m2 = read_matrix(num2)
    print(add_matrix(m1,m2))
    print(mult_matrix(m1,m2))

if __name__ == '__main__':
    main()
