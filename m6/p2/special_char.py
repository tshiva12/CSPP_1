'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str1 = input()
    len1 = len(str1)
    str2 = ['!', '@', '#', '$', '%', '^', '&', '*']
    res = ""
    for i in range(0, len1, 1):
        temp = str1[i]
        for j in range(i, len1, 1):
            if temp != str2[j]:
                temp += " "
                res = temp
        res += temp
    print(res)
if __name__ == "__main__":
    main()
