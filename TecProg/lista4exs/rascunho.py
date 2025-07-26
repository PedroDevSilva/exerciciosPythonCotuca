import os
os.system('cls')

def separarComandos(frase):
    palavras = frase.split()
    comandos = ["\\t", "\\a", "\\b", "\\f", "\\n", "\\r", "\\v"]
    barra="\"
    
    frasePronta = ""  # inicializa fora do loop
    for i in range(len(palavras)):
        if palavras[i] in comandos:
            # Substituir o comando por "o"
            palavras[i] = palavras[i].replace("\\", "", 1)
            print(f"Substituído na posição {i}")
    
    frasePronta = " ".join(palavras)
    return frasePronta

print(separarComandos(r"\t o rato roeu a roupa do rei de roma"))

# Example of using string.join()
words = ["Python", "is", "awesome"]
separator = " "
sentence = separator.join(words)
print(sentence) # Output: Python is awesome
