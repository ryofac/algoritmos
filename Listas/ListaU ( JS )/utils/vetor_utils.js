export function my_map(array, map_function){
    const out = [];
    for(let i = 0; i < array.length; i ++){
        out.push(map_function(array[i]));
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
    console.log(array)
    for (let i = 0; i < array.length; i ++) {
        if (array[i] === element) {
            return true
        }
    }
    return false
}