from wordleSolverFunctions import *
wordleSolver = WordleSolver()
    
def initWordList():
    wordleSolver.initGuessList()
    
def getWordList():
    return wordleSolver.getGuessList()
    
def getRecommendedGuess():
    return wordleSolver.calcSuggestedGuess()
    
def processFeedback(guess,feedback):
    return wordleSolver.processFeedback(guess,feedback)