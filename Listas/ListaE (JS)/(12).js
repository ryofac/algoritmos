import { question } from "readline-sync";
import { question } from "readline-sync";

function main(){
    const num1 = Number(question('Digite o número a ser verificado: '))
    if(eh_impar(num1)){
        console.log('Ele é ímpar!')
    }
    else{
        console.log('Ele é par!')
    }



function eh_impar(numero){
   return numero % 2
}
}
main()