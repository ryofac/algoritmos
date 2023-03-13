//  Calculadora de taxa metabólica basal em homens: (TMB)
/* O metabolismo basal é a quantidade de energia que o corpo necessita para desempenhar suas funções essenciais enquanto está em repouso.
Dado pela fórmula(Para mulheres): TMB = 447,6 + (9,2 x peso) + (3,1 x altura) - (4,3 x idade)
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
    console.log(`${bold('Peso:')} ${peso} kg\n${bold('Altura:')} ${altura} m\n${bold('Idade:')} ${idade} ano\n${bold('Sexo:')} Feminino`)
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


function calcularTMB(peso, altura, idade){ // Calcula a taxa metabólica basal (em mulheres)
    var TMB = 447.6 + (9,2 * peso) + (3,1 * altura) - (4,3 * idade)
    return TMB
}

main() // chamando a função main