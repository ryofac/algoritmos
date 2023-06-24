import { get_integer, get_text,
     show_text, get_integer_interval, 
     delay } from "./utils/io_utils.js"

import {vender_bilhete_manual,
    ler_arquivo, bye, gerar_bilhetes_dezenas, 
    write_in_file, ler_bilhetes,ler_pessoas,mostrar_ganhadores,
    zerar_dados, mostrar_bilhetes,
    calcular_valor_arrecadado, check_empty_values, mostrar_valor_arrecadado, DEBUG,
    atribuir_sessao_anterior, ler_sessao_anterior } from "./features.js"

import { clear_screen, enter_to_continue, green_text } from "./utils/visual_utils.js"



// Criação de constantes para melhor leitura visual
const opcoes = {
    VENDA_BILHETE_MANUAL: 1,
    MOSTRAR_VALOR_ARRECADADO: 2,
    REALIZAR_SORTEIO_DEZENAS: 3,
    MOSTRAR_BILHETES: 4,
    APAGAR_DB: 5,
    SAIR: 0
}

// Lendo arquivos do "Banco de Dados"
let bilhetes = ler_bilhetes("./data/bilhetes.txt")
let pessoas = ler_pessoas("./data/pessoas.txt", bilhetes)
const bye_file = ler_arquivo("./data/bye.txt")
// Guarda dados importantes da sessão
let sorteio_atual = ler_sessao_anterior('./data/temp.txt')

function main(){
    clear_screen()
    let opcao
    show_text('Bem vindo ao sistema PATROBET!')
    if(sorteio_atual['well_closed'] === false){
       sorteio_atual = atribuir_sessao_anterior('./data/temp.txt')
    }else{
        sorteio_atual = {
            premiado: [],
            valor_arrecadado: 0,
            valor_bilhete: 0,
            debug: false,
            well_closed: false
        }
    }
    clear_screen()
    while(opcao !== opcoes['SAIR']){
        // "Checagem" e seleção de valores iniciais
        check_empty_values(sorteio_atual)
        DEBUG(sorteio_atual, pessoas, bilhetes)
        calcular_valor_arrecadado(pessoas, sorteio_atual)
        sorteio_atual['well_closed'] = false
        write_in_file("./data/temp.txt", sorteio_atual, 'sorteio_atual') // Salva a cada volta
        opcao = get_integer_interval(menu(sorteio_atual), 0, 10) // Pede a opção
        enter_to_continue()

        if (opcao === opcoes['VENDA_BILHETE_MANUAL']) {
            vender_bilhete_manual(pessoas, bilhetes)
            enter_to_continue()
        }
        if (opcao === opcoes['MOSTRAR_VALOR_ARRECADADO']) {
            mostrar_valor_arrecadado(sorteio_atual)
            enter_to_continue()
        }
        if(opcao === opcoes['MOSTRAR_TABELA_ARRECADACAO']){
            mostrar_tabela_arrecadacao(sorteio_atual)

        }
        if (opcao == opcoes['REALIZAR_SORTEIO_DEZENAS']) {
           sorteio_atual['premiado'] = gerar_bilhetes_dezenas()
           mostrar_ganhadores(bilhetes, sorteio_atual['premiado'], pessoas)
           enter_to_continue()
        }
        if (opcao === opcoes['MOSTRAR_BILHETES']){
            mostrar_bilhetes(pessoas, sorteio_atual['premiado'])
            enter_to_continue()
        }
        if (opcao == opcoes["APAGAR_DB"]){
            pessoas = zerar_dados()
            bilhetes = zerar_dados()
            sorteio_atual['premiado'] = zerar_dados()
            sorteio_atual['valor_bilhete'] = 0
            sorteio_atual['valor_arrecadado'] = 0
            show_text('Valores apagados!', 'R')
        }
       
    }
    clear_screen()
    sorteio_atual['well_closed'] = true
    write_in_file("./data/bilhetes.txt", bilhetes, 'bilhetes')
    write_in_file("./data/pessoas.txt", pessoas, 'pessoas')
    write_in_file("./data/temp.txt", sorteio_atual, 'sorteio_atual')

    bye(bye_file)
}

function menu(sorteio_atual){
    let opcao = "========= PATROBET's: MegaPATRO da PATROvirada ==========="
    sorteio_atual['premiado'].length > 0? opcao += green_text(`\n === ÚLTIMO SORTEADO: ${sorteio_atual['premiado']} ===`): opcao += ''
    opcao += '\n1 - Venda manual de bilhete'
    opcao += '\n2 - Mostrar valor arrecadado'
    opcao += '\n3 - Realizar sorteio dezenas'
    opcao += '\n4 - Mostrar bilhetes'
    opcao += '\n5 - Apagar TUDO!'
    opcao += '\n0 - SAIR'
    opcao += '\n > '
    return opcao


}
main()
