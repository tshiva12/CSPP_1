'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''Bisection method'''
    value = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    count = 0
    low = 1.0
    high = value
    res = (high+low)/2.0
    while abs(res**2 - value) >= epsilon:
        count += 1
        if res**2 < value:
            low = res
        else:
            high = res
        res = (high+low)/2.0
    print(count)
    print(res)
    # your code starts here

if __name__ == "__main__":
    main()
