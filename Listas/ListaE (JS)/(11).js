import { question } from "readline-sync";

function main(){
    // entrada
    const num1 = Number(question('Digite um número: '))
    const num2 = Number(question('Digite um número: '))
    const num3 = Number(question('Digite um número: '))
    // processamento e saida
    const opcao = Number(question('Digite o número que você quer ver: '))
    if(opcao == 1){
        console.log(num1)
    }
    if(opcao == 2){
        console.log(num2)
    }
    if(opcao == 3){
        console.log(num3)
    }
    else{
        console.log('Fora de intervalo!')
    }
}
main()