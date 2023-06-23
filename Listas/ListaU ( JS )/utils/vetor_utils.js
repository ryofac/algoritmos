import { show_text } from "./io_utils.js";

export function my_map(array, map_function, string = false){
    let out
    if(!string){
         out = [];
    }else{
        out = ''
    }for(let i = 0; i < array.length; i ++){
        !string? out.push(map_function(array[i])) : out += map_function(array[i])
    }
    return out
}

export function my_filter(array, filter_function){
    const out = [];
    for(let i = 0; i < array.length; i ++){
        if(filter_function(array[i])){
            out.push(array[i]);
        }
    }
    return out
}

export function is_in(element, array){
    for (let i = 0; i < array.length; i ++) {
        if (array[i] === element) {
            return true
        }
    }
    return false
}

export function string_vetor(array){
    let itens = '[ '
    for(let item of array){
        itens += `${item}, `
    }
    itens += ']'
    return itens
}

export function count_elements_between(array1, array2){
    let count = 0
    for(let element of array1){
        for(let element2 of array2){
            if(element === element2) count += 1
        }
    }
    return count
}

export function eh_objeto_vazio(obj){
    let empty_count = 0
    let element_count = 0
    for (let item of Object.keys(obj)){
        element_count += 1
        if(!obj[item] || obj[item].length <= 0) empty_count += 1
    }
    return empty_count === element_count
}
