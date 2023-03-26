import { question } from "readline-sync";
function main(){
header('VERIFICADOR DE TRIÂNGULOS')
 const area1 = Number(question('Digite o primeiro ângulo: \n>> '))
 const area2 = Number(question('Digite o segundo ângulo \n>> '))
 const area3 = Number(question('Digite o terceiro ângulo \n>> '))

 console.log(vrfTriangulo(area1, area2, area3))

}

function vrfTriangulo(a1, a2, a3){
    if (a1 + a2 + a3  === 180){
        header('CLASSIFICAÇÃO:')
        if(a1 === 90|| a2 === 90|| a3 === 90 ){
            return 'O triângulo é retângulo!'
        }
        else if(a2> 90 || a2 > 90 || a3 > 90 ){
            return 'O triângulo é obtuso'
        }
        else{
            return 'O triângulo é acutângulo'
        }
        }
    else{
        return 'Digite um valor válido'
    }
}

function header(txt){
    console.log('='.repeat(txt.length))
    console.log(txt)
    console.log('='.repeat(txt.length)) }

main()