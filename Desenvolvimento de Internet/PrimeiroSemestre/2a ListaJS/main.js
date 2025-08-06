function calcularSalario() {
  let nome = prompt("Digite seu nome:");
  let salario = parseFloat(prompt("Digite seu salário:"));
  let novoSalario = salario * 1.15;

  alert("Olá " + nome + ", seu novo salário é R$ " + novoSalario.toFixed(2));
  document.write("Olá " + nome + ", seu novo salário é R$ " + novoSalario.toFixed(2));
}

function verificarTriangulo() {
  let a = parseInt(prompt("Digite o valor do lado A:"));
  let b = parseInt(prompt("Digite o valor do lado B:"));
  let c = parseInt(prompt("Digite o valor do lado C:"));

  if (a < b + c && b < a + c && c < a + b) {
    if (a === b && b === c) {
      alert("Triângulo EQUILÁTERO");
    } else if (a === b || a === c || b === c) {
      alert("Triângulo ISÓSCELES");
    } else {
      alert("Triângulo ESCALENO");
    }
  } else {
    alert("Essas medida nao fazem um triangulo.");
  }
}

function calcularValor() {
  let preco = parseFloat(prompt("Digite o preço do produto:"));
  let parcelas = parseInt(prompt("Digite a quantidade de parcelas:"));
  let final = preco;

  if (parcelas === 1) {
    // sem valor extra, no caso a vista
  } else if (parcelas >= 1 && parcelas <= 3) {
    final = preco * 1.10;
  } else if (parcelas >= 4 && parcelas <= 10) {
    final = preco * 1.19;
  } else if (parcelas > 10) {
    final = preco * 1.20;
  }

  alert("Mano, o valor a ser pago é de R$ " + final.toFixed(2));//esqueci de falar, o .tofixed(x) printa a quantidade de casas decimais q estao entre o parenteses
}

function calcularMedia() {
  let nome = prompt("Digite seu nome:");
  let n1 = parseFloat(prompt("Digite a nota N1:"));
  let n2 = parseFloat(prompt("Digite a nota N2:"));
  let n3 = parseFloat(prompt("Digite a nota N3:"));

  let media = (0.2 * n1) + (0.3 * n2) + (0.5 * n3);
  let mensagem = "";

  if (media > 0 && media < 3) {
    mensagem = "Tu repetiu mano";
  } else if (media >= 3 && media < 5) {
    mensagem = "Vai ter que revisar as parada ae mano";
  } else {
    mensagem = "Passou direto fi, brabo";
  }

  alert("Ae " + nome + ", sua média é " + media.toFixed(2) + ". " + mensagem);
}

function verificarNumero() {
  let numero = parseInt(prompt("Digite um número:"));

  if (numero % 2 === 0) {
    alert("O número " + numero + " é PAR.");
  } else {
    alert("O número " + numero + " é ÍMPAR.");
  }
}
