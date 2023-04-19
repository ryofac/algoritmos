import { question } from "readline-sync";
function main(){
    const char = question('Você é de que sexo? (M ou F)\n >> ')
    if (is_valid(char)){
        console.log('Anotado no sistema!')
    }
    else{
        console.log('Valor errado, digite novamente! ')
    }
}
function is_valid(txt){
    return txt === 'M' || txt === 'm' || txt ==='F' || txt === 'f'
}
main()