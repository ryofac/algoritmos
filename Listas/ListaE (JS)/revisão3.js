import { question } from "readline-sync";
function main(){
    const carta_credito = Number(question('Digite o valor da sua carta de crédito \n> R$'))
    const parcelas = Number(question('Digite o número de parcelas por mês \n > '))
    const quer_lance = question('Como você quer ser contemplado? \n1- Por Lance\n2 - Por sorteio\n>> ')
    lance(quer_lance, carta_credito)
    
    
    if(!isNumber(quer_lance) || 0 > quer_lance > 2){ // Fail fast
        console.log('Valor inválido!')
        return 
    }


    const taxa_adm = porcento(carta_credito, 0.5)
    const fundo_reserva = porcento(carta_credito, 1)
    const parcela_mensal = Math.round((carta_credito / parcelas) + taxa_adm + fundo_reserva) // Taxação
  

    
    console.log(`Valor da parcela mensal: R$${parcela_mensal}`)
    console.log(`Isso com uma taxa de admnistração de R$${taxa_adm} e um fundo reserva de R$${fundo_reserva}`)

}
function porcento(number, por_cento){
    return number * por_cento / 100
}

function lance(resposta, carta_credito){
    if (resposta == 1){
       const valor_lance = question('Qua o valor do lance? \n >> ')
       if(valor_lance >= porcento(carta_credito,20)){
        console.log('Você será contemplado por lance')
       }
       else{
        console.log('Você não tem valor de carta suficiente, seu lance será por sorteio')
       }

    }
    else{
        console.log('Você será contemplado por sorteio')
    }
}
function isNumber(value){
    return value * 0 == 0 // Para verificar se é número, analisa se o valor x 0 é igual a 0
}

main()