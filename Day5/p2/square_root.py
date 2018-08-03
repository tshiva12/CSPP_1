'''Write a python program to find the square root of the given number'''
# using approximation method

def main():
    '''square root'''
    val = int(input())
    epsilon = 0.01
    guess = 0.0
    increment = 0.001
    num = 0
    while abs(guess**2 -val) >= epsilon:
        guess += increment
        num += 1
    if abs(guess**2 - val) >= epsilon:
        print("Failed  on square root of", val)
    else:
        print(guess, 'is close to the squareroot of', val)
    #your code here

if __name__ == "__main__":
    main()
