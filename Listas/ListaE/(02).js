import { question } from "readline-sync";
function main(){
    header('VERIFICADOR DE MENOR NÚMERO')
    const n1 = Number(question('Digite o primeiro número \n> '))
    const n2 = Number(question('Digite o segundo número \n> '))
    console.log(`O menor valor entre os números digitados é : ${menor(n1,n2)}`)
}

function menor(num1,num2){ // Verifica os números e retorna o menor!
    if (num1 > num2){
    return num2
    } else if (num2 > num1){
    return num1
    }
    else{
    return  ' VALORES IGUAIS '
    }
    }


function header(txt){
    console.log('='.repeat(txt.length))
    console.log(txt)
    console.log('='.repeat(txt.length))

}

main()