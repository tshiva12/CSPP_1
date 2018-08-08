'''Exercise : Function and Objects Exercise-2'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(list1):
    '''increment'''
    list1 += 1
    return list1
def apply_to_each(list2, func):
    '''incrementing list'''
    print(list(map(func, list2)))

def main():
    '''list'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, inc)

if __name__ == "__main__":
    main()
