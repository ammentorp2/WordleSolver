import React from 'react';
import { useState } from 'react';
import { Button, Grid, MenuItem, Select, TextField, Typography } from "@mui/material"
import { initSolver } from '../API/solverAPI';

export const WordleSolver = () => {
    const [mounted,setMounted] = useState(false);
    const [guesses,setGuesses] = useState(0);
    const [guess,setGuess] = useState("");
    const [feedback,setFeedback] = useState("");
    
    const [availableWords,setAvailableWords] = useState([]);
    const [recommendedGuess,setRecommendedGuess] = useState("");

    const [showWordList,setShowWordList] = useState(false);
    const [showRecommendedGuess,setShowRecommendedGuess] = useState(false);

    if(!mounted){
        //init backend wordlist
        //get recomended guess
        try{
            initSolver().then((response) => {
                if(response !== null && response.status === 200){
                    setAvailableWords(response.data.wordList);
                    setRecommendedGuess(response.data.recommendedGuess)
                    setMounted(true);
                }
                else{
                    console.log("Error initializing solver")
                }
            });
        } catch(e){
            console.log("Error initializing solver")
        }
        
    }

    const handleSubmitGuess = () => {
        //make api request to validate word and feedback and then process feedback
        console.log(guess,feedback,recommendedGuess);

        //hide before making request
        setShowRecommendedGuess(false);
        setShowWordList(false);



        setGuesses(guesses + 1)
    }

    const handleShowHideWords = () => {
        setShowWordList(!showWordList)
    }

    const handleShowHideRecommendedGuess = () => {
        setShowRecommendedGuess(!showRecommendedGuess)
    }

    return(
        <div>
        {mounted ?  
            <div>
            <Grid>
                <Grid item>
                    <header>
                        Wordle Solver
                    </header>
                </Grid>
                <Grid item>
                    Guess Number : {guesses + 1}
                </Grid>
                <Grid item>
                    Guess: <TextField onChange={e => {setGuess(e.target.value)}}>{guess}</TextField>
                </Grid>
                <Grid item>
                    Feedback: <TextField onChange={e => {setFeedback(e.target.value)}}>{feedback}</TextField>
                </Grid>
                <Grid item>
                    <Button onClick={handleSubmitGuess}>
                        Submit
                    </Button>
                </Grid>
                <Grid item>
                    <Button onClick={handleShowHideRecommendedGuess}>
                        Show/Hide Suggested Guess
                    </Button>
                    {
                        showRecommendedGuess ?
                            <Typography>{recommendedGuess}</Typography>
                        :
                        null
                    }
                </Grid>
                <Grid item>
                    <Button onClick={handleShowHideWords}>
                        Show/Hide Available Words
                    </Button>
                    {
                        showWordList ? 
                        availableWords.map(a => (
                            <Typography key={a}>{a}</Typography>
                        ))
                        :
                        null
                    }
                </Grid>
            </Grid>
        </div>
            :
            <div>loading...</div>
        }
        </div>
    )
}