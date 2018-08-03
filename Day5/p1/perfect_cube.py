'''Write a python program to find if the given number is a perfect cube or not'''
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    '''perfect cube'''
    # input is captured in s
    value = int(input())
    res = 0
    while res ** 3 < value:
        res += 1
    if res ** 3 != value:
        print(str(value) + " " + "is not a perfect cube")
    else:
        print(str(value) + " " + "is a perfect cube")
    # watch out for the data type of value stored in s
    # your code starts here

if __name__ == "__main__":
    main()
