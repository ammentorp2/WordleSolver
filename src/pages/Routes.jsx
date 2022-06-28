import React from 'react';
import { Route , Routes} from 'react-router-dom';
import { HomePage } from './HomePage';
import { Solver } from './Solver';
import { Tester } from './Tester';

export const PageRoutes = () => {
    return(
        <Routes>
            <Route path='/' element={<HomePage />} />
            <Route path='/solve' element={<Solver />} />
            <Route path='/test' element={<Tester />} />
        </Routes>
        
    )
}