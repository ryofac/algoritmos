// npm install chalk
import chalk from "chalk"
// Biblioteca que adciona algumas cores e funcionalidades visuais básicas no terminal
import { question } from "readline-sync"

function main(){
    header('Calculadora de água') // Descrição

    // Entrada: 
    const pes = Number(question(('Qual é o seu peso? (em Kg)\n>> ')))
    const temp = Number(question('Quanto tempo de atividade física você fez? (em horas)\n>> '))
    const calor = Number(question('Quantas calorias você gastou no exercício? (em kcal)\n>> '))

    // Processamento:
    const ex_leve = (pes / 1000) * 35
    const ex_pesado = (pes / 1000) * 45
    const valor_met = calcular_met(calor,pes,temp)

     // Saída: 
    if (valor_met < 3 ){
        header('> EXERCÍCIO LEVE <')
         console.log(`Você deve beber ${arredondar(ex_leve)} L de água`)
        
    }
    if (valor_met >= 3 || valor_met <= 5.9){
        header('> EXERCÍCIO MODERADO <')
         console.log(`Você deve beber ${arredondar(ex_leve)} L de água`)
         
    }
    if (valor_met > 6){
        header('> EXERCÍCIO PESADO < ')
         console.log(`Você deve beber ${arredondar(ex_pesado)} L de água`)    
    }

    print(`Peso: ${verde(pes)} Kg`)
    print(`Tempo de atividade: ${vermelho(temp)} h`)
    print(`Calorias gastas: ${calor} Kcal`)
    print(`Valor do MET ("Múltiplos de equivalentes metabólicos"): ${verde(valor_met)}`)
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
    const met = (peso * cal) / tempo
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


//Função para saída de dados
function print(valor){
    return console.log(valor)   
    }


//Função que fornecerá a cor vermelha no terminal
function vermelho(txt){
    const resultado = chalk.red(txt) 
    return resultado // Retorna o texto em vermelho
}


// Função que fornecerá a cor verde no terminal
function verde(txt){
    const resultado = chalk.green(txt) 
    return resultado // Retorna o texto em verde
}

}
main() // chamando a função main()
