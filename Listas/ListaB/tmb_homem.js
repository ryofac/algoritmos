//  Calculadora de taxa metabólica basal em homens: (TMB)
/* O metabolismo basal é a quantidade de energia que o corpo necessita para desempenhar suas funções essenciais enquanto está em repouso.
Dado pela fórmula(Para homens): TMB = 88,36 + (13,4 x peso) + (4,8 x altura) - (5,7 x idade)
 */
import { question } from "readline-sync";
import chalk from "chalk";


function main(){
    // Descrição
    header(' > CALCULADORA DE TAXA METABÓLICA BASAL < ')

    // Entrada
    const peso = Number(read(`Digite o seu ${bold('peso')}(em kg)`))
    const altura = Number(read(`Digite a sua ${bold('altura')}(em cm)`))
    const idade = Number(read(`Digite a sua ${bold('idade')}`))

    // Processamento
    var TMB = Math.floor(calcularTMB(peso, altura, idade))

    // Saída
    header('Dados:')
    console.log(`${bold('Peso:')} ${peso} kg\n${bold('Altura:')} ${altura} m\n${bold('Idade:')} ${idade} ano\n${bold('Sexo:')} Masculino`)
    header(`Taxa metabólica basal(TMB): ${chalk.blueBright(TMB)} `)
    console.log(bold('VOLTE SEMPRE! ;D'))

}


function bold(txt){ // Recebe como parâmetros uma string e retorna o texto em negrito
    return chalk.whiteBright(txt)
}


function header(txt){ // Recebe como parâmetro uma string e retorna um título simples
    console.log('='.repeat(txt.length)) // Repete a string com o número de caracteres do texto
    console.log(chalk.greenBright(txt)) // O texto retorna verde
    console.log('='.repeat(txt.length))
}


function read(txt){ // Recebe como parâmetros uma string e a armazena, formatando a pergunta
    return question(txt + '\n>> ')
}


function calcularTMB(peso, altura, idade){ // Calcula a taxa metabólica basal (em homens)
    var TMB = 88.36 + (13,4 * peso) + (4,8 * altura) - (5,7 * idade)
    return TMB
}

main() // chamando a função main
