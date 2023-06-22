import { question } from "readline-sync";

export function len_of(iterable){
    let count = 0
    for(let item of iterable){
        count ++
    }
    return count
}