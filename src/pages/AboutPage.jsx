import React from 'react';
import { Button, Grid, MenuItem, Select, TextField, Typography } from "@mui/material"
import { useNavigate } from "react-router-dom";
import { Header } from '../components/Header';
import { Collapse } from '@mui/material';

export const AboutPage = () => {
    return(
        <div>
            <Header />
            <Grid container justifyContent="center" direction={'column'} spacing={5}>
                <Grid item>
                    <Typography variant="h4">
                        How does the app work?
                    </Typography>
                    <Typography paragraph>
                        This app was made with a ReactJS frontend (using create-react-app) and Python Flask endpoints.
                        From there, the server was seperated from the frontend and each were deployed using Heroku. 
                    </Typography>
                </Grid>
                <Grid item>
                    <Typography variant="h4">
                        App history
                    </Typography>
                    <Typography paragraph>
                        Originally, I just just made this as a python console app inspired by (https://replit.com/@jamesabela/WordleSolver).
                        Quickly I wanted the program to calculate a suggested guess based on the available words. 
                        But how can one quantify that? The initial way
                        I calculated this by assigning each word a "score" , if the letter hadn't appeared in the word add its
                        frequency score (found here: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html). 
                        Then, the word with the highest score would become the sugested guess.
                        From there, I created functionality that given the correct word would solve the word (aka always using 
                        the suggested guess). After that I expanded upon the formula, not only factoring in how often the word appears,
                        but how often it appears <i>in each position in the word</i>   
                        (http://www.viviancook.uk/SpellStats/LetFreqByWordPosition.html). For example, using the old 
                        formula <b>Irate</b> was the suggested first guess. While containing common letters, not many words start with 'I' 
                         (relatively speaking).
                        Thus factoring in the start,middle, and medial positions of each letter <b>Trine</b> is new first suggested guess.
                    </Typography>
                </Grid>
                <Grid item>
                    <Typography variant="h4">
                        Future tasks
                    </Typography>
                    <Typography paragraph>
                        <ul>
                            <li>Factor in common two/three letter combinations, such as st,str,pl etc</li>
                            <li>
                                The edge case of only one missing letter. For example my auto solver takes 7 guesses to solve for "rakes".
                                Looking at its past guesses it guesses 4 words before getting the 'k' correct. Finding a different word
                                to guess that uses multiple unused letters to find which one is in the word seems to be the better
                                strategy.
                            </li>
                        </ul>
                    </Typography>
                </Grid>
            </Grid>
        </div>
    )
}