import React from 'react';
import { useState } from 'react';
import { Button, Grid, Box, TextField, Typography,Tooltip ,IconButton  } from "@mui/material"
import HelpIcon  from '@mui/icons-material/Help';
import { initSolver, processFeedback } from '../API/solverAPI';

// user wordle solver
export const WordleSolver = () => {
    // to init some things
    const [mounted,setMounted] = useState(false);
    // number of guesses used
    const [guesses,setGuesses] = useState(0);
    // current guess
    const [guess,setGuess] = useState("guess");
    // feedback on guess
    const [feedback,setFeedback] = useState("wwwww");

    const [pastGuesses,setPastGuesses] = useState([]);
    const [pastFeedbacks,setPastFeedbacks] = useState([]);
    
    const [availableWords,setAvailableWords] = useState([]);
    const [recommendedGuess,setRecommendedGuess] = useState("");

    const [showWordList,setShowWordList] = useState(false);
    const [showRecommendedGuess,setShowRecommendedGuess] = useState(false);

    const [solved,setSolved] = useState(false);

    if(!mounted){
        //init backend wordlist
        //get recomended guess
        try{
            initSolver().then((response) => {
                if(response !== null && response.status === 200){
                    setAvailableWords(response.data.wordList.sort());
                    setRecommendedGuess(response.data.recommendedGuess)
                    setMounted(true);
                    setSolved(false);
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
        //make api request to validate word (if in dict) and then process feedback
        //console.log(guess,feedback,recommendedGuess);

        if(guess.length < 5){
            alert("Guess needs to be 5 characters!")
            return;
        }


        let newGuesses = [...pastGuesses];
        let newFeedbacks = [...pastFeedbacks];

        newGuesses.push(guess);
        newFeedbacks.push(feedback);

        // add to past guesses and feedbacks
        setPastGuesses(newGuesses);
        setPastFeedbacks(newFeedbacks);

        //hide before making request
        setShowRecommendedGuess(false);
        setShowWordList(false);


        try{
            processFeedback(guess.toLowerCase(),feedback).then((response) => {
                if(response !== null && response.status === 200){
                    // word not in dict
                    if(response.data.status === 2){
                        alert("Word not in dictionary. Try again")
                        setGuess('guess')
                        setFeedback("wwwww")
                        setPastGuesses(pastGuesses.splice(-1))
                        setPastFeedbacks(pastFeedbacks.splice(-1))
                    }
                    // solved
                    else if(response.data.status === 0){
                        //congrats
                        //TODO render congrats page or graphic thing
                        setSolved(true);
                    }
                    // valid word, but not correct
                    else if(response.data.status === 1){
                        setAvailableWords(response.data.wordList);
                        setRecommendedGuess(response.data.recommendedGuess)
                        setGuesses(guesses + 1)
                        setGuess('')
                        setFeedback("wwwww")
                    }

                    
                }
                else{
                    console.log("Error with response")
                }
            })
        } catch(e){
            console.log("Error with response")
        }

        
    }

    const handleShowHideWords = () => {
        setShowWordList(!showWordList)
    }

    const handleShowHideRecommendedGuess = () => {
        setShowRecommendedGuess(!showRecommendedGuess)
    }

    //determine color of text
    const calcFeedbackColor = (index) => {
        switch(feedback[index]){
            case 'w' : return 'black';
            case 'g' : return 'green';
            case 'y' : return 'yellow';
            default: return 'black';
        }
    }

    //determine color of text
    const calcPastFeedbackColor = (wordIndex,letterIndex) => {
        switch(pastFeedbacks[wordIndex][letterIndex]){
            case 'w' : return 'black';
            case 'g' : return 'green';
            case 'y' : return 'yellow';
            default: return 'black';
        }
    }

    // changes feedback
    function updateFeedback(index) {
        let newFeedback = "";

        for(let i = 0; i < feedback.length; i++){
            if(i === index){
                switch(feedback[index]){
                    case 'w': newFeedback += 'y'; break;
                    case 'g': newFeedback += 'w'; break;
                    case 'y' : newFeedback += 'g'; break;
                    default : newFeedback += 'w';
                }
            }
            else{
                newFeedback += feedback[i];
            }
        }

        setFeedback(newFeedback);
    }

    const renderFeedback = () => {
        let output = [];
        for(let i = 0; i < guess.length; i++){
            output.push(
            <Box sx={{ 
                width : 'auto',
                p : 1,}}
                component="span"
                id={i}
                >
                <Button id={i} variant="outlined" sx={{color:'gray',backgroundColor:calcFeedbackColor(i)}}
                    onClick={() => updateFeedback(i)}>
                    {guess[i]}
                </Button>
                
            </Box>
            );
        }

        return output;
    }

    const renderPastFeedbacks = () => {
        let output = [];
        for(let i = 0; i < pastGuesses.length; i++){
            for(let j = 0; j < pastGuesses[i].length; j++){

                output.push(
                    <Box sx={{ 
                        width : 'auto',
                        p : 1,}}
                        component="span"
                        id={j}
                        >
                        <Button id={j} variant="outlined" sx={{color:'gray',backgroundColor:calcPastFeedbackColor(i,j)}}
                        >
                            {pastGuesses[i][j]}
                        </Button>
                        
                    </Box>
                    );
            }
            output.push(<div></div>)
            
        }

        return output;
    }

    return(
        <div>
        {mounted ?
            solved ?
                <div>
                    Congrats!
                </div>
            :
            <div>
            <Grid container direction={'column'} spacing={5}>
                <Grid item>
                    <Typography>Guess Number : {guesses + 1}</Typography>
                </Grid>
                <Grid item>
                    <Typography>Guess:</Typography> 
                    <TextField inputProps={{ maxLength: 5 }} required onChange={e => {setGuess(e.target.value)}} placeholder="guess">
                        {guess}
                    </TextField>
                </Grid>
                <Grid item>
                    Feedback on word (from Wordle): 
                    <Tooltip title="Click on a letter to cycle between the feedbacks from Wordle: black, yellow, and green">
                        <IconButton>
                            <HelpIcon />
                        </IconButton>
                    </Tooltip>
                    <Grid container direction={'colummn'} spacing={2}>
                        <Grid item>
                        {
                            renderPastFeedbacks()
                        }
                        {
                            renderFeedback()
                        }
                        </Grid>
                    </Grid>

                </Grid>
                <Grid item>
                    <Button variant="contained" onClick={handleShowHideRecommendedGuess}>
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
                    <Button variant="contained" onClick={handleShowHideWords}>
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
                <Grid item>
                    <Button variant="contained" color="success" onClick={handleSubmitGuess}>
                        Submit Guess
                    </Button>
                </Grid>
            </Grid>
        </div>
            :
            <div>loading...</div>
        }
        </div>
    )
}