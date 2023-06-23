import chalk from "chalk";
import { len_of } from "./str_utils.js";
import { get_text } from "./io_utils.js";


export function red_text(text, bold = false){
    if(bold){
        return chalk.redBright(text)
    }
    return chalk.red(text)
}


export function blue_text(text, bold = false){
    if(bold){
        return chalk.blueBright(text)
    }
    return chalk.blue(text)
}

export function green_text(text, bold = false){
    if(bold){
        return chalk.greenBright(text)
    }
    return chalk.green(text)
}


export function yellow_text(text, bold = false){
    if(bold){
        return chalk.yellowBright(text)
    }
    return chalk.yellow(text)
}


export function progress_bar(valor_atual, valor_fim){
    let _label = ` + ${(valor_atual/valor_fim * 100).toFixed(2)}%`
    let _current_value = Math.floor(valor_atual / 10)
    let _final_value = 10
    let _loaded = '#'.repeat(_current_value)
    if (_current_value < 4){
        _loaded = red_text(_loaded)
    }
    else if(_current_value < 6){
        _loaded = yellow_text(_loaded)
    }
    else if(_current_value === 10){
        _loaded = green_text(_loaded, true)
        _label = 'COMPLETED'
    }
    else{
        _loaded = green_text(_loaded)
    }
    let _blank = ' '.repeat(_final_value - _current_value)
    let _current_state = `[${_loaded + _blank}] (${_label})`
    console.log(_current_state) 
    }


export function COLOrFuL(text){
    let new_text = ''
    let colors = [red_text, green_text, blue_text]
    let index;
    for(let i = 0; i < len_of(text); i++){
        index = i % colors.length
        new_text += colors[index](text[i], true)
    }
    return new_text
}

export function enter_to_continue(){
    get_text('<ENTER>...')
    clear_screen()
}

export function clear_screen(){
    console.clear()
}
