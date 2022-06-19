import React from 'react';
import { Button, Grid, MenuItem, Select, TextField } from "@mui/material"
import { useNavigate } from "react-router-dom";

export const HomePage = () => {
    let navigate = useNavigate();

    const handleGoToSolve = () => {
        navigate('solve')
    }

    return (
        <div>
            <Grid>
                <Grid item textAlign={true}>
                    The Girth
                </Grid>
                <Grid item>
                    <Button onClick={handleGoToSolve}>
                        Wordle Solver
                    </Button>
                </Grid>
                <Grid item>
                    <Button>
                        Tester
                    </Button>
                </Grid>
                <Grid item>
                    <Button>
                        About
                    </Button>
                </Grid>
            </Grid>
        </div>
    )
}