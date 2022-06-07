"""
Python wordle solver - user input version
This program is built upon https://replit.com/@jamesabela/WordleSolver
Author : Andrew Ammentorp
"""
# TODO explicity say main method
from wordleSolverFunctions import *

# user's guess
guess = ""
# feedback from wordle
feedback = ""

# this uses the linux dictionary (words)
initGuessList()

print("Recomended starter word: " , calcSuggestedGuess())

# loop 6 times for our 6 guesses (duh)
for guesses in range(6):

    # input guess (and verify)
    guess = input("\n5 letter word: ").lower()
    validGuess = validateGuess(guess)
    
    while validGuess == False:
        print("Word should be 5 letters in length and only be alphabetical characters")
        guess = input("\n5 letter word: ").lower()
        validGuess = validateGuess(guess)

    # verify feedback
    print("g - green, y - yellow, w - wrong / grey")
    feedback = input("Feedback: ").lower()
    validFeedback = validateFeedback(feedback)
    
    while validFeedback == False:
        print("Feedback should only have g,y, or w and be 5 letters in length")
        feedback = input("Feedback: ").lower()
        validFeedback = validateFeedback(feedback)
        
    if feedback == "ggggg":
        print("Congrats it took " + str(guesses+1) + " guesses!")
        exit(0)
    else:
        processFeedback(guess,feedback,[],guesses,"")

    counter = 0
    print("Available words to guess:")
    for word in getGuessList():
        print(word,end=", ")
        counter+=1
        if counter == 8:
            print("")
            counter = 0
    
    print("\nSuggested guess:", calcSuggestedGuess() )