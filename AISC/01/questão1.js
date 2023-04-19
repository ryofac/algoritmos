import { question } from "readline-sync";
function main(){
    console.log('Olá, posso simular seu FIES!\nVamos começar...')
    const tempo_anos = Number(question("Duração do curso (em anos): \n >> "))
    console.log(`Ok, então vão ser ${periodos(tempo_anos)} períodos, boa sorte!`)
    const valor_mensalidade = Number(question("Valor da mensalidade:  \n >> "))
    const selic = Number(question("Valor atual da SELIC \n >> "))
    const salario_min = Number(question("Valor atual do Salário Mínimo \n >> R$"))
    const renda_familiar = Number(question("Renda Familiar\n >> R$"))
    const tamanho_familia = Number(question("Quantas pessoas na família \n >> "))
    const ano_inicial = Number(question("Ano de início \n >> "))
    const semestre_inicial = Number(question('Semestre de início \n >> '))
   
    const percapita = calcular_percapita(renda_familiar, tamanho_familia, salario_min)

    // Verifica se vai ser aprovado ou não
    if (!is_aproved(percapita, salario_min)){ // Fail Fast
        console.log('Você não foi aprovado para o FIES!')
        return 
    }
    
    const duracao = anos_meses(tempo_anos)

     // Calcula o valor a ser financiado
    const financiamento = calcular_financiamento(valor_mensalidade, duracao)
    

    // Valor pago durante o curso
    const valor_pago = pago_durante_curso(duracao)


    // Calcula a quantidade total de juros
    const juros = calcular_juros(financiamento, selic, percapita, salario_min, tempo_anos)
    const juros_totais = juros - valor_pago // Valor pago durante o curso é descontado no juros

    // Valor total a pagar (por enquanto)
    const valor_total = juros_totais + financiamento

    // Valor carência
    const carencia = calcular_carencia()

    // Valor total com descontos
    const valor_total_final = (valor_total - carencia - valor_pago)

    // Valor parcela
    console.log(`OK, você foi aprovado, o valor total deu R$${valor_total.toFixed(2)}`)
    const parcelamento = Number(question('Você quer parcelar em quantas vezes? '))
    if (parcelamento > (duracao * 4)){
        print('Valor não apto para o parcelamento')
        return 
    }
    const parcela = calcular_parcela(parcelamento, valor_total_final)
    
    // Mínimo de Renda do Aluno:
    const minimo_renda = (parcela * 10).toFixed(2)

    // Saída
    new_line()
    console.log('RESULTADO FINAL: ')
    new_line()
    console.log(`VALOR A SER FINANCIADO: R$${financiamento}`)
    console.log(`VALOR DA TAXA SELIC: ${selic}%`)
    console.log(`VALOR DOS JUROS R$${juros}`)
    console.log(`JUROS TOTAIS(com o desconto da carência) R$${juros_totais}`)
    console.log(`VALOR A SER PAGO NO CURSO: R$${valor_pago}`)
    console.log(`VALOR A SER PAGO NA CARÊNCIA: R$${carencia}`)
    new_line()
    console.log(`VAlOR COM DESCONTOS: ${valor_total_final}`)
    console.log(`VALOR A SER PAGO POR PARCELA: R$${parcela}`)
    console.log(`Valor mínimo de renda para aplicar: R$${minimo_renda}`)
    console.log('* considerando 10% do salário')
    new_line()
}

    
function calcular_parcela(parcelamento, valor_total){
    return valor_total / parcelamento
}
function calcular_percapita(salario, pessoas){
    return salario / pessoas
}
function is_aproved(percapita, salario_min){
    return percapita <= (3 * salario_min)

}

function calcular_financiamento(mensalidade, duracao){
    return mensalidade * duracao

}
function anos_meses(anos){
    return anos * 12

}

function calcular_juros(valor, selic, percapita, salario_min, tempo_anos){
    const taxa = calcular_taxa(percapita, salario_min, selic)
    return valor * taxa * tempo_anos
}

function calcular_taxa(percapita, salario_min, selic){
    if (percapita <= 1.5 * salario_min){
        return 0.1 * (selic/100)
    }else if (percapita <= 2  * salario_min){
        return 0.15 * (selic/100)

    }else if (percapita <= 2.5 * salario_min){
        return 0.20 * (selic/100)
    }
    else{
        return 0.25 * (selic/100)
    } 

}

function calcular_carencia(){
    return 18 * 50
}

function pago_durante_curso(tempo_curso){
    return Math.floor(tempo_curso / 3) * 50

}
function periodos(anos){
    return anos * 2
}
function new_line(){
    console.log('='.repeat(50))
}
// function semestre_final(ano_inicial, semestre_inicial, duracao_meses){
//     if ((ano_inicial * 12) / duracao_meses > 6) 
// }

main()