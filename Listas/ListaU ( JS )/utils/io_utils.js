import { question } from "readline-sync";
import { len_of } from "./str_utils.js";
import {red_text, yellow_text, green_text, blue_text} from "./visual_utils.js"
import { is_in } from "./vetor_utils.js";


export function get_integer(label='Digite um inteiro: ', type=undefined){
    let num = question(label) 
    while(!num){
        num = question(label= 'Digite novamente: ') 
    }
    num = Number(num)

    // Fail Fasts: Checagens antes da execução do problema ("Pare logo")
    if(is_number(num) == false){
        // Checa se é numero
        return get_integer(red_text(label = 'Digite novamente: ', true), type)
    }

    if(num != Math.floor(num)){
        //Checa se é inteiro
        return get_integer(red_text(label = 'Digite um número inteiro: '))
    }
    if(type === '+'){
        // Checa se é positivo
        if (num < 0){
            return get_integer(red_text(label='Digite um número positivo!: '), type)
        }
        return num
    }
    else if(type === '-'){
        // Checa se é negativo
        if(num > 0){
            return get_integer(red_text(label='Digite um número negativo!: '), type)
        }return num
    }else{
        return num
    }
}

export function get_number(label='Digite um inteiro: ', type=undefined){
    let num = question(label) 
    while(!num){
        num = question(label= 'Digite novamente: ') 
    }
    num = Number(num)

    // Fail Fasts: Checagens antes da execução do problema ("Pare logo")
    if(is_number(num) == false){
        // Checa se é numero
        return get_number(red_text(label = 'Digite novamente: ', true), type)
    }

    if(type === '+'){
        // Checa se é positivo
        if (num < 0){
            return get_number(red_text(label='Digite um número positivo!: '), type)
        }
        return num
    }
    else if(type === '-'){
        // Checa se é negativo
        if(num > 0){
            return get_number(red_text(label='Digite um número negativo!: '), type)
        }return num
    }else{
        return num
    }
}


export function get_integer_interval(label= 'Digite um inteiro: ', min, max){
    let num = get_integer(label)
    if(num < min || num > max){
        return get_integer_interval(yellow_text(label=`Digite um número no intervalo[${min},${max}]: `), min, max)
    }else{
        return num
    }
}


export function delay(msecs){
    return new Promise(resolve => setTimeout(resolve, msecs))
}


export function get_text(label="Digite o texto:", max_limit = undefined){
    let input = question(label)
    if(!max_limit){
        return input
    }
    return len_of(input) > max_limit? get_text(label = `No máximo(${max_limit}): `, max_limit) : input

}


export function show_text(text, color){
    if(!color){
        console.log(text)
    }
    else if(color === 'R'){
        console.log(red_text(text))
    }
    else if(color === 'B'){
        console.log(blue_text(text))
    }
    else if(color === 'G'){
        console.log(green_text(text))
    }
}


export function get_vetor(label, tamanho, intervalo_num_min, intervalo_num_max, inline=false){
    let out = []
    if (!inline) {
    for (let i = 0; i < tamanho; i++) {
        show_text(label)
        const num = get_integer_interval(`Digite o a posição ${i}`, intervalo_num_min, intervalo_num_max)
        out.push(num)
    }
    return out
    }
    const nuns = get_text('Digite os números na linha: ')
    out = nuns.split(' ')
    while(out.length !== tamanho){
        show_text(`Digite ${tamanho} numeros!`)
        const nuns = get_text('Digite os números na linha: ')
        out = nuns.split(' ')
    }
    return out
 }



 export function get_random_array(length, min_limit, max_limit, repeats = false){
    const out = []
    if (!repeats) {
        let number;
        while(out.length < length){
            number = get_random_number_between(min_limit, max_limit)
            if (!(is_in(number, out))) {
                out.push(number)
            }
        }
        return out
    }
    while (out.length < length){
        out.push(number)
    }
    return out

}


export function get_random_number_between(min, max){
    return Math.floor(Math.random() * (max - min) + min)

}


// Check Functions
const is_number = x => x * 0 === 0
