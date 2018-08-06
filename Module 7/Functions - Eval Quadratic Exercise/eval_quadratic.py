'''Exercise: eval quadratic'''
# Write a Python function, evalQuadratic(a, b, c, x),
# that returns the value of the quadratic a . x 2 + b . x + c
# This function takes in four numbers and returns a single number.
def evalquadratic(val1, val2, val3, val4):
    ''' quadratic expression'''
    res = val1*val4**2 + 2*val2*val4 + val3
    return res
def main():
    ''' quadratic expression'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for val4 in enumerate(len(data)):
        temp = str(data[val4]).split('.')
        if temp[1] == '0':
            data[val4] = int(float(str(data[val4])))
        else:
            data[val4] = data[val4]
    print(evalquadratic(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()
