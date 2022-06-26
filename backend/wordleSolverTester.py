"""
Python wordle solver.
This program auto-solves the wordle by always guessing the suggested guess
Author : Andrew Ammentorp
"""
import sys

from wordleSolverFunctions import *

# user's guess
guess = ""
# feedback from wordle
feedback = ""

# recomended guess
recomendedGuess = ""
# correct word
correctWord = ""


# main method protection
if __name__ == '__main__':
    # validate args
    if len(sys.argv) != 2:
        print("Usage: python wordleSolverTester.py <correct word>")
        exit(1)
        
    # get correct word    
    correctWord = str(sys.argv[1]).lower().strip()
    #print(correctWord)
    
    wordleSolver = WordleSolver()
    
    if not wordleSolver.validateGuess(correctWord):
        print("Correct word must only be characters and len of 5", correctWord)
        exit(1)
    
    
    # this uses the linux dictionary (words)
    wordleSolver.initGuessList()

    # clac best initial guess
    # calc good initial guess (fun fact: its 'tares'!)
    recomendedGuess = wordleSolver.calcSuggestedGuess()
    #print("Recomended starter word: " , recomendedGuess)
    

    for guesses in range(1000):

        # input guess (and verify)
        guess = recomendedGuess
        

        # calc the feedback
        feedback = wordleSolver.calcFeedback(guess,correctWord)   
        
        code = wordleSolver.processFeedback(guess,feedback)
        
        if code == 0:
            exit(0)
             
        recomendedGuess = wordleSolver.calcSuggestedGuess()
        #print("\nSuggested guess:", recomendedGuess )