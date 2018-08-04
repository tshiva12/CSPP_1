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
    newstr = ""
    len1 = len(string)
    for i in range(0,len1,1):
    	if string[i] == ['!', '@', '#', '$', '%', '^', '&', '*']:
    		
    		


if __name__ == "__main__":
    main()
