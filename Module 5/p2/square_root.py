'''Write a python program to find the square root of the given number'''
# using approximation method

def main():
    '''square root'''
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
    #your code here

if __name__ == "__main__":
    main()
