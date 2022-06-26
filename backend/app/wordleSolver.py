"""
Python wordle solver - user input version
This program is built upon https://replit.com/@jamesabela/WordleSolver
Author : Andrew Ammentorp
"""
from wordleSolverFunctions import *

# user's guess
guess = ""
# feedback from wordle
feedback = ""

# main method protection
if __name__ == '__main__':
    # init solver object
    wordleSolver = WordleSolver()
    
    # this uses the linux dictionary (words)
    wordleSolver.initGuessList()

    print("Recomended starter word: " , wordleSolver.calcSuggestedGuess())

    # loop 6 times for our 6 guesses (duh)
    for guesses in range(6):

        # input guess (and verify)
        guess = input("\n5 letter word: ").lower()
        validGuess = wordleSolver.validateGuess(guess)
        
        while validGuess == False:
            print("Word should be 5 letters in length and only be alphabetical characters")
            guess = input("\n5 letter word: ").lower()
            validGuess = wordleSolver.validateGuess(guess)

        # verify feedback
        print("g - green, y - yellow, w - wrong / grey")
        feedback = input("Feedback: ").lower()
        validFeedback = wordleSolver.validateFeedback(feedback)
        
        while validFeedback == False:
            print("Feedback should only have g,y, or w and be 5 letters in length")
            feedback = input("Feedback: ").lower()
            validFeedback = wordleSolver.validateFeedback(feedback)
            
        
        code = wordleSolver.processFeedback(guess,feedback)

        if code == 0:
            exit(0)

        counter = 0
        print("Available words to guess:")
        for word in wordleSolver.getGuessList():
            print(word,end=", ")
            counter+=1
            if counter == 8:
                print("")
                counter = 0
          
        print("\nSuggested guess:", wordleSolver.calcSuggestedGuess() )
        