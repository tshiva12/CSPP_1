'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''Take the count of each word in a string'''
    dict1 = {}
    list_1 = string.split(' ')
    for index in list_1:
        word = re.sub('[^a-zA-Z0-9]', '', index)
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1
    return dict1
def main():
    '''Main function'''
    dict1 = {}
    num = int(input())
    for _ in range(num):
        string = input()
    tokenize(string)
    print(dict1)
if __name__ == '__main__':
    main()
