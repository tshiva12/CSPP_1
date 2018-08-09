'''Exercise : Biggest Exercise'''
#Write a procedure, called biggest, which returns the key corresponding to the entry with the
#largest number of values associated with it. If there is more than one such entry,
#return any one of the matching keys.


def biggest(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    flag = 0
    max_res = ""
    for keys in adict:
        if len(adict[keys]) > flag:
            flag = len(adict[keys])
            max_res += keys
    return max_res[-1]
def main():
    '''biggest'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        sample = input()
        l_sample = sample.split()
        if l_sample[0][0] not in adict:
            adict[l_sample[0][0]] = [l_sample[1]]
        else:
            adict[l_sample[0][0]].append(l_sample[1])
    print(biggest(adict))


if __name__ == "__main__":
    main()
