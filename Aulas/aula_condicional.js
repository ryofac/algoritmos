import { question } from "readline-sync"
/*
> Função pertence ao programa como um todo!
> Expressão: Unidade de código com valor >> o computador "avalia"
*/
const pi = 3.14 // Variável global (Fora do main()) > Pode ser usada por todo o programa

function main(){
    /* Expressões condicionais: 
    > São expressões que retornam valores lógicos (True ou False):
    >> Operadores relacionais: >, <, >=, <=, =, ===, !== : Expressões booleanas simples
    >> Operadores lógicos: &&(python: and), ||(python: or), !(python: not): Expressões booleanas compostas
    */
   
    const ms = 80
   const qnt_aulas = 100
   const qnt_faltas = 26

   if ((ms >= 7.5) && (qnt_faltas * 0.25)){
    console.log('True')
   }
   else{
    console.log('False')
   }
   

}

function imc(peso, altura){
    const imc = peso/altura**2 // Variável local(Destruída após o uso da função)
    // altura = 1.80 // Essa construção é errada!!, o parâmetro deve ser read_only
    return imc // Essencialmente, sem desempacotamento, a função só retorna uma variável
}
main()