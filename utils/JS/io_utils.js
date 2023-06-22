import { question } from "readline-sync";
import { len_of } from "./str_utils.js";

export function get_integer(label ='Digite um inteiro: ', type=undefined){
    const num = Number(question(label))

    if(!is_number(num)){
        return get_integer(label = 'Não é um número: ', type)
    }

    if(type === '+'){
        if (num < 0){
            return get_integer(label='Digite um número positivo!: ', type)
        }
        return num
    }
    else if(type === '-'){
        if(num > 0){
            return get_integer(label='Digite um número negativo!: ', type)
        }
        return num
    }else{
        return num
    }
}

export function loading_bar(valor_inicio, valor_fim, async = true){
    if (async){
        while(valor_inicio <= valor_fim){
            let _current_value = Math.floor(valor_inicio / 10)
            let _final_value = Math.floor(valor_fim / 10)
            let _loaded = '#'.repeat(_current_value)
            let _blank = ' '.repeat(_final_value - _current_value)
            let _current_state = `[${_loaded + _blank}]${_current_value}/${_current_value - _final_value}`
            valor_inicio ++
            console.log(_current_state) 
            }
    }else{
        let _current_value = Math.floor(valor_inicio / 10)
        let _final_value = Math.floor(valor_fim / 10)
        let _loaded = '#'.repeat(_current_value)
        let _blank = ' '.repeat(_final_value - _current_value)
        let _current_state = `[${_loaded + _blank}]${_current_value}/${_current_value - _final_value}`
        valor_inicio ++
        console.log(_current_state)
    }
}


export function get_text(label, max_limit = undefined){
    const input = question(label)
    if(!max_limit){
        return input
    }
    return len_of(input) > max_limit? get_text(label = `No máximo(${max_limit}): `, max_limit) : input

}


export function show_text(text){
    console.log(text)
}

// Check Functions
const is_number = x => x * 0 === 0
