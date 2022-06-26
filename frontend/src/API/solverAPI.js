import axios from "axios";

export async function initSolver(){
    try{
        return await axios.get("initSolver");
    }catch(e){
        return null;
    }
}

export async function processFeedback(guess,feedback){
    try{
        return await axios.get("processFeedback/" + guess + "/" + feedback);
    }catch(e){
        return null;
    }
}

export async function solveForWord(correctWord){
    try{
        return await axios.get("solveForWord/" + correctWord);
    }catch(e){
        return null;
    }
}