'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''approximation method'''
    val = int(input())
    epsilon = 0.01
    res = 0.0
    increment = 0.1
    while abs(res**2 - val) >= epsilon:
        res += increment
    if abs(res**2 - val) >= epsilon:
        print("Failed  on square root of", val)
    else:
        print(res)
if __name__ == "__main__":
    main()
