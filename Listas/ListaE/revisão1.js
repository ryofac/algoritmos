import { question } from "readline-sync";
function main(){
    const number1 = question('Digite o número: ')
    if(!isNumber(number1)){ // fail fast
        console.log('Digite um valor válido! ')
        return
    }
    if (number1 == 0){
        console.log('É igual a zero')
    }
    else if(isNegative(number1)){
        console.log('É um número negativo')
    }
    else{
        console.log('É um número positivo')
    }
}

function isNegative(number){
    return number < 0
}

function isNumber(value){
    return value * 0 == 0 // Para verificar se é número, analisa se o valor x 0 é igual a 0
}
main()