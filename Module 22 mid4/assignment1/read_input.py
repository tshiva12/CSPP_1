'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    '''How to take input for the given assignment'''
    # Main function of string
    string = ""
    num = int(input())
    for _ in range(num):
        string += str(input()) + "\n"
        # i += 1
    print(string)

if __name__ == '__main__':
    main()
