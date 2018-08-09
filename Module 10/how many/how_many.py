'''Exercise : how many'''
# write a procedure, called how_many, which returns
# the sum of the number of values associated with a dictionary.

def how_many(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    values = adict.values()
    for words in values:
        count += len(words)
    return count

def main():
    '''aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
                aDict['d'] = ['donkey']
                aDict['d'].append('dog')
                aDict['d'].append('dingo')'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        sample = input()
        l_sample = sample.split()
        if l_sample[0][0] not in adict:
            adict[l_sample[0][0]] = [l_sample[1]]
        else:
            adict[l_sample[0][0]].append(l_sample[1])
    print(adict)
    print(how_many(adict))

if __name__ == "__main__":
    main()
