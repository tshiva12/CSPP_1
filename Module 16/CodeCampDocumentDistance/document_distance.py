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
    print(dict1)
    dict2 = "".join(ele for ele in dict2 if ele in char)
    print(dict2)
    dict1 = dict1.lower().strip().split()
    print(dict1)
    dict2 = dict2.lower().strip().split()
    print(dict2)
    stopword = load_stopwords("stopwords.txt")
    for word in list(dict1):
        if word in stopword:
            dict1.remove(word)
    for word in list(dict2):
        if word in stopword:
            dict2.remove(word)
    counter1 = {}
    counter2 = {}
    counter1 = collections.Counter(dict1)
    counter2 = collections.Counter(dict2)
    # print(counter1.most_common())
    # print(counter2.most_common())
    # numer = []
    denom1 = []
    denom2 = []
    for word in counter1:
        if word in counter2:
            numer.append(counter1[word]*counter2[word])
    for word in counter1:
        denom1.append(counter1[word]**2)
    for word in counter2:
        denom2.append(counter2[word]**2)
    Numerator = sum(numer)
    Denominator = math.sqrt(sum(denom1)) * math.sqrt(sum(denom2))
    return Numerator/Denominator




def load_stopwords(_):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(_, 'r') as _:
        for line in _:
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
