'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''finding frequency'''
    list1 = list(dictionary.keys())
    len1 = len(list1)
    list1.sort()
    for i in range(len1):
        dictionary[list1[i]] = "#" * dictionary[list1[i]]
        print(list1[i], "-", dictionary[list1[i]], end=('\n'))

def main():
    '''Main finction'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
