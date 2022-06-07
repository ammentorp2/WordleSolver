"""
Python wordle solver.
This program auto-solves the wordle by always guessing the suggested guess
Author : Andrew Ammentorp
"""
# TODO test with vales and wears
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
    
    # we use the first 2 guesses for information gathering
    # calc next best guess (highest freq score and not characters in inital guess)
    # fun fact it's 'doing'!
    secondGuess = wordleSolver.calcSecondGuess(recomendedGuess)
    
    
    # use initial guess
    guess = recomendedGuess
    feedback = wordleSolver.calcFeedback(guess,correctWord)
    wordleSolver.processFeedback(guess,feedback,correctWord)

    # TODO edge case if just missing one letter and everything else green

    # now use second guess    
    guess = secondGuess
    feedback = wordleSolver.calcFeedback(guess,correctWord)
    wordleSolver.processFeedback(guess,feedback,correctWord)
    
    recomendedGuess = wordleSolver.calcSuggestedGuess()

    for guesses in range(1000):

        # input guess (and verify)
        guess = recomendedGuess
        

        # calc the feedback
        feedback = wordleSolver.calcFeedback(guess,correctWord)   
        
        wordleSolver.processFeedback(guess,feedback,correctWord)
             
        recomendedGuess = wordleSolver.calcSuggestedGuess()
        #print("\nSuggested guess:", recomendedGuess )