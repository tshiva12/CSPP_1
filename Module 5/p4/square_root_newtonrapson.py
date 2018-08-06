'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''newton raphson method'''
    epsilon = 0.01
    val = int(input())
    res = val/2.0
    count = 0
    while abs(res*res - val) >= epsilon:
        count += 1
        res = res - (((res**2) - val)/(2*res))
    print(res)
if __name__ == "__main__":
    main()
