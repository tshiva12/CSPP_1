'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    '''remove special characters and spaces'''
    len1 = len(string)
    i = 0
    res = ""
    while i < len1:
        if string[i] in ['!', '@', '#', '$', '%', '^', '&', '*', '.']:
            res += ""
        else:
            res += string[i]
        i = i+1
    return res.replace(" ", "")

def main():
    '''Main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
