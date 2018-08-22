'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def calculation(dictionary):
    num = 0
    denom1 = 0
    denom2 = 0
    for d in dictionary:
        num += dictionary[d][0] * dictionary[d][1]
    for d in dictionary:
        denom1 += dictionary[d][0] ** 2
    for d in dictionary:
        denom2 += dictionary[d][1] ** 2
    return num/(math.sqrt(denom1) * math.sqrt(denom2))

def tokens(data):
    data = data.lower()
    data = re.sub('[^a-z\ ]', '',data)
    swords = load_stopwords("stopwords.txt")
    data = data.strip().split(" ")
    list1 = []
    for word in data:
        # k = re.sub(r'[^a-z\1]','',word).strip()
        if word not in swords and len(word) > 0:
            list1.append(word)
    return list1
def freq(dictionary,data,index):
    for d in data:
        if d not in dictionary:
            dictionary[d] = [0,0]
            dictionary[d][index] += 1
        else:
            dictionary[d][index] += 1
    return dictionary
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary = {}
    dict1 = tokens(dict1)
    dict2 = tokens(dict2)
    dictionary = freq(dictionary,dict1,0)
    dictionary = freq(dictionary,dict2,1)
    print(dictionary)
    result = calculation(dictionary)
    return result
    # import string
    # import collections
    # import math
    # char = string.ascii_letters + ' '
    # dict1 = "".join(ele for ele in dict1 if ele in char)
    # dict2 = "".join(ele for ele in dict2 if ele in char)
    # dict1 = dict1.lower().strip().split()
    # dict2 = dict2.lower().strip().split()
    # stopword = load_stopwords("stopwords.txt")
    # for word in list(dict1):
    #     if word in stopword:
    #         dict1.remove(word)
    # print(dict1)
    # for word in list(dict2):
    #     if word in stopword:
    #         dict2.remove(word)
    # print(dict2)
    # counter1 = {}
    # counter2 = {}
    # counter1 = collections.Counter(dict1)
    # counter2 = collections.Counter(dict2)
    # # print(counter1.most_common())
    # # print(counter2.most_common())
    # dict3 = []
    # dict4 = []
    # dict5 = []
    # for word in counter1:
    #     if word in counter2:
    #         dict3.append(counter1[word]*counter2[word])
    # for word in counter1:
    #     dict4.append(counter1[word]**2)
    # for word in counter2:
    #     dict5.append(counter2[word]**2)
    # return sum(dict3)/(math.sqrt(sum(dict4)) * math.sqrt(sum(dict5)))




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
