/* o IAC é uma medida que leva em conta a relação entre a altura, as pregas cutâneas e o perímetro do quadril 
para estimar a quantidade de gordura corporal em relação à massa magra. */
// Formula do IAC: IAC = (quadril / (altura * sqrt(altura))) - 18
import chalk from "chalk";
import { question } from "readline-sync";

function main(){
    // Descrição:
    header('CALCULADORA DE IAC')

    // Entrada:
    var altura = Number(read('Digite sua altura: (em cm'))
    var altura = (altura / 100)
    const quadril = Number(read('Digite o diâmetro da sua cintura: (em cm)'))

    // Processamento:
    var IAC = calcularIAC(altura, quadril)
    var max = valorMAX(altura)
    var min = valorMIN(altura)

    // Saída: 
    header('DADOS:')
    console.log(`Altura: ${altura} m`)
    console.log(`Circunferência do quadril: ${quadril} cm`)
    header(`IAC = ${IAC}\n>> Normal: Entre 9 e 20.9`)
    console.log(`${verde('O tamanho do quadril mínimo')} para sua altura, para que IAC esteja no valor normal é de ${verde(min + ' cm')}`)
    console.log(`${verm('O valor do quadril máximo')} para sua altura, para que o IAC esteja no valor normal é de ${verm(max + ' cm')}`)
    header('Volte sempre!!')


}
 // Função que lê o número, retornando a formatação de input com a quebra de linha
function read(txt){
    return question(txt + '\n>> ')
}


// Função que calcula o iac
function calcularIAC(alt, quad){
    var IAC = (quad / (alt * Math.sqrt(alt))) - 18
    return IAC.toFixed(2)
}

function valorMAX(altura){ // Valor máximo da cintura
    // iac máx = 20.9
    const cintura_max = (38.9 * (altura * Math.sqrt(altura))).toFixed(2)
    return cintura_max
}

function valorMIN(altura){ // Valor mínimo da cintura
    // iac min = 9
    const cintura_min = (27 * (altura * Math.sqrt(altura))).toFixed(2) 
    return cintura_min
}


function verde(txt){ // Deixa o texto verde
    return chalk.greenBright(txt)
}


function verm(txt){ // Deixa o texto vermelho
    return chalk.redBright(txt)
}


// Formata um título simples
function header(txt){ // Recebe como parâmetro uma string e retorna um título simples
    console.log('='.repeat(txt.length)) // Repete a string com o número de caracteres do texto
    console.log(chalk.greenBright(txt)) // O texto retorna verde
    console.log('='.repeat(txt.length))
}

main() // chamando a função main