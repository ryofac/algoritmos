import { question } from "readline-sync";
function main(){
    header('VERIFICADOR DE DÍGITOS IGUAIS')
    const num = Number(question('Digite um número de 2 Dígitos \n >> '))
    console.log(verificar(num))

}

function header(txt){
    console.log('='.repeat(txt.length))
    console.log(txt)
    console.log('='.repeat(txt.length))

}
 function verificar(num){
    const dezena = Math.floor(num / 10)
    const unidade = num % 10
    if (dezena > unidade){
        return (`Dezena maior que a unidade: ${dezena} > ${unidade}`)
    }else if (dezena < unidade){
        return (`Unidade maior que a dezena: ${unidade} > ${dezena} `)
    }
    else{
        return ('Unidade igual a dezena!')
    }
 }
main()