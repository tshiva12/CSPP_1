'''Exercise : Function and Objects Exercise-3'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(list1):
    '''square'''
    list1 = list1 ** 2
    return list1
def apply_to_each(list2, func):
    '''function'''
    print(list(map(func, list2)))

def main():
    '''main'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, square)

if __name__ == "__main__":
    main()
