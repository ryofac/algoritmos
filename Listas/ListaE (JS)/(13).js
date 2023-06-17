import { question } from "readline-sync";
function main(){

    var maior_valor = -Infinity
    var menor_valor = Infinity
    var cont = 0
    while(cont < 5){
        var num = Number(question('Digite o seu número inteiro: '))

        if(num > maior_valor){
            maior_valor = num
        }
        if(num < menor_valor){
            menor_valor = num
        }
        cont ++

    }
    console.log(`O maior valor é  ${maior_valor}`)
    console.log(`O menor valor é ${menor_valor}`)
   

}

main()