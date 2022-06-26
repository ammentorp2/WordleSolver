"""
    This file runs our backend and handles our endpoints
"""

from flask import Flask
from . import wordleSolverFunctions
#from wordleSolverFunctions import *
from . import siteManager as siteManager
#import siteManager as siteManager


app = Flask(__name__)

"""
    Initilizes wordle solver word list
"""
@app.route('/initSolver',methods=['GET'])
def initSolver():
    # recreate obj just in case
    siteManager.initWordList()
    
    response_body = {
        "wordList" : siteManager.getWordList(),
        "recommendedGuess" : siteManager.getRecommendedGuess()
    }
    
    return response_body

"""
    Based on a user's guess and the feedback it updates the wordlist
"""
@app.route('/processFeedback/<guess>/<feedback>',methods=['GET'])
def processFeedback(guess,feedback): 
    code = siteManager.processFeedback(guess,feedback)
    response_body = {
        "status" : code,
        "wordList" : siteManager.getWordList(),
        "recommendedGuess" : siteManager.getRecommendedGuess()
    }
    
    return response_body
    
"""
    Auto solves for a word
"""
@app.route('/solveForWord/<correctWord>',methods=['GET'])
def solveForWord(correctWord):
    response_body = siteManager.solveForWord(correctWord)
    
    return response_body
    
@app.route('/',methods=['GET'])    
def home():
    return "<h1>Welcome to the Ammentorp wordle solver endpoints. For documentation click here<h1>"