/* o IAC é uma medida que leva em conta a relação entre a altura, as pregas cutâneas e o perímetro do quadril 
para estimar a quantidade de gordura corporal em relação à massa magra. */
// Formula do IAC: IAC = (quadril / (altura * sqrt(altura))) - 18
import chalk from "chalk";
import { question } from "readline-sync";

function main(){
    header('CALCULADORA DE IAC')
    var altura = Number(read('Digite sua altura: (em cm'))
    var altura = (altura / 100)
    const quadril = Number(read('Digite o diâmetro da sua cintura: (em cm)'))
    var IAC = calcularIAC(altura, quadril)
    var max = valorMAX(altura)
    var min = valorMIN(altura)


    header('DADOS:')
    console.log(`Altura: ${altura} m`)
    console.log(`Circunferência do quadril: ${quadril} cm`)
    header(`IAC = ${IAC}`)
    console.log(`${verde('O valor da cintura mínimo')} para sua altura, para que esteja no valor normal é de ${verde(min + ' cm')}`)
    console.log(`${verm('O valor da cintura máximo')} para sua altura, para que esteja no valor normal é de ${verm(max + ' cm')}`)
    header('Volte sempre!!')


}

function read(txt){
    return question(txt + '\n>> ')
}

function calcularIAC(alt, quad){
    var IAC = (quad / (alt * Math.sqrt(alt))) - 18
    return IAC.toFixed(2)
}

function valorMAX(altura){
    // iac máx = 20.9
    const cintura_max = (38.9 * (altura * Math.sqrt(altura))).toFixed(2)
    return cintura_max
}

function valorMIN(altura){
    // iac min = 9
    const cintura_min = (27 * (altura * Math.sqrt(altura))).toFixed(2) 
    return cintura_min
}

function verde(txt){
    return chalk.greenBright(txt)
}

function verm(txt){
    return chalk.redBright(txt)
}

function header(txt){ // Recebe como parâmetro uma string e retorna um título simples
    console.log('='.repeat(txt.length)) // Repete a string com o número de caracteres do texto
    console.log(chalk.greenBright(txt)) // O texto retorna verde
    console.log('='.repeat(txt.length))
}

main()