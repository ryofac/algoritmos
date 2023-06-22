import {readFileSync, writeFileSync} from "fs"; 
import { COLOrFuL } from "./utils/visual_utils.js";
import { get_integer, get_random_number_between, get_text, show_text } from "./utils/io_utils.js";
import { my_filter, my_map } from "./utils/vetor_utils.js"
import { get_random_array, get_vetor } from "./utils/io_utils.js";
import { ulid } from "ulid"
import { constants, randomFillSync } from "crypto";


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
            out.push(bilhetes[i])
        }
    return out
    }
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
        line = line.split("#") // ID#ID_PAI#NUMBERS
        console.log(line)
        let id = line[0]
        let numbers = my_map(line[2].split(','), x => Number(x))
        let id_pai = line[1]
        const bilhete = ler_bilhete(id_pai, numbers, id)
        bilhetes.push(bilhete)
    }
    return bilhetes
}


export function mostrar_valor_arrecadado(bilhetes){
    const valor_arrecadado = calcular_valor_arrecadado(bilhetes)
    show_text(`O Valor arrecadado total foi de R$${valor_arrecadado}`)
    
}


export function vender_bilhete_manual(pessoas, bilhetes_file){
    const nome = get_text('Digite o seu nome: ')
    const quantidade_bilhetes = get_integer('Quantidade de bilhetes a ser comprada: ')
    const pessoa = criar_pessoa(nome, [])
    console.log(pessoa)
    for(let i = 0; i < quantidade_bilhetes; i++){
        let bilhete = get_vetor('Digite os números na linha: ', 6, 1, 60, true)
        let new_bilhete = criar_bilhete(pessoa['id'], bilhete, ulid())
        bilhetes_file.push(new_bilhete)
        pessoa['bilhetes'].push(new_bilhete['numeros'])
    }
    pessoas.push(pessoa)
}


export function gerar_bilhetes_dezenas(){
    const out = get_random_array(6, 1, 60, false)
    return out

}

export function bye(bye_file){
    const list = bye_file
    const random_index = get_random_number_between(0, bye_file.length)
    const frase_para_se_despedir_e_ficar_triste = list[random_index]
    show_text(frase_para_se_despedir_e_ficar_triste)

}


export function calcular_valor_arrecadado(bilhetes, valor_bilhete){
    let valor_total = []
    for (let bilhete of bilhetes){
        valor_total += valor_bilhete
    }
    return valor_total
}
export function write_in_file(file, memory, type){
    console.log(file, 'Recebido!')
    let data = '';
    for(let item of memory){
        if(type === 'pessoas'){
            console.log('Arquivo Pessoas sendo salvo!')
            data += `${item['id']}#${item['nome']}\n`
        }
        if(type === 'bilhetes'){
            data += `${item['id']}#${item["id_pai"]}#${item['numeros']}\n`
            console.log('Add', data)
        }
    }
    console.log(`Arquivo ${file} salvo com sucesso`)
    writeFileSync(file, data)

}

export function enter_to_continue(){
    get_text('<ENTER>...')
    console.clear()
}

