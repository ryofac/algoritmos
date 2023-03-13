import { question } from "readline-sync";
function main(){
var distancia = Number(question('Qual a distancia da prova, em m? \n >> '))
var velocidade = Number(question('Qual é a velocidade do atleta? (em km/h) \n >> '))
const tempo = calcularTempo(distancia, velocidade)

console.log(`O tempo da prova é de ${tempo} min`)
}

function calcularTempo(distancia, velocidade){
    var tempo = (distancia/1000) / (velocidade)
    return tempo * 60

}
main()