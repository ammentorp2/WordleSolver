from flask import Flask
from flask_cors import CORS
from wordleSolverFunctions import *
import siteManager as siteManager

app = Flask(__name__)
CORS(app)

@app.route('/initSolver',methods=['GET'])
def initSolver():
    # recreate obj just in case
    siteManager.initWordList()
    
    response_body = {
        "wordList" : siteManager.getWordList(),
        "recommendedGuess" : siteManager.getRecommendedGuess()
    }
    
    return response_body

@app.route('/processFeedback/<guess>/<feedback>',methods=['GET'])
def processFeedback(guess,feedback):
    # recreate obj just in case
    
    code = siteManager.processFeedback(guess,feedback)
    response_body = {
        "status" : code,
        "wordList" : siteManager.getWordList(),
        "recommendedGuess" : siteManager.getRecommendedGuess()
    }
    
    return response_body
    
    

if __name__ == '__main__':
    #siteManager.start()
    app.run(debug=True)