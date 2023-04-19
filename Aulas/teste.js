function main() {
    // Só os True vão entender:
    const media_peso = (elementos, num_elementos) => elementos / num_elementos;

    // ================== ESTADO INICIAL ========================
    let peso_maior = -Infinity;
    let peso_menor = Infinity;
    let id_menor = null;
    let id_maior = null;
    let soma_peso = 0;
    let qnt_boi = 0;
    console.log(' = = = - BOI - = = =');
    let num_id = Number(prompt('ID: '));
    // ===========================================================

    while (num_id !== 0) { // -> CONJUNÇÃO DE CONTINUIDADE

        // ================== TRABALHO ========================
        let peso = Number(prompt('PESO (@): '));
        soma_peso += peso; // soma_peso = peso + soma_peso
        qnt_boi += 1; // qnt_boi = qnt_boi + 1
        if (peso_maior < peso || peso_maior === 0) {
            peso_maior = peso;
            id_maior = num_id;
        }
        if (peso_menor > peso || peso_menor === 0) {
            peso_menor = peso;
            id_menor = num_id;
        }
        console.log(' = = = - BOI - = = =');
        num_id = Number(prompt('ID: '));
    }
    // =====================================================

    // CONVERGÊNCIA DE DADOS: Não é muito explícito, no caso, o programa
    // se encerra quando id = 0 ( Chequei no GPT )

    // ================== SAÍDA ========================
    if (!id_maior && !id_menor) { // Fail Fast
        console.log('Sem valores!');
        return;
    }
    alert(`==== PESO MAIOR =====
>>>, peso_maior, 
ID: ${id_maior}
==== PESO MENOR =====
>>> peso_menor
ID: ${id_menor}
===== MÉDIA TOTAL PESOS ====
MÉDIA: ${media_peso(soma_peso, qnt_boi).toFixed(2)}`)
}

main();
