# Hangman Game by Damian Arnold, v0.0
import random
#words = 'dog1 sink2 tree3 cat4 ape5 take7 eat8 book9 look10 paper11 water12 router13 window14 apple15 artery16 femur17 tongue18 bathroom19 building20 uniformitarianism21 indubitably22 pronunciation23 definition24 Hippopotomonstrosesquippedaliophobia25 trypophobia26 phytoplankton27 pneumonoultramicroscopicsilicovolcanoconiosis28 pneumonia29 descriptian30'. split()
#dictionary version
#stored in key;value pairs
#actual dictionary word (key) : value (definition)
#uses {} to specify a dictionary
words = {'Colors': 'red blue teal gold green white gray brown indigo pink silver'.split(),
         'Animals': 'cat dog cow lion sheep lizaed aligator hippopotamus pig deer'.split(),
         'Shapes': 'square rectangle triangle trapizoid rambus diamond pentagon hexagon octogon dodecehedron'.split(),
         'Fruit': 'apple orange grape grapefuit dragonfruit bannana'.split()}
         



HANGMAN_BOARD = [''
    +---+
        |
        |
        |
       =======''','''
    +---+
    0   |
        |
        |
       =======''','''
    +---+
    0   |
    |   |
        |
       ======''','''
    +---+
     0  |
    /|  |
        |
       ======''','''
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
       ======''','''
    +---+
     0  |
    o-o |
    / \ |
       =====''','''
    +---+
     0  |
    o-o |
    / \ |
   o   o|
      =====''',''']

# def getRandomWord(wordlist): 
#     wordIndex = random.randint(0, len(wordList) - 1)
#     # Ien(listName) -1 is extremely common
#     return wordList[wordIndex] 

def getRandomWord(wordDict): 
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) -1)
    return [wordDict[wordKey][wordIndex], wordKey] 

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
        else:
            return guess

def playAgain():
    print('Do you want to play again? Yes or no?')
    return input().lower().startswitch('y')


print('Play Hangman')


difficulty = 'X'
while difficulty not in 'EMH':
    print('Please choose Easy, Medium, or Hard. Type the first letter then press enter')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
if difficulty == 'H':
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]



missedLetters =''
correctLetters = ''
secretWord,secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is from the ' + secretSet + 'category.\n')
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess



        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                FoundAllLetters = False
                break
        if foundAllLetters:
            print('Congrats! You did it!')
            print('The secret word was' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('You made this number of correct letters' = str(len(correctLetters)))
            print('The secret word was' = secretWord)
            gameIsDode = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord,secretSet = getRandomWord(words)
        else:
            break
    
            

            

