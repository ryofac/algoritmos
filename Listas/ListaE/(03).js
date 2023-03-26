import { question } from "readline-sync";

function main(){
    // Entrada:
    const num1 = Number(ler('Digite o primeiro número: '))
    const num2 = Number(ler('Digite o segundo número: '))
    const num3 = Number(ler('Digite o terceiro número: '))

    // Saída
    console.log(`O maior desses três números é o ${maior(num1, num2, num3)}`)

}


function ler(txt){
    // Função para otimizar o imput dos dados
    const pergunta = question(txt)
    return pergunta
}


function maior(n1,n2,n3){
    /* Processamento
    Foram feitas 3 situações condicionais para analisar qual dos números é maior ou menor
    */

    if(n1 > n2 && n1 > n3){
        return n1
    }
    else if (n2 > n1 && n2 > n3){
        return n2
    }
    else{
        return n3
    }
  }

// Chamando a função main()
main()