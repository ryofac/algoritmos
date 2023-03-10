import { question } from "readline-sync"
function main(){
    header('Calculadora de água') // Descrição

    // Entrada: 
    const pes = question('Qual é o seu peso?\n>> ')
    const temp = question('Quanto tempo de atividade física você fez? (em horas)\n>> ')
    const calor = question('Quantas calorias você gastou no exercício? (em kcal)\n>> ')

    // Processamento:
    const ex_leve = (pes / 1000) * 35
    const ex_pesado = (pes / 1000) * 45

     // Saída: 
    if (calcular_met(pes,temp,calor) < 3 ){
        header('> EXERCÍCIO LEVE <')
         console.log(`Você deve beber ${arredondar(ex_leve)} L de água`)
        
    }
    if (calcular_met(pes,temp,calor) >= 3 || calcular_met(pes,temp,calor)  <= 5.9){
        header('> EXERCÍCIO MODERADO <')
         console.log(`Você deve beber ${arredondar(ex_leve)} L de água`)
         
    }
    if (calcular_met(pes, temp, calor) > 6){
        header('> EXERCÍCIO PESADO < ')
         console.log(`Você deve beber ${arredondar(ex_pesado)} L de água`)    
    }
    
    console.log(`MET = ${calcular_met(pes,temp,calor)}`)
    header('Volte sempre !')


// Processamento dos dados recebidos:
/*
 Para saber a intensidade de um exercício físico, é utilizado pelo algoritmo o conceito de MET (Múltiplos de equivalentes metabólicos),
 O MET caracteriza a itensidade do exercício físico:
 – atividades consideradas como de intensidade moderada são as que consomem de 3 a 5,9 METs
 – atividades consideradas como intensas consomem 6 METs ou mais
*/

// Determina a itensidade do exercício físico
function calcular_met(cal, peso, tempo){
    //Gasto energético = MET  x  peso corporal (kg) x [tempo da atividade (min) / 60]
    const met = (tempo * peso) / cal
    return met
}

// Cabeçalho
function header(txt){
    var tamanho = (txt.length)
     // Fazendo um cabeçalho proporcional ao tamanho da string
    console.log('=-'.repeat(tamanho))
    console.log(' ' + txt + ' ')
    console.log('-='.repeat(tamanho))
 }

// Função que arredonda o número fornecido em duas casas decimais
 function arredondar(numero){
    var arredondamento = numero.toFixed(2)
    return arredondamento
    }
}
main() // chamando a função main()
