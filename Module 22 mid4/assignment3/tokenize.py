'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
dictionary = {}
def tokenize(string):
    '''Take the count of each word in a string'''
    list_1 = string.split(' ')
    for index in list_1:
        word = re.sub('[^a-zA-Z0-9]', '', index)
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
            
def main():
    '''Main function'''
    num = int(input())
    for i in range(num):
        string = input()
    tokenize(string)
    print(dictionary)
    

if __name__ == '__main__':
    main()
