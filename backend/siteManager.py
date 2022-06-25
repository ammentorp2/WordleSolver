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