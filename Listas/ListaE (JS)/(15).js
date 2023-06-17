import { question } from "readline-sync";
function main(){
    valor_hora_a = question('Qual o valor da hora do professor Adalberto? ')
    horas_a = question('Quantas horas ele dá por dia: ')
    valor_hora_b = question('Qual o valor da hora-aula do professor Bernardo?: ')
    horas_b = question('Quantas horas ele dá por dia?: ')

    salario_a = calcular_salario(valor_hora_a, horas_a)
    salario_b = calcular_salario(valor_hora_b, horas_b)
    if(salario_a > salario_b){
        console.log('Salário do professor Adalberto maior!')
    }
    if(salario_b > salario_a){
        console.log('Salário do professor Bernardo maior!')
    }
    else{
        console.log('Salarios iguais!')
    }
    console.log(`ADALBERTO R$${salario_a.toFixed(2)}`)
    console.log(`BERNARDO R$${salario_b.toFixed(2)}`)

function calcular_salario(horas, tempo){
    return tempo * horas
}
}