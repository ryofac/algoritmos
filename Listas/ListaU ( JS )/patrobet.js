import { get_integer, get_text, show_text, get_integer_interval, delay } from "./utils/io_utils.js"
import {vender_bilhete_manual,
     ler_arquivo, bye,
     gerar_bilhetes_dezenas, 
     write_in_file, ler_bilhetes,
     enter_to_continue, ler_pessoas} from "./features.js"

// Criação de constantes para melhor leitura visual
const opcoes = {
    VENDA_BILHETE_MANUAL: 1,
    MOSTRAR_VALOR_ARRECADADO: 2,
    MOSTRAR_TABELA_ARRECADACAO: 3,
    REALIZAR_SORTEIO_DEZENAS: 4,
    GERAR_N_SURPRESINHAS: 5,
    MOSTRAR_BILHETES: 6,
}
const bilhetes = ler_bilhetes("./data/bilhetes.txt")
const pessoas = ler_pessoas("./data/pessoas.txt", bilhetes)
const bye_file = ler_arquivo("./data/bye.txt")


function main(){
    let opcao = get_integer_interval(menu(), 0, 10)
    while(opcao !== 0){
        console.log(pessoas)
        console.log(bilhetes)
        if (opcao === opcoes['VENDA_BILHETE_MANUAL']) {
            vender_bilhete_manual(pessoas, bilhetes)
        }
        if (opcao === opcoes['MOSTRAR_VALOR_ARRECADACAO']) {
            mostrar_valor_arrecadado(bilhetes)

        }
        if (opcao == opcoes['REALIZAR_SORTEIO_DEZENAS']) {
            const sorteado = gerar_bilhetes_dezenas()
            show_text('O sorteado foi: ' + sorteado)
        }
       
        if(opcao === opcoes['GERAR_N_SURPRESINHAS']){
            const n = get_integer('Digite a quantidade de bilhetes: ')
            for(let i = 0; i < n; i ++){
                bilhetes.push(gerar_bilhetes_dezenas())
            }
        }
        if (opcao === opcoes['MOSTRAR_BILHETES']){

        }
        opcao = get_integer_interval(menu(), 0, 10)
        enter_to_continue()
    }
    bye(bye_file)
    write_in_file("./data/bilhetes.txt", bilhetes, 'bilhetes')
    write_in_file("./data/pessoas.txt", pessoas, 'pessoas')
}

function menu(){
    let opcao = "========= PATROBET's: MegaPATRO da PATROvirada ==========="
    opcao += '\n1 - Venda manual de bilhete'
    opcao += '\n2 - Mostrar valor arrecadado'
    opcao += '\n3 - Mostrar tabela de arrecadação '
    opcao += ('\n4 - Realizar sorteio dezenas')
    opcao += '\n5 - Gerar surpresinha '
    opcao += '\n6 - Mostrar bilhetes'
    opcao += '\n > '
    return opcao


}
main()
