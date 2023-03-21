import { question } from "readline-sync"
function main(){
    var pesoAtual = Number(question('Qual é seu peso atual? \n>> '))
    var perder = Number(question('Quantos % você quer perder de peso? \n >> '))
    var tempo = Number(question('Em quantas semanas você deseja perder?\n >> '))
    var kcal_diario = Number(question('Quantas calorias você consome por dia? \n >> '))
    
    // Processamento
    var perder = pesoAtual * (perder / 100) // Calcula a porcentagem do peso
    const def = calcularDef(kcal_diario, tempo, perder).toFixed(2)
    
    console.log(`O seu déficit diário tem que ser de ${def} kcal`)


    
}

function calcularDef(kcal, tempo, perder){
    var kcal_total = kcal * (tempo * 7)
    var peso_kcal = perder * 7700
    const total = kcal_total - peso_kcal
    const tempo_total = tempo * 7
    return total / tempo_total
}
main()