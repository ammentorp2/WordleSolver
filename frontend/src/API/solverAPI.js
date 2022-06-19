import axios from "axios";

export async function initSolver(){
    try{
        return await axios.get("initSolver");
    }catch(e){
        return null;
    }
}