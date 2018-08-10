'''Exercise: Assignment-4'''
#We are now ready to begin writing the code that interacts with the player.
#We'll be implementing the playHand function.
#This function allows the user to play out a single hand.
#First, though, you'll need to implement the helper calculateHandlen function, which can be done
#in under five line of code.


def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    res = 0
    for k in hand:
        res = res + hand[k]
    return res

def main():
    '''length of hand'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        data = input()
        l_data = data.split()
        adict[l_data[0]] = int(l_data[1])
    print(calculatehandlen(adict))
if __name__ == "__main__":
    main()
