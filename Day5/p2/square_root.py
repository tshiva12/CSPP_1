'''Write a python program to find the square root of the given number'''
# using approximation method

def main():
    '''square root'''
    val = int(input())
    epsilon = 0.01
    guess = 0.0
    increment = 0.1
    while abs(guess**2 - val) >= epsilon:
        guess += increment
    if abs(guess**2 - val) >= epsilon:
        print("Failed  on square root of", val)
    else:
        print(guess, 'is close to the squareroot of', val)
    #your code here

if __name__ == "__main__":
    main()
