"""
Python wordle solver functions
This program contains the class for handling solving the wordle
Author : Andrew Ammentorp
"""

# the frequency of each letter  
# Materials provided by https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html          
letterFreqs = {
    'e' : 56.88,
    'a' : 43.31,
    'r' : 38.64,
    'i' : 38.45,
    'o' : 36.51,
    't' : 35.43,
    'n' : 33.92,
    's' : 29.23,
    'l' : 27.98,
    'c' : 23.13,
    'u' : 18.51,
    'd' : 17.25,
    'p' : 16.14,
    'm' : 15.36,
    'h' : 15.31,
    'g' : 12.59,
    'b' : 10.56,
    'f' : 9.24,
    'y' : 9.06,
    'w' : 6.57,
    'k' : 5.61,
    'v' : 5.13,
    'x' : 1.48,
    'z' : 1.39,
    'j' : 1.00,
    'q' : 1
}

# freq of each letter in each position, start, medial, and final
# http://www.viviancook.uk/SpellStats/LetFreqByWordPosition.html
posFreqs = {
    'e' : [2.12,13.35,19.75],
    'a' : [11.56,8.85,2.73],
    'r' : [1.96,6.91,6.06],
    'i' : [6.63,9.21,0.97],
    'o' : [6.30,9.11,4.60],
    't' : [15.14,6.53,10.03],
    'n' : [2.15,8.49,7.87],
    's' : [7.59,4.19,11.50],
    'l' : [3.12,5.10,2.88],
    'c' : [4.04,3.00,0.28],
    'u' : [1.24,4.17,1.00],
    'd' : [2.79,2.09,11.75],
    'p' : [2.95,1.76,0.87],
    'm' : [3.84,2.12,1.98],
    'h' : [7.72,6.77,2.57],
    'g' : [1.90,1.97,3.50],
    'b' : [4.34,0.86,0.09],
    'f' : [3.90,1.08,3.54],
    'y' : [1.62,0.70,5.51],
    'w' : [6.96,1.05,1.13],
    'k' : [0.65,0.84,1.28],
    'v' : [0.58,1.34,0.02],
    'x' : [0.01,0.26,0.08],
    'z' : [0.01,0.09,0.01],
    'j' : [0.60,0.09,0.01],
    'q' : [0.25,0.08,0.01] 
}

"""
Class for handling the wordle solver
"""
class WordleSolver:
    """
    Constructor
    """
    def __init__(self):
        self.guess_list = []
        self.pastGuesses = []
        self.guesses = 0
        
    """
    Loads up the word pool
    """
    def initGuessList(self):
        try:
            with open('validWordleWords.txt') as f:
                for line in f:
                    theWord = line.strip().lower()
                    # only add if word is only letters and length of 5
                    if self.validateGuess(theWord) and not theWord in self.guess_list:
                        self.guess_list.append(theWord)
        except FileNotFoundError:
            print("file not found")
            exit(1)
    """
    Gets a copy of the guess list
    """
    def getGuessList(self):
        return self.guess_list.copy()
    """
    Removes a word from the word pool
    """
    def removeWord(self,word):
        self.guess_list.remove(word)
    
    """
    Process feedback based on guess and feedback
    (aka updates the word pool
    """
    def processFeedback(self,guess,feedback):
        self.pastGuesses.append(guess)
        if feedback == "ggggg":
            try:
                with open('log.csv',"a") as f:
                    print("Congrats it took " + str(self.guesses+1) + " guesses to guess " + guess + "\n" + str(self.pastGuesses))
                    f.write(guess + "," + str(self.guesses+1) + "," + str(self.pastGuesses) + "\n")
                    exit(0)
            except FileNotFoundError:
                print("file not found")
                exit(1)
            
        else:    
            self.guesses += 1
            
            temp_tuple = tuple(self.guess_list)
            # for each word in the potential word bank
            for word in temp_tuple: # You can't iterate over a list you want to change, so using a tuple.
                # for each letter in your guess/feedback
                for i in range(len(guess)):
                
                    # if correct does not have guess letter and word has letter
                    if feedback[i] == "w" and guess[i] in word:
                        self.removeWord(word)
                        break
                    
                    # if correct letter and spot but dict word does not have said letter at spot
                    elif feedback[i] == "g" and guess[i] != word[i]:
                        self.removeWord(word)
                        break
                        
                    # if word contains letter and dict word does not have letter at all
                    elif feedback[i] == "y" and guess[i] not in word:
                        self.removeWord(word)
                        break
                        
                    # if word contains letter and dict word has letter at that spot
                    elif feedback[i] == "y" and guess[i] == word[i]:
                        self.removeWord(word)
                        break
    """
    This function takes a guess and makes sure it's valid
    @param guess the user's guess
    @returns Boolean if guess is valid
    """
    def validateGuess(self,guess):
        if len(guess) != 5:
            return False
            
        for char in guess:
            if ord(char) < 97 or ord(char) > 122:
                return False
        return True

    """
    This function take the wordle feedback and says if valid
    @param feedback the user's feedback
    @returns Boolean if feedback is valid
    """
    def validateFeedback(self,feedback):
        if len(feedback) != 5:
            return False
            
        for char in feedback:
            if char != 'g' and char != 'y' and char != 'w':
                return False
        return True
    
    """
    Gets a letter's position frequency
    """
    def getPositionFreq(self,char,posInWord):
        # get letter
        # using dict pass in index
        #print(char,posFreqs[char][posInWord])
        return posFreqs[char][posInWord]

    """
    This function calculates a suggested guess based on your feedback and the word bank
    @param guess_list the available word list pool
    @returns a suggested guess
    """    
    def calcSuggestedGuess(self):
        # empty word pool
        if len(self.guess_list) <= 0:
            return "N/A - error"
            
        # if len is 1 just return that word - no need to calculate stuff
        if len(self.guess_list) == 1:
            return self.guess_list[0]
        
        # get max score based on word freqs
        maxGuessScore = 0
        suggestedGuess = ""
        
        # for each guess
        for guess in self.guess_list:
            guessScore = 0
            
            lettersInWord = []
            lettersInGuess = []
            index = 0
            posInWord = 0 # 0 for start , 1 for medial, 2 for final
            # get its freq score
            for char in guess:
                if not char in lettersInWord and not char in lettersInGuess:
                    guessScore = guessScore + (letterFreqs[char] * self.getPositionFreq(char,posInWord))
                    lettersInWord.append(char)
                    lettersInGuess.append(char)
                else:
                    # TODO give some points for being a repeat letter (like if its an e or something I guess)
                    if char == 'e' or char == 'a' or char == 't' or char == 's' or char == 'o':
                        guessScore = guessScore + (letterFreqs[char] * self.getPositionFreq(char,posInWord) / 5)
                    else:
                        guessScore += 0
                    
                index += 1
                if index == 0:
                    posInWord = 0
                if index >= 1 and index <= 3:
                    posInWord = 1
                if index >= 4:
                    posInWord = 2
            
            # TODO what about a tie(?)
            if guessScore > maxGuessScore:
                maxGuessScore = guessScore
                suggestedGuess = guess
        
        return suggestedGuess
    
    """
    Calculates feedback based on the correct word
    """
    def calcFeedback(self,guess,correctWord):
        feedback = ""
        
        for i in range(len(guess)):
            if guess[i] == correctWord[i]:
                feedback += "g"
            elif guess[i] in correctWord and guess[i] != correctWord[i]:
                feedback += "y"
            elif guess[i] not in correctWord:
                feedback += "w"
            else:
                feedback += "w"
        
        return feedback





    
    
