'''Assume s is a string of lower case characters.'''
#Write a program that counts the num of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    '''count of vowels'''
    string = input()
    countofvowels = 0
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' \
        or char == 'o' or char == 'u':
            countofvowels += 1
    print(countofvowels)
if __name__ == "__main__":
    main()
