import random

secretWord = "giraffe"
guess = ""
tentatives = 3
guessCount = 0
outOfGuesses = False
wordSize = len(secretWord)

print("TIP: The word lenght is: " + str(wordSize))
while guess != secretWord and not(outOfGuesses):
    if guessCount < tentatives:
        position = random.randint(0, wordSize)
        tipNumber = str(guessCount + 1)
        print("TIP Number " + tipNumber + ": The letter at position " + str(position + 1) + " is: " + secretWord[position])
        guess = raw_input("Enter guess: ")
        guessCount += 1
    else:
        outOfGuesses = True

if outOfGuesses:
    print("You lose! The word was: " + secretWord)
else:
    print("You win!")