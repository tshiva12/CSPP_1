'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def result(string):
    '''result of string after updating into one string'''
    print("\n")
    return string
def main():
    '''How to take input for the given assignment'''
    # Main function of string
    string = ""
    num = int(input())
    for i in range(num):
        string += str(input())
        i += 1
    result(string)
    print(string)

if __name__ == '__main__':
    main()
