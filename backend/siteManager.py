"""
    This file takes care of our wordleSolver object
"""

from wordleSolverFunctions import *
wordleSolver = WordleSolver()
   
# Initilize the wordlist   
def initWordList():
    wordleSolver.initGuessList()

# Gets the word list    
def getWordList():
    return wordleSolver.getGuessList()

# Gets the suggested guess    
def getRecommendedGuess():
    return wordleSolver.calcSuggestedGuess()

# Processes feedback    
def processFeedback(guess,feedback):
    return wordleSolver.processFeedback(guess,feedback)

# Solves for a word (basically this is wordleSolverTester.py)    
def solveForWord(correctWord):
    response_body = {
        "status" : 0,
        "pastGuesses" : [],
        "pastFeedbacks" : []
    }
    
    pastFeedbacks = []
    pastGuesses = []
    
    wordleSolver.initGuessList()
    
    if not correctWord in wordleSolver.getGuessList():
        response_body['status'] = 1
    else:
        recomendedGuess = wordleSolver.calcSuggestedGuess()
        for guesses in range(1000):
            # input guess (and verify)
            guess = recomendedGuess
            

            # calc the feedback
            feedback = wordleSolver.calcFeedback(guess,correctWord)   
            pastFeedbacks.append(feedback)
            pastGuesses.append(guess)
            
            code = wordleSolver.processFeedback(guess,feedback)
            
            if code == 0:
                response_body['pastGuesses'] = pastGuesses
                response_body['pastFeedbacks'] = pastFeedbacks
                break
                 
            recomendedGuess = wordleSolver.calcSuggestedGuess()
    
    return response_body