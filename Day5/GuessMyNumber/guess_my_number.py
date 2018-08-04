'''Guess My Number Exercise'''

def main():
    '''lucky number'''
    mid = 50
    high = 100
    low = 0
    #luckynum = 0
    num = 'l'
    while num != 'c':
        print(mid)
        num = input("enter 'h' if guess is too high,'l' if its too low.\
            'c' to indicate I guessed correctly")
        if num == 'h':
            high = mid
            mid = (high+low)//2
        elif num == 'l':
            low = mid
            mid = (high+low)//2
    print('your lucky number is :', mid)
if __name__ == "__main__":
    main()
