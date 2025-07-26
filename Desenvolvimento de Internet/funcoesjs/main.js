const nomes=['Pedro','Gabriel','Luke','Maria','Roberto','João'];
const meunome=nomes[0];
document.write(`Seu nome é ${meunome}`);

nomes.push('Rogério'); //Insere no final da lista
document.write(`<br><br>Conteúdo da lista com item adicionado no fim= ${nomes}`);

nomes.unshift('Marcos'); //Insere no começo da lista
document.write(`<br><br>Conteúdo da lista com item adicionado no começo= ${nomes}`);

nomes.pop(); //deleta ultimo item da lista
document.write(`<br><br>Conteudo da lista com item deletado= ${nomes}`);

//nomes[3]='Eduardo'; // substitui item
//document.write(`<br>Conteudo da lista ${nomes}`)

const nomesOrdernadosAlfa=nomes.sort(); //ordena
document.write(`<br><br>Conteudo da lista ordenada= ${nomesOrdernadosAlfa}`);

//MAP aplica algo a cada elemento de uma lista

const numeros=[1,3,4,10,78,99,7,43];
const numerosMultiplicadosPorCinco=numeros.map(function(numeros) { //map recebe funcao e aplica a todos os itens da lista, ou alguns
    return numeros * 5;
})
document.write(`<br><br>Conteudo da lista de numeros= ${numeros}`);
document.write(`<br>Conteudo da lista de numeros multiplicados por 5= ${numerosMultiplicadosPorCinco}`);

const idades=[17,22,34,66,35,99,81,100];
const idadesPares=idades.filter(function(idades){//filter recebe condição e filtra ne po
    return idades % 2 == 0;
})
document.write(`<br><br>Conteudo da lista de idades= ${idades}`);
document.write(`<br>Conteudo da lista de idades pares= ${idadesPares}`);

const somaDasIdades=idades.reduce(function(idades,resultado){//realiza alguma operação em relacao aos itens da lista
    return resultado+idades
});
document.write(`<br><br>Conteudo da lista de idades= ${idades}`);
document.write(`<br>Conteudo da lista com soma das idades= ${somaDasIdades}`);
