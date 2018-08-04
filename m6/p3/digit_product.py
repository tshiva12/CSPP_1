'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    num = int(input())
    prd = 1
    if num == 0:
        print(num)
    else:
        while num != 0:
            rem = num%10
            prd *= rem
            num //= 10
        print(prd)


if __name__ == "__main__":
    main()
