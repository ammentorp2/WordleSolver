import React from 'react';
import { Button, Grid, MenuItem, Select, TextField, Typography } from "@mui/material"
import { useNavigate } from "react-router-dom";
import { Header } from '../components/Header';

export const HomePage = () => {
    let navigate = useNavigate();

    const handleGoToSolve = () => {
        navigate('solve')
    }

    const handleGoToTest = () => {
        navigate('test')
    }

    return (
        <div>
            <Header />
            <Grid container justifyContent="center" direction={'column'} spacing={5}>
                <Grid item>
                    <Typography paragraph variant="body1">
                        Welcome to the Ammentorp Wordle Solver! Wordle is an super popular site, so I thought it would be
                        a fun challenge to create an application to help users as well as automatically attempt to solve it.
                    </Typography>
                </Grid>
                <Grid item>
                    <Button variant="contained" onClick={handleGoToSolve}>
                        Access the Wordle Solver
                    </Button>
                </Grid>
                <Grid item>
                    <Button variant="contained" onClick={handleGoToTest}>
                        Auto-Solve for a word
                    </Button>
                </Grid>
            </Grid>
        </div>
    )
}