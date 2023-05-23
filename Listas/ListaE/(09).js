import { question } from "readline-sync";

function main(){
    const num1 = Number(question('Digite o primeiro número: '))
    if(eh_primo(num1)){
        console.log('Ele é primo!')
    }
    else{
        console.log('Ele não é primo!')
    }



function eh_primo(numero){
    var cont = 0
    for (var i = 1; i <= numero; i ++){
        if(numero % i == 0){
            cont ++
        }
    }
    return cont <= 2

    }
}
main()