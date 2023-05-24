import { question } from "readline-sync";

function main(){
    const date = question('Digite uma data no formato DD/MM/AAAA: ')
    if (eh_data_valida(date)){
        console.log("É uma data válida")
    }else{
        console.log('É uma data inválida!')
    }

function eh_data_valida(data){
    return data.lenght < 11 || eh_numero(date.slice(0,2)) && eh_numero(date.slice(3,5)) &&
    eh_numero(date.slice(6,))
}
function eh_numero(num){
    return num * 0 == 0
}
}
main()