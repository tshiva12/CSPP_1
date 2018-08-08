'''Exercise : Function and Objects Exercise-1'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]
def apply_to_each(list2, func):
    '''positive'''
    print(list(map(func, list2)))
def main():
    '''positive numbers'''
    data = input()
    data = data.split()
    list1 = []
    for index in data:
        list1.append(int(index))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
