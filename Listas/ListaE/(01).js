import { question } from "readline-sync";

function main(){
    // Entrada
    const num1 = ler('Digite o primeiro número: ')
    const num2 = ler('Digite o segundo número: ')
    const num3 = ler('Digite o terceiro número: ')

    // Fui pesquisar e descobri que para comparar strings se usa o operador "==="
    // Fiz três condicionais, uma se pelo menos dois números são iguais, uma se todos são e outra se nenhum é  
    // Para isso, utilizei a função "eIgual"

    // Saída (com condicionais)
    if (eIgual(num1, num2, num3) === 'todos'){
        console.log('São todos iguais! ')
    }

    else if (eIgual(num1, num2, num3) === '2iguais'){
        console.log('Tem dois números iguais!')
    }

    else if (eIgual(num1, num2, num3) === 'nenhum'){
        console.log('São todos diferentes! ')
    }

}

 // Processamento
function eIgual(n1,n2,n3){
// Checa se tem pelo menos dois números iguais, ou são todos iguais, ou nenhum
    
    if((n1 === n2) && (n2 === n3)){
        return 'todos'
    }

    else if((n1 === n2) || (n2 === n3)){
        return '2iguais'
    }
    
    else{
        return 'nenhum'
    }
}

// Função para ler o input do usuário
function ler(txt){
    const pergunta = question(txt)
    return pergunta
    }

// Chamando a função main()
main()