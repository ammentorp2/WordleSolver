import React from 'react';
import { Typography } from "@mui/material"
import {WordleSolver} from '../components/WordleSolver'
import { Header } from '../components/Header';

export const Solver = () => {
    return(
        <div>
            <Header />
            <WordleSolver></WordleSolver>
        </div>
    )
}