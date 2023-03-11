/* Crie um programa que receba a idade de uma pessoa e calcule a sua frequência cardíaca máxima, 
que é dada pela fórmula 220 menos a idade. O programa deve então calcular a faixa de batimentos cardíacos ideais
para atividades físicas moderadas e intensas, que correspondem a 50-70% e 70-85% da frequência cardíaca máxima, respectivamente. 
Os resultados devem ser exibidos na tela. */

// Tomei a liberdade de pegar uma biblioteca nova, já que a gente viu como fazer isso na aula e essa é bem simples de entender:

import chalk from "chalk" // npm install chalk
import { question } from "readline-sync" // para ler o input do usuário


function main(){
    header(`CALCULADORA DE ${vermelho('BATIMENTOS CARDÍACOS')}`)
    // Entrada:
    const idade = input('Qual a sua idade?')
    
    // Processamento:
    const frequenc_max = 220 - idade

    // Saída:
    print(moderada(frequenc_max))
    print(pesado(frequenc_max))
    header(azul('Obrigado por utilizar o programa!'))

}

// Função que lê o input do usuário
function input(valor){
    return question(valor + '\n>> ')

}

// Função que utiliza o console.log, só que "facilitada"
function print(valor){
    return console.log(valor)
}


// Funções que retornam os valores em bpm para atividade física moderada e pesada:
function moderada(freq){
    var min = Math.floor(0.5 * freq)
    var max = Math.floor(0.7 * freq)
    return `O valor ${azul('ideal')} de batimentos por minuto para atividades físicas ${verde('moderadas')}:\n >> Entre ${min} bpm (min) e ${max} bpm (max)`
}

function pesado(freq){
    var min = Math.floor(0.7 * freq)
    var max = Math.floor(0.85 * freq)
    return `O valor ${azul('ideal')} de batimentos por minuto para atividades físicas ${vermelho('pesadas')}:\n >> Entre ${min} bpm (min) e ${max} bpm (max)`
}

// Cabeçalho
function header(txt){
    var tamanho = (txt.length)
     // Fazendo um cabeçalho proporcional ao tamanho da string
    console.log('='.repeat(tamanho))
    console.log(' ' + txt + ' ')
    console.log('='.repeat(tamanho))
    } 


// Função que fornecerá a cor vermelha no terminal
function vermelho(txt){
    const resultado = chalk.red(txt) 
    return resultado // Retorna o texto em vermelho
}

// Função que fornecerá a cor verde no terminal
function verde(txt){
    const resultado = chalk.green(txt) 
    return resultado // Retorna o texto em verde
}

// Função que fornecerá a cor azul no terminal
function azul(txt){
    return chalk.blueBright(txt)
}


main()
