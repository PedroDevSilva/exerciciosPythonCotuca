function ex1() {
    let contador=1;
    let resultadoconsole="";
    let resultadordoc="";
    let numero1=10;
    let numero2=1;
    while (contador <=5 ) {
        resultadoconsole += (numero1 * contador) + ", ";
        resultadordoc+= (numero1 * contador ) + ", ";
        numero2=1;
        numero2=(numero2 * contador);
        for (indice=1 ; indice <=5; indice++) {
            resultadoconsole+=numero2+" ";
            resultadordoc+=numero2+" ";
        }
        resultadoconsole+='\n';
        resultadordoc+='<br>';
        numero2*contador;
        contador++;
    }
    console.log(resultadoconsole);
    document.write(resultadordoc);
}

function ex2() {
    let contador=1;
    let resultadoconsole="";
    let resultadordoc="";
    let numero1=1;
    let numero2=1;
    while (contador <=6 ) {
        if (contador % 2 == 0) {
            resultadoconsole += (numero1+1) + ", ";
            resultadordoc += (numero1+1) + ", ";
        } else {
            resultadoconsole += numero1 + ", ";
            resultadordoc += numero1+ ", "; 
        }
        for (indice = 1 ; indice <=5 ; indice++ ){
            resultadoconsole += numero2 + " ";
            resultadordoc += numero2 + " ";
            numero2 +=1;
        }
        resultadoconsole += "\n";
        resultadordoc += "<br>";
        numero2*contador;
        contador++;
    }
    console.log(resultadoconsole);
    document.write(resultadordoc);
}

function ex3() {
    let frase = prompt("Digite a palavra na qual deseja criptografar");
    let novafrase = frase.toLowerCase();
    let resultado = "";
    for (let indice = 0; indice < novafrase.length; indice++) {
        let letra = novafrase[indice];

        switch (letra) {
            case "a":
                resultado += "1";
                break;
            case "b":
            case "c":
            case "f":
            case "g":
            case "j":
            case "l":
            case "m":
                resultado += "@";
                break;
            case "e":
            case "o":
            case "u":
                resultado += "#";
                break;
            case "n":
            case "p":
            case "q":
            case "r":
            case "s":
            case "t":
            case "v":
                resultado += "&&";
                break;
            default:
                resultado += letra;
        }
    }

    alert(resultado);
    document.write(resultado);
}

function ex4() {
    let frase = prompt("Digite uma frase:");
    let novafrase=frase.toLowerCase;
    let resultado= "";

    for (let indice=0;indice<novafrase.length;indice++) {
        let letra=novafrase[indice];
        if (letra=='0' || letra == '1' || letra=='2' || letra=='3' || letra=='4' || letra=='5' || letra=='6' || letra=='7' || letra=='8' || letra=='9') {
            resultado +='&';
        }
        else if (indice%2!=0){
                resultado+=letra.LowerCase();
        }
        else {
            switch (letra.toUppercase()){
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                resultado+='@';
                break;
            default:
                resultado+=letra;
            }
        }
    }
    alert(resultado)
}