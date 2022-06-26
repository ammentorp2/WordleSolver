import React from 'react';
import { useState } from 'react';
import { Button, Grid, Box, TextField, Typography } from "@mui/material"
import { initSolver,solveForWord } from '../API/solverAPI';

export const WordleSolverTester = () => {
    const [mounted,setMounted] = useState(false);
    const [targetWord,setTargetWord] = useState("");
    const [wordSubmitted,setWordSubmitted] = useState(false);

    const [pastGuesses,setPastGuesses] = useState([]);
    const [pastFeedbacks,setPastFeedbacks] = useState([]);

    if(!mounted){
        //init backend wordlist
        //get recomended guess
        try{
            initSolver().then((response) => {
                console.log(response)
                if(response !== null && response.status === 200){
                    setMounted(true);
                }
                else{
                    console.log("Error initializing solver - bad response")
                }
            });
        } catch(e){
            console.log("Error initializing solver")
        }
        
    }

    const handleSolveWord = () => {
        try{
            solveForWord(targetWord).then((response) => {
                if(response !== null && response.status === 200){
                    if(response.data.status === 1){
                        alert("Word not in dictionary!")
                    }
                    else if(response.data.status === 0){
                        setWordSubmitted(true)
                        setPastFeedbacks(response.data.pastFeedbacks);
                        setPastGuesses(response.data.pastGuesses);
                    }
                }
                else{
                    console.log("Error solving for word")
                }
            })
        } catch(e){
            console.log("Error solving for word")
        }
    }

    const calcPastFeedbackColor = (wordIndex,letterIndex) => {
        if(pastFeedbacks !== undefined){
            switch(pastFeedbacks[wordIndex][letterIndex]){
                case 'w' : return 'black';
                case 'g' : return 'green';
                case 'y' : return 'yellow';
                default: return 'black';
            }
        }
        
    }

    const renderPastFeedbacks = () => {
        let output = [];

        if(pastGuesses.length > 0){
            
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
        }
    
        return output;
        
    }

    const handleSolveAgain = () => {
        setPastFeedbacks([])
        setPastGuesses([])
        setTargetWord("")
        setWordSubmitted(false);
    }

    return(
        <div>
            {mounted ? 
                <Grid container direction={'column'} spacing={5}>
                    <Grid item>
                        <header>
                            Wordle Solver
                        </header>
                    </Grid>
                    <Grid item>
                        Word to solve for: <TextField inputProps={{ maxLength: 5 }} required 
                                                onChange={e => {setTargetWord(e.target.value)}} disabled={wordSubmitted}>
                                                    {targetWord}
                                            </TextField>
                    </Grid>
                    <Grid item>
                        <Button variant="outlined" onClick={handleSolveWord} disabled={wordSubmitted}>
                            Solve for word
                        </Button>
                    </Grid>
                    <Grid item>
                        {
                            renderPastFeedbacks()
                        }
                    </Grid>
                    <Grid item >
                        <Button variant="outlined" onClick={handleSolveAgain} disabled={!wordSubmitted}>
                            Solve for another word
                        </Button>
                    </Grid>
                </Grid>

                : 
                <div> Loading... </div>
            }
        </div>
    )
}