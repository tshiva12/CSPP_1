'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    string = input()
    string1 = ['!', '@', '#', '$', '%', '^', '&', '*']
    newstr = ""
    len1 = len(string)
    temp = ""
    for i in range(0, len1, 1):
        temp = string[i]
        if temp == string1[i]:
            temp == " "
            newstr += temp
    print(newstr)
if __name__ == "__main__":
    main()
