import { question } from "readline-sync"
function main(){
    header('Calculando imc')
    // Entrada:
    const altura = Number(question('Altura: '))
    const peso = Number(question('Peso: '))
    console.log('Seu IMC é de ' + calcularImc(altura, peso))
}

// Processamento:
function calcularImc(altura, peso){
    const imc = peso / altura ** 2
    return imc
}


function header(txt){
    console.log('============')
    console.log(txt)
    console.log('=============')
}
// Saída:
main()
