import { show_text, get_integer, get_text } from "./io_utils.js";
import { len_of } from "./str_utils.js";
import {COLOrFuL} from "./visual_utils.js"

async function main(){
    const text = get_text('Digite um texto e veja a mágica ocorrer! \n> ')
    show_text('O seu texto: ' + COLOrFuL(text))
}
main()