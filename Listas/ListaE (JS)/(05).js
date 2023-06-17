import { question } from "readline-sync";
function main(){
    // Entrada:
    const num1 = Number(question('Digite o primeiro número: '))
    const num2 = Number(question('Digite o segundo número: '))
    const num3 = Number(question('Digite o terceiro número: '))

    // Saída
    console.log(`A ordem crescente desses números é: ${crescente(num1,num2,num3)}`)

}

function crescente(n1,n2,n3){
    /* Processamento :
    Nas condicionais, vê-se primeiro o maior número */

    if(is_higher(n1,n2,n3)){ // Verifica se o primeiro número é o maior
        if(n2 > n3){
            return ` ${n3}, ${n2}, ${n1}`
        }
        else{
            return `${n2}, ${n3}, ${n1}`
        }
    }
    else if (is_higher(n2,n3,n1)){ // Verifica se o segundo número é o maior
        if(n1 > n3 ){
            return ` ${n3}, ${n1}, ${n2}`
        }
        else{
            return `${n1}, ${n3}, ${n2}`
        }
    }else{ // Se o terceiro número for maior
        if(n1 > n2){
            return `${n2}, ${n1}, ${n3}`
        }
        else{
            return `${n1}, ${n2}, ${n3}`
        }
    }
 }

 function is_higher(n1,n2,n3){
    return n1 >= n2 && n1 >= n3 // Retorna o valor booleano dessa expressão, ajuda bastante !
 }

main()