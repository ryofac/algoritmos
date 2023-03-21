import { question } from "readline-sync";

function main(){
    console.log('Calculadora de notas!')
    const nota1 = Number(question('Qual é a sua primeira nota? \n > '))
    const nota2 = Number(question('Qual é a sua segunda nota? \n > '))
    const media = calcularMedia(nota1,nota2)
    const situacao = verificarSituacao(media)
    console.log(`Sua média é de ${media.toFixed(2)} e sua situação é: ${situacao}`)

     
}
function calcularMedia(a,b){
    return (a + b ) / 2
}

function verificarSituacao(media){
   if (media >= 7){
    return 'aprovado'
   }
   else if (media >= 4){
    return 'prova final'
   }

   else{
    return 'reprovado'
   }
}
main()