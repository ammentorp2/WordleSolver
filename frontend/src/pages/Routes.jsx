import React from 'react';
import { Route , Routes} from 'react-router-dom';
import { HomePage } from './HomePage';

export const PageRoutes = () => {
    return(
        <Routes>
            <Route path='/' element={<HomePage />} />
        </Routes>
        
    )
}