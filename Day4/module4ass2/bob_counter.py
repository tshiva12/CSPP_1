'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''count of bob'''
    str1 = input()
    str2 = 'bob'
    count = 0
    for i in range(len(str1)-2):
        if str1[i]+str1[i+1]+str1[i+2] == str2:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
