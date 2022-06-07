"""
    This function takes a guess and makes sure it's valid
    @param guess the user's guess
    @returns Boolean if guess is valid
"""
def validateGuess(guess):
    if len(guess) != 5:
        return False
        
    for char in guess:
        if ord(char) < 97 or ord(char) > 122:
            return False
    return True
    
# main method protection
if __name__ == '__main__':
    # open the wordlist file
    # this uses the linux dictionary (words)
    try:
        with open('words.txt') as f:
            for line in f:
                theWord = line.strip().lower()
                # only add if word is only letters and length of 5
                if validateGuess(theWord):
                    with open('validWordleWords.txt','a') as w:
                        w.write(theWord + "\n")
    except FileNotFoundError:
        print("file not found")
        exit(1)