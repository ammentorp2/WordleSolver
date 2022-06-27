import React from 'react';
import { Typography } from "@mui/material"
import { WordleSolverTester } from '../components/WordleSolverTester';
import { Header } from '../components/Header';

export const Tester = () => {
    return(
        <div>
            <Header />
            <WordleSolverTester />
        </div>
    )
}