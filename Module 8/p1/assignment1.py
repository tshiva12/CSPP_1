'''Exercise: Assignment-1'''
# Write a Python function, factorial(n), that takes in one number and
# returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(num):
    '''the factorial of n'''
    # Your code here
    if num == 0:
        return 1
    return num * factorial(num-1)
def main():
    '''fact'''
    val = input()
    print(factorial(int(val)))
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(25500)
    main()
