//1o Exercício:

function conferiridade() {
    alert("Digite seu nome e sua idade na próxima janela");
    nome=prompt("Digite seu nome: ");
    idade=prompt("Digite agora sua idade: ");
    if (idade<18) {
        alert(nome+", você ainda é menor de idade");
        console.log(nome+", você ainda é menor de idade")
    }
    else {
        alert(nome+", você já é maior de idade! ");
        console.log(nome+", você já é maior de idade! ")
    }
    
}


//2o Exercício:

function soma() {
    alert("Digite dois números e retornarei o total da soma entre eles!");

    let num1 = Number(prompt("Digite o primeiro número: "));
    let num2 = Number(prompt("Digite agora o segundo número: "));

    let total = num1 + num2;
    alert("A soma entre eles é: " + total);
}


//3o Exercício:

function calcular() {
    // usando number transforma em numeros, tambem da pra usar parseInt
    let num1 = Number(document.getElementById("num1").value);
    let num2 = Number(document.getElementById("num2").value);

    // Faz as contas básicas
    let soma = num1 + num2;
    let sub = num1 - num2;
    let mult = num1 * num2;
    let div = num1 / num2;
    let resto = num1 % num2;

    // SAi printando o texto com todas as operacoes
    let texto = "";
    texto += "Soma: " + soma + "<br>";
    texto += "Subtração: " + sub + "<br>";
    texto += "Multiplicação: " + mult + "<br>";
    texto += "Divisão: " + div + "<br>";
    texto += "Resto da divisão: " + resto;

    // printa na pagina da html
    document.getElementById("resultado").innerHTML = texto;
}

//4o Exercício:
//NAO ME MANDA FAZER MAIS PIRAMIDE NAO MARCIA PFV, EU N AGUENTO MAIS, O MALIGNO JA MATOU A GENTE C ISSO
function gerarpiramide() {
    let resultado = ""; //resultado = nada, depois adicionamos a quebra de linha e os demais numeros
    let a = prompt("Digite seu numero");  // comeca do numero 11
    let b = a;  

    // loop vai continuar enquanto a for maior que 1
    while (a >= 1) {
        for (let i = 0; i < b; i++) {
            if (a<10) {
                resultado += + " " + ""+ a + " ";  // se for menor q 10 bota espaco e o zero antes do a atual p alinhar
            } else {
                resultado += a + " ";
            }
        } 
        

        resultado += "\n";  // pula linha 
        a--;  // a passa pro proximo numero
        b--;  // b diminui quantidade de numeros na linha 
    }
    alert(resultado)
}
//MAXIMO QUE CONSEGUI, nao ta rodando e n sei o pq :/

//5o Exercício

function gerarnumero() {
    let numgerado = Math.floor(Math.random() * 9+1) ;
    console.clear
    console.log(numgerado)
    
    n1escolhido=prompt("Digite sua primeira tentativa: ");
    if (numgerado==n1escolhido) {
        alert("Cagada da porra, voce acertou!");
    } else n2escolhido=prompt("Digite sua segunda tentativa: ");
    if (numgerado==n2escolhido) {
        alert("Cagada da porra, voce acertou!");
    } else n3escolhido=prompt("Digite sua terceira tentativa: ");
    if (numgerado==n3escolhido) {
        alert("Cagada da porra, voce acertou!");
    } else alert("Vixi pai, errou tudo, clica no botao dnv pra tentar novamente");
    alert(numgerado+"<---- este foi o numero gerado");
}

//6o Exercício

function lerstring() { 
    string=prompt("Digite uma frase e retornarei o comprimento dela, desconsiderando os espacos: ");
    stringsemespaco=string.split(" ").join("");
    stringlida=stringsemespaco.length;
    alert(stringlida);
}

//7o Exercício 

function letrasparesmaiusculas() {
    let frase = prompt("Digite uma frase:");
    let novaFrase = "";

    // uso o i para indicara letra sendo lida, fazendo um loop com for para percorrer cada letra da frase
    for (let i = 0; i < frase.length; i++) {
    let caractere = frase[i];

    // se a posição for par (0, 2, 4...), transforma em maiscula
    if (i % 2 === 0) {
        novaFrase += caractere.toUpperCase();
    } else {
        novaFrase += caractere; // mantém como está
    }
    }

    alert("Frase com posições pares em maiúsculas:\n" + novaFrase);

}

//8o Exercício

function palindromo() {
    let texto = prompt("Digite uma palavra ou frase:");
    let textoLimpo = texto.toLowerCase().replace(/\s/g, ""); // remove espaços e deixa tudo minusculo

        // Inverte o texto
        let textoInvertido = textoLimpo.split("").reverse().join("");

        // Verifica se é palíndromo
        if (textoLimpo === textoInvertido) {
            alert("É um palíndromo ");
            document.write(textoLimpo+"------>"+textoInvertido)
        } else {
            alert("Não é um palíndromo.");
        }
}

//9o Exercício

function criptografia(){
    let frase = prompt("Digite uma frase para criptografar:");
    let criptografada = "";

    // Faz a troca letra por letra
    for (let letra of frase) {
    switch (letra.toLowerCase()) {
        case "a": // o case identifica se a letra (sendo minuscula), é igual a A, se for modifica variavel usando += para @, break quebra o loop
        criptografada += "@";
        break;
        case "e":
        criptografada += "X";
        break;
        case "i":
        criptografada += "#";
        break;
        case "o":
        criptografada += "$";
        break;
        case "u":
        criptografada += "WW";
        break;
        default:
        criptografada += letra; // se a letra n for vogal, adiciona mais uma posicao na letra, passando pra proxima
    }
    }

    alert("Frase criptografada: " + criptografada);

}

function contagem(){
    let frase = prompt("Digite uma frase:");
    let vogais = "aeiou";
    let alfabeto = "abcdefghijklmnopqrstuvwxyz";

    let qtdVogais = 0;
    let qtdConsoantes = 0;

    frase = frase.toLowerCase();

    for (let letra of frase) {
    if (alfabeto.includes(letra)) {
        if (vogais.includes(letra)) {
        qtdVogais++;
        } else {
        qtdConsoantes++;
        }
    }
    }

    alert("Quantidade de vogais: " + qtdVogais +"\nQuantidade de consoantes: " + qtdConsoantes);


}
