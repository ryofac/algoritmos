import { question, keyIn } from "readline-sync";
import chalk from "chalk";

function main(){
    let selected = 0
   
    while(true){
        console.clear()
        draw_menu(selected)
        const key = keyIn('\n W(UP) S(DOWN)', {hideEchoBack: true , mask: '', limit:'wsv'})
        if(key === 's'){
            selected ++
        }
        if(key === 'w'){
            selected --
        }
        if(key === 'v'){
            break
        }
        if(selected < 0) selected = 0
        if(selected >= 2) selected = 2
    }

    if(selected === 0){
        console.log(chalk.redBright('Matei o Patrocínio'))
    }
    if(selected === 1){
        console.log(chalk.redBright('Matei o Rogério'))
    }
    if(selected === 2){
        console.log('Matei o Marcelino')
    }
    

}

function draw_menu(selected){
    let opcoes = ['\n 1 - Matar o patrocinio',
    '\n 2 - Matar o Rogério', '\n 3 - Matar o Marcelino']

    for(let i = 0; i < opcoes.length; i ++){
        if(i === selected){
            opcoes[i] = chalk.yellowBright(opcoes[i])
        }
        console.log(opcoes[i])
    }

}
main()