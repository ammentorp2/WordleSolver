from flask import Flask
from flask_cors import CORS
from wordleSolverFunctions import *

app = Flask(__name__)
wordleSolver = WordleSolver()
CORS(app)

@app.route('/initSolver',methods=['GET'])
def initSolver():
    # recreate obj just in case
    wordleSolver = WordleSolver()
    
    wordleSolver.initGuessList()
    recommendedGuess = wordleSolver.calcSuggestedGuess()
    
    response_body = {
        "wordList" : wordleSolver.getGuessList(),
        "recommendedGuess" : recommendedGuess
    }
    
    return response_body

if __name__ == '__main__':
    app.run(debug=True)