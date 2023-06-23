import {readFileSync, writeFileSync} from "fs"; 

import { COLOrFuL, green_text, clear_screen, red_text} from "./utils/visual_utils.js";

import { get_integer, get_integer_interval, get_number, 
    get_random_number_between, get_text, 
    show_text} from "./utils/io_utils.js";

import { is_in, my_filter, my_map, string_vetor, count_elements, eh_objeto_vazio } from "./utils/vetor_utils.js"
import { get_random_array, get_vetor } from "./utils/io_utils.js";
import { ulid } from "ulid"
import { len_of } from "./utils/str_utils.js";


export function criar_pessoa(nome, bilhetes, id=ulid()){
    const pessoa = {
        id: id,
        nome: nome,
        bilhetes: bilhetes
    }
    return pessoa
}


export function ler_pessoa(bilhetes, nome, id){
    const pessoa = {
        id: id,
        nome: nome,
        bilhetes: get_bilhete_by_id(bilhetes, id)
    }
    return pessoa
}


export function criar_bilhete(id_pai, numeros, id=ulid()){
    const bilhete = {
        id: id,
        id_pai: id_pai,
        numeros: numeros
    }
    return bilhete
}


export function ler_bilhete(id_pai, numeros, id){
    const bilhete = {
        id: id,
        id_pai: id_pai,
        numeros: numeros
    }
    return bilhete
}


export function ler_arquivo(file){
    const raw = readFileSync(file, 'utf8').split('\n')
    const out = my_filter(raw, x => x != '')
    return out
}

export function get_bilhete_by_id(bilhetes, id_pai){
    const out = []
    for(let i = 0; i < bilhetes.length; i++){
        // Buscar id's dentro de bilhetes e ver se é igual ao id_pai
        let bilhete = bilhetes[i]
        let id = bilhete['id_pai']
        if(id === id_pai){
            out.push(bilhetes[i]['numeros'])
        }
    }
    return out
}


export function ler_pessoas(file, bilhetes){
    const pessoas = [] // Array que irá armazenar os objetos de pessoas
    const pessoas_raw = ler_arquivo(file)
    
    for (let i = 0; i < pessoas_raw.length; i ++ ){
        let linha = pessoas_raw[i]
        linha = linha.split('#')
        const pessoa = ler_pessoa(bilhetes, linha[1], linha[0])
        pessoas.push(pessoa)
    }
    return pessoas
}


export function ler_bilhetes(file){
    const bilhetes  = []
    const raw = ler_arquivo(file)
    for(let line of raw){
        if(!line || line === '\n')  continue
        line = line.split("#") 
        let id = line[0]
        let numbers = my_map(line[2].split(','), x => Number(x))
        let id_pai = line[1]
        const bilhete = ler_bilhete(id_pai, numbers, id)
        bilhetes.push(bilhete)
    }
    return bilhetes
}

export function atribuir_sessao_anterior(file){
    console.log('Vi que você fechou o arquivo ' + red_text('sem salvar') + ' quer tentar recuperar dados? ')
    let opcao = '1 - Sim'
    opcao += '\n2 - Não'
    opcao += '\n> '
    let choice = get_integer_interval(opcao, 1, 2)
    if(choice === 2) {
        const sorteio_atual = {
            premiado: [],
            valor_arrecadado: 0,
            valor_bilhete: 0,
            debug: false,
            well_closed: false
        }   
        return sorteio_atual
    }
    let sorteio_atual = ler_sessao_anterior(file)
    return sorteio_atual
}
    

export function ler_sessao_anterior(file){
    const raw = ler_arquivo(file)
    let sorteio_atual
    let premiado
    for(let line of raw){
        if(!line || line === '\n')  continue
        line = line.split("#") //PREMIADO#VALOR_BILHETE#VALOR_ARRECADADO#DEBUG#W_C
        len_of(line[0]) > 1 ? premiado = my_map(line[0].split(','), x => Number(x)): premiado = []
        sorteio_atual = {
            premiado: premiado,
            valor_arrecadado: Number(line[1]),
            valor_bilhete: Number(line[2]),
            debug: line[3] === 'false'? false: true,
            well_closed: line[4] === 'false'? false: true
        }
    }
    return sorteio_atual

}


export function mostrar_valor_arrecadado(sorteio_atual){
    show_text(`O valor arrecadado é de R$${sorteio_atual['valor_arrecadado'].toFixed(2)}`)
}


export function vender_bilhete_manual(pessoas, bilhetes_file){
    clear_screen()
    let opcoes = 'Digite a opção!'
    opcoes += '\n1 - Gerar nova pessoa'
    opcoes += '\n2 - Comprar de pessoa existente'
    opcoes += '\n> '
    const choice = get_integer_interval(opcoes, 1, 2)

    while(!choice) choice = get_integer_interval(opcoes, 1, 2)
    let pessoa
    if(choice === 1){
        const nome = get_text('Digite o seu nome: ')
        pessoa = criar_pessoa(nome, [])
        pessoas.push(pessoa)
    
    }
    else{
        const index = get_index_pessoas(pessoas)
        pessoa = pessoas[index]
    }
        
        let menu = 'Digite a opção!'
        menu += '\n1 - Gerar Manual'
        menu += '\n2 ' + COLOrFuL('Gerar SURPRESINHA')
        menu += '\n> '
        const opcao = get_integer_interval(menu, 1, 2)
        while(!opcao) opcao = get_integer_interval(menu, 1, 2)
        if(opcao === 1){
            const quantidade_bilhetes = get_integer('Quantidade de bilhetes a ser comprada: ')
            for(let i = 0; i < quantidade_bilhetes; i++){
                let bilhete = get_vetor('Digite os números na linha: ', 6, 1, 60, true)
                let new_bilhete = criar_bilhete(pessoa['id'], bilhete, ulid())
                bilhetes_file.push(new_bilhete)
                pessoa['bilhetes'].push(new_bilhete['numeros'])
            }
        }else{
            const quantidade_bilhetes = get_integer('Quantidade de bilhetes a ser comprada: ')
            for(let i = 0; i < quantidade_bilhetes; i++){
                let bilhete = get_random_array(6, 1, 60, false)
                let new_bilhete = criar_bilhete(pessoa['id'], bilhete, ulid())
                bilhetes_file.push(new_bilhete)
                pessoa['bilhetes'].push(new_bilhete['numeros'])
                }
            }
}

export function bye(bye_file){
    const list = bye_file
    const random_index = get_random_number_between(0, bye_file.length)
    const frase_para_se_despedir_e_ficar_triste = list[random_index]
    show_text(frase_para_se_despedir_e_ficar_triste)

}


export function calcular_valor_arrecadado(pessoas, sorteio_atual){
    const num_bilhetes = obter_total_bilhetes(pessoas)
    sorteio_atual['valor_arrecadado'] = sorteio_atual['valor_bilhete'] * num_bilhetes 
}


export function write_in_file(file, memory, type){
    let data = '';
    if(type == 'sorteio_atual'){
        data += `${memory['premiado']}#${memory['valor_arrecadado']}#${memory['valor_bilhete']}#${memory['debug']}#${memory['well_closed']}`
    }else{
        for(let item of memory){
            if(type === 'pessoas'){
                data += `${item['id']}#${item['nome']}\n`
            }
            if(type === 'bilhetes'){
                data += `${item['id']}#${item["id_pai"]}#${item['numeros']}\n`
            }
        }
        show_text(`Arquivo ${file} foi salvo com sucesso!`, 'G')
    }
    writeFileSync(file, data)
}


export function obter_ganhadores(premiado, bilhetes){
    const ganhadores = {
        total: [],
        quina: [],
        quadra: []
    }
    for(let bilhete of bilhetes){
        const acertos = count_elements(bilhete['numeros'], premiado)
        if(acertos === bilhete.length) ganhadores['total'].push(bilhete)
        if(acertos === 5) ganhadores['quina'].push(bilhete)
        if(acertos === 4) ganhadores['quadra'].push(bilhete)
    }
    return ganhadores
}
   

export function get_index_pessoas(pessoas){
    for(let i = 0; i < pessoas.length; i ++) {
        show_text(`${i + 1} -> ${pessoas[i]['nome']}`)
    }
    let opcao = get_integer_interval('Escolha uma pessoa: ', 1 , pessoas.length + 1)
    let index = opcao - 1
    return index
}

export function mostrar_ganhadores(bilhetes, premiado, pessoas){
    show_text('O premiado foi: ' + string_vetor(premiado))
    const ganhadores = obter_ganhadores(premiado, bilhetes)

    eh_objeto_vazio(ganhadores)? console.log('Prêmio Acumulado!'): console.log('=== Ganhadores ===')    
    if(ganhadores['total'].length > 0){
        console.log(' == PATROBET DA VIRADA == ')
        for(let bilhete of ganhadores['total']){
            show_text(get_pessoa_by_id(pessoas, bilhete['id_pai'])['nome'] + ' => ' + bilhete['numeros'], 'G')
        }
    }
    if (ganhadores['quadra'].length > 0){
        console.log(' == QUADRA == ')
        for(let bilhete of ganhadores['quadra']){
            show_text(get_pessoa_by_id(pessoas, bilhete['id_pai'])['nome'] + ' => ' + bilhete['numeros'], 'G')
        }
    }
    if (ganhadores['quina'].length > 0){
        console.log(' == QUINA == ')
        for(let bilhete of ganhadores['quina']){
            show_text(get_pessoa_by_id(pessoas, bilhete['id_pai'])['nome'] + ' => ' + bilhete['numeros'], 'G')
        }
    }    
}

export function mostrar_bilhetes(pessoas, premiado){
    if(pessoas.length === 0){
        console.log('Não há pessoas ainda!') 
        return
    }
    let index = get_index_pessoas(pessoas)
    console.clear()
    for(let i = 0; i < pessoas[index]['bilhetes'].length; i ++){
        show_text(`====BILHETE ${i+1}====`)
        show_bilhete(pessoas[index]['bilhetes'][i], premiado)
        show_text('===============')
    }
}


export function check_empty_values(sorteio_atual){
    if(!sorteio_atual['valor_bilhete']){
        sorteio_atual['valor_bilhete'] = get_number('Digite o valor de cada bilhete: R$ ', "+")
    }
}

export function obter_total_bilhetes(pessoas){
    let total_bilhetes = 0
    for(let pessoa of pessoas){
        if (!pessoa) continue
        total_bilhetes += pessoa["bilhetes"].length
    }
    return total_bilhetes

}

export function DEBUG(sorteio_atual, pessoas, bilhetes){
    if(sorteio_atual['debug']){
    show_text('Modo DEBUG ativo!')
    console.log('PESSOAS:')
    console.log(pessoas)
    console.log('BILHETES:')
    console.log(bilhetes)
    console.log('CONFIG: ')
    console.log(sorteio_atual)
    console.log('VALOR BILHETE: ' + sorteio_atual['valor_bilhete'])
    }
}

// ======= UTILS ========

export function zerar_dados(){
    return []
}

export function gerar_bilhetes_dezenas(){
    const out = get_random_array(6, 1, 60, false)
    return out

}
export function show_bilhete(bilhete, premiado){

    if(!premiado){
        show_text(bilhete)
    }
    for(let numero of bilhete){
        if(is_in(numero, premiado)){
            process.stdin.write(` ${green_text(numero)} `)
        }
        else{
            process.stdin.write(` ${numero} `) 
        }
    }
    console.log()

}

export function get_pessoa_by_id(pessoas, id){
    for(let pessoa of pessoas){
        if (pessoa['id'] === id){
            return pessoa
        }
    }
}