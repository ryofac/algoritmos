/* Crie um programa que receba o peso e a atividade física diária de uma pessoa e calcule a quantidade de água que ela deve beber por dia. 
A quantidade de água recomendada é de 35 ml por quilo de peso para pessoas com atividade física moderada, 
e 45 ml por quilo de peso para pessoas com atividade física intensa. O resultado do cálculo deve ser exibido na tela. */

import chalk from "chalk" // npm install chalk
// Biblioteca que adciona algumas cores e funcionalidades visuais básicas no terminal

import { question } from "readline-sync"

function main() {
    // Descrição:
    header(`CALCULADORA DE ${azul('ÁGUA')}`)

    // Entrada:
    var pes = Number(input('Qual é o seu peso? (em Kg)\n>> '))

    // Processamento: 
    const agua_moderado = arredondar(moderado(pes))
    const agua_intenso = arredondar(intenso(pes))

    // Saída:
    header(`PESO = ${azul(pes) + azul('Kg')}`)
    print(`O valor de água diário recomendado para atividades físicas ${verde('moderadas ')}é de ${verde(agua_moderado)} L`)
    print(`O valor de água diário recomendado para atividades físicas ${vermelho('intensas')} é de ${vermelho(agua_intenso)} L`)
    header('Volte Sempre!')

}


// Exercício intenso ou moderado:
function moderado(peso) {
    var quantidade_agua = (peso / 1000) * 35
    return quantidade_agua
}


function intenso(peso) {
    var quantidade_agua = (peso / 1000) * 45
    return quantidade_agua

}


// Um cabeçalho que recebe como parâmetros um texto
function header(txt) {
    // Fazendo um cabeçalho proporcional ao tamanho do texto
    var tamanho = txt.length
    console.log('='.repeat(tamanho))
    console.log('' + txt + '')
    console.log('='.repeat(tamanho))
}


// Função para receber os dados
function input(valor) {
    return question(valor)
}

//Função para saída de dados
function print(valor) {
    return console.log(valor)

}


// Função que arredonda os valores fornecidos em duas casas decimais
function arredondar(numero) {
    var arredondamento = numero.toFixed(2)
    return arredondamento
}


// Função que fornecerá a cor vermelha no terminal
function vermelho(txt) {
    const resultado = chalk.red(txt)
    return resultado // Retorna o texto em vermelho
}


// Função que fornecerá a cor verde no terminal
function verde(txt) {
    const resultado = chalk.green(txt)
    return resultado // Retorna o texto em verde
}

// Função que fornecerá a cor azul no terminal
function azul(txt) {
    return chalk.blueBright(txt)
}


main() // chamando a função main()
