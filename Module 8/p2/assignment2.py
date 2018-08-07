'''Exercise: Assignment-2'''
# Write a Python function, sumofdigits, that takes in one number and
# returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(num):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if num == 0:
        return 0
    if num != 0:
        return (num%10) + sumofdigits(num//10)
def main():
    '''sumofdigits'''
    val = input()
    print(sumofdigits(int(val)))
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(25500)
    main()
