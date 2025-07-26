let primeironome = 'Pedro';
let sobrenomne = 'Silva';
let frase = 'O rato roeu a roupa do rei de Roma';

frase1 = 'cOlEgIo Do coTUCa UiuUi';
console.log('MAIUSCULO = ' + frase1.toUpperCase());
console.log('minusculo = ' + frase1.toLowerCase());

let lista  = ['alberto','rogerio','armando','zico'];
lista.push('juliana');
lista.unshift('Matheus');

(lista+1);

console.log(lista);

function pegarPedacoFrase () 
{
    alert("Exibindo a SubString da primeira posição à decima primeira posição de FRASE = " + frase.substring(5,15)) ;
} 

function substituicao ()
{
    let meunome="Pedroca";
    let saudacao="Olá, nome, tudo bem com você";
    alert("Substituição de strings = "+saudacao.replace("nome",meunome));
}

function contador ()
{
    let contador = 1;
    while (contador <=10)
    {
        console.log(contador);
        contador+=1;
    }
}