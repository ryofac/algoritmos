import { question } from "readline-sync";
function main(){
header('VERIFICADOR DE TRIÂNGULOS')
// Entrada
 const lado1 = Number(question('Digite o primeiro lado: \n>> '))
 const lado2 = Number(question('Digite o segundo lado: \n>> '))
 const lado3 = Number(question('Digite o terceiro lado \n>> '))

 // Processamento
if (is_triangle(lado1 ,lado2, lado3)){
        header('CLASSIFICAÇÃO:')
        if(a1 >  a2 && a1 > a3 ){
            console.log('O triângulo é RETÂNGULO') // Saída se o triângulo tiver pelo menos um ângulo = 90
        }
        else if(a1 > 90 || a2 > 90 || a3 > 90 ){ // Saída se o ângulo tiver pelo menos um ângulo maior que 90
         console.log('O triângulo é OBTUSO')
        }else{ // Saída se for acutângulo
            console.log('O triângulo é ACUTÂNGULO')
        }
    }else{
        console.log('Digite um valor válido!')
    }
}


function is_triangle(a1, a2, a3){
    return a1 + a2 >=a3 
    || a2 + a3 > a1 
    ||a1 + a3 > a2 && is_not_zero_minus(a1,a2,a3)

}
function is_not_zero_minus(a1,a2,a3){ // Verifica se os números são iguais a 0
    return a1 <= 0 && a2 <= 0 && a3 <= 0
}

function header(txt){
    console.log('='.repeat(txt.length))
    console.log(txt)
    console.log('='.repeat(txt.length)) 
}


main()