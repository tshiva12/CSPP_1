'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadwords():
    """
    Returns a list of valid words. Words are strings of lowercase letters
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseword(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadwords()

def iswordguessed(secretword, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # FILL IN YOUR CODE HERE...
    count = 0
    for char in secretword:
        if char in lettersguessed:
            count += 1
    if count == len(secretword):
        return True
    return False



def getguessedword(secretword, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    list2 = ''
    for char in secretword:
        if char in lettersguessed:
            list2 += char
        else:
            list2 += '_'
    return list2



def getavailableletters(lettersguessed):
    '''import string'''
    import string
    # FILL IN YOUR CODE HERE...
    str1 = string.ascii_lowercase
    res = ''
    for char in str1:
        if char in lettersguessed:
            continue
        else:
            res += char
    return ''.join(res)
def sampleinput(guess):
    '''testing input'''
    if len(guess) > 1 or (guess <= 'a' and guess >= 'z'):
        print("Invalid Input....")
        return False
    return True
def hangman(secretword):
    '''
    secretWord: string, the secret word to guess

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    lettersguessed = []
    print("I am thinking of a word that is ", len(secretword), "letters word")
    print("---------------------------------------")
    flag = False
    maxguessletters = len(secretword) + 7
    print(getguessedword(secretword, lettersguessed))
    while maxguessletters != 0:
        print("You have", maxguessletters, "Left")
        print("AvailableLetters:", getavailableletters(lettersguessed))
        guess = input("Please guess a letter: ")
        maxguessletters -= 1

        if not sampleinput(guess):
            continue
        lettersguessed.append(guess)
        flag = iswordguessed(secretword, lettersguessed)
        if flag:
            break
        print(getguessedword(secretword, lettersguessed))
    print(secretword)
    if flag:
        print("Congratulations you guessed the correct word..........")
    else:
        print("Try Again.....")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

def main():

    '''
    Main function for the given program
    When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secretWord while you're testing)
	'''
	# secretWord = chooseWord(wordlist).lower()
	# hangman(secretWord)
    secretword = chooseword(wordlist).lower()
    hangman(secretword)


if __name__ == "__main__":
    main()
