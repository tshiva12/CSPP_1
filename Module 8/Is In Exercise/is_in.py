'''Exercise: Is In'''
# Write a Python function, isIn(char, aStr), that takes in two arguments
# a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isin(char, astr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    val = 0
    length = len(astr)
    if val == length:
        return False
    if char == astr[val]:
        return True
    astr = astr[val + 1:length]
    return isin(char, astr)

def main():
    '''alphabets'''
    data = input()
    data = data.split()
    print(isin((data[0][0]), data[1]))


if __name__ == "__main__":
    main()
