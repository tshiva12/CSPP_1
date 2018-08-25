'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''print dictionary'''
    list1 = list(dictionary.keys())
    list1.sort()
    for i in range(len(list1)):
        print(list1[i], "-", dictionary[list1[i]], end=('\n'))

def main():
    '''Main function'''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
