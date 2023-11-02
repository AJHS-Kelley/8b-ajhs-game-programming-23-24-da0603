# Hangman Game by Damian Arnold, v0.0

words = 'dog1 sink2 tree3 cat4 ape5 take7 eat8 book9 look10 paper11 water12 router13 window14 apple15 artery16 femur17 tongue18 bathroom19 building20 uniformitarianism21 indubitably22 pronunciation23 definition24 Hippopotomonstrosesquippedaliophobia25 trypophobia26 phytoplankton27 pneumonoultramicroscopicsilicovolcanoconiosis28 pneumonia29 descriptian30'. split()
HANGMAN_BOARD = [''    
    +---+
    0   |
        |
        |
    ======''','''
    +---+
    0   |
    |   |
        |
    =====''','''
    +---+
     0  |
    /|  |
        |
    =====''','''
    +---+
     0  |
    /|\ |
        |
    ======''','''
    +---+
     0   |
    /|\  |
    /    |
    ======''','''
    +---+
     0  |
    /|\ |
    / \ |
    =====''',''']

def getRandomWord(wordlist): 
    wordIndex = random.randint(0, len(wordList) - 1)
    # Ien(listName) -1 is extremely common
    return wordList[wordIndex] 

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter , end = ' ')
    print()

    blanks = '_' * len(secretWord)


    for i in range (len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[;i] + secretWord[i]+ blanks[i+1:]

    for letter in blanks:
        print(letter, and = '')
    print()


def getGuess(alreadyGuessed): 
    while True:
        print('Pleas guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('Letter has been guessed already, try again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please guess a Letter from the English alphabet')
                return guess

#i = 0
#while 1 < 50:
    #word = getRandomWord(words)
    #print(word)
    #i += 1
