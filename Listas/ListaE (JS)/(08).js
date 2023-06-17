import { question } from "readline-sync"

function main(){
const dia = Number(question('Digite o dia que você nasceu \n >> '))
const mes = Number(question('Digite o mês que você nasceu \n >> '))
const ano = Number(question('Digite o ano que você nasceu \n >> '))


if (!isValid(dia,mes,ano)){ // fail fast
    console.log('Dados Inválidos !!')
    return 
}
const ano_atual = 2023
const mes_atual = 3
const dia_atual = 23

let idade = ano_atual - ano

if (mes > mes_atual || mes == mes_atual && dia < dia_atual){
    idade = idade - 1
}
else if (dia == dia_atual) {
    console.log('Feliz aniversário!!!')

}
console.log(`DATA ATUAL: ${formatar(dia_atual,mes_atual,ano_atual)}`)
console.log(`Você tem ${idade} anos de idade ! Pois você nasceu na data ${formatar(dia,mes,ano)}`) 
}

function isValid(d,m,a){
    if (!(d > 0 && m > 0 && a > 0)){    // Fail Fast
        return
    }
    if ( m == 2 ){
        return d <= 28 && m <= 12 && a < 2023
    }
    return d <= 31 &&  m <= 12 && a < 2023 
}
function formatar(d,m,a){
     return `${d}/${m}/${a}`
}

main()