/**
 * This file handles the API calls to the wordle solver
 */

import axios from "axios";

/**
 * 
 * @returns word list and suggested guess
 */
export async function initSolver(){
    try{
        return await axios.get("initSolver");
    }catch(e){
        return null;
    }
}

/**
 * 
 * @param {*} guess user's guess
 * @param {*} feedback feedback on guess
 * @returns (new) word list and (new) suggested guess
 */
export async function processFeedback(guess,feedback){
    try{
        return await axios.get("processFeedback/" + guess + "/" + feedback);
    }catch(e){
        return null;
    }
}

/**
 * 
 * @param {*} correctWord word to solve for
 * @returns guesses used and their feedbacks
 */
export async function solveForWord(correctWord){
    try{
        return await axios.get("solveForWord/" + correctWord);
    }catch(e){
        return null;
    }
}