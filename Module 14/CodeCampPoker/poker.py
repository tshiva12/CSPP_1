'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def new(hand):
    '''Appending rank'''
    count = len(hand)
    newhand = []
    for element in range(count):
        if hand[element][0] == 'A':
            newhand.append(14)
        elif hand[element][0] == 'K':
            newhand.append(13)
        elif hand[element][0] == 'Q':
            newhand.append(12)
        elif hand[element][0] == 'J':
            newhand.append(11)
        elif hand[element][0] == 'T':
            newhand.append(10)
        else:
            newhand.append(int(hand[element][0]))
    return newhand
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    count = len(hand)
    newlist = sorted(new(hand))
    for element in range(count-1):
        if newlist[element+1] - newlist[element] != 1:
            return False
    return True

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    count = len(hand)
    for element in range(count - 1):
        if hand[element][1] != hand[element+1][1]:
            return False
    return True

def is_fourofakind(hand):
    ''' fourofakind have same number cards of four and one different'''
    cnt = 0
    newlist = sorted(new(hand))
    for i in range(len(newlist)-3):
        if newlist[i] == newlist[i+1] == newlist[i+2] == newlist[i+3]:
            cnt += 1
    if cnt == 1:
        return True
    return False
def is_threeofakind(hand):
    '''threeofakind have same number cards of three and two different'''
    count = 0
    newlist = sorted(new(hand))
    for i in range(len(newlist)-2):
        if newlist[i] == newlist[i+1] == newlist[i+2]:
            count += 1
    if count == 1:
        return True
    return False

def is_onepair(hand):
    '''Only onepair of cards are same in number'''
    newlist = sorted(new(hand))
    newlist1 = set(newlist)
    if len(newlist) - len(newlist1) == 1:
        return True
    return False

def is_twopair(hand):
    '''It have two pairs of same cards and one different'''
    newlist = sorted(new(hand))
    newlist1 = set(newlist)
    if len(newlist) - len(newlist1) == 2:
        return True
    return False

def is_fullhouse(hand):
    '''It have three of same rank and two of same rank'''
    count = 0
    i = 0
    newlist = sorted(new(hand))
    if newlist[i] == newlist[i+1] == newlist[i+2] or newlist[i+3] == newlist[i+4]:
        count += 1
    elif newlist[i+3] == newlist[i+4] and newlist[i] == newlist[i+1] == newlist[i+2]:
        count += 1
    if count == 1:
        return True
    return False

def is_highcard(hand):
    count = 0
    newlist = sorted(new(hand))
    for i in range(len(newlist)):
        if newlist[i] < newlist[i+1]:
            count += 1
    if count == 5:
        return True
    return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_threeofakind(hand):
        return 3
    if is_onepair(hand):
        return 1
    if is_twopair(hand):
        return 2
    if is_fullhouse(hand):
        return 7
    if is_fourofakind(hand):
        return 4
    if is_straight(hand) and is_flush(hand):
        return 8
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    return 0
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for _ in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
