import { question } from "readline-sync";

function main(){
    const num1 = Number(question('Digite o número: '))
    const num2 = Number(question('Digite o número: '))
    const num3 = Number(question('Digite o número: '))
    const num4 = Number(question('Digite o número: '))
    const num5 = Number(question('Digite o número: '))

    media = (num1 + num2 + num3 + num4 + num5) / 5

    if(num1 > media){
        console.log(num1)
    }
    if(num2 > media){
        console.log(num2)
    }
    if(num3 > media){
        console.log(num3)
    }
    if(num4 > media){
        console.log(num4)
    }
    if(num5 > media){
        console.log(num5)
    }
    console.log('Valores maiores que a média')
    console.log(`MEDIA: ${media}`)
    
}
main()