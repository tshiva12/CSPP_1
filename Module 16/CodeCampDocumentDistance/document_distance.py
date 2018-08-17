'''
    Document Distance - A detailed description is given in the PDF
'''
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    import string
    import collections
    import math
    char = string.ascii_letters + ' '
    dict1 = "".join(ele for ele in dict1 if ele in char)
    dict2 = "".join(ele for ele in dict2 if ele in char)
    dict1 = dict1.lower().strip().split()
    dict2 = dict2.lower().strip().split()
    stopword = load_stopwords("stopwords.txt")
    for word in list(dict1):
        if word in stopword:
            dict1.remove(word)
    print(dict1)
    for word in list(dict2):
        if word in stopword:
            dict2.remove(word)
    print(dict2)
    counter1 = {}
    counter2 = {}
    counter1 = collections.Counter(dict1)
    counter2 = collections.Counter(dict2)
    # print(counter1.most_common())
    # print(counter2.most_common())
    dict3 = []
    dict4 = []
    dict5 = []
    for word in counter1:
        if word in counter2:
            dict3.append(counter1[word]*counter2[word])
    for word in counter1:
        dict4.append(counter1[word]**2)
    for word in counter2:
        dict5.append(counter2[word]**2)
    return sum(dict3)/(math.sqrt(sum(dict4)) * math.sqrt(sum(dict5)))




def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
