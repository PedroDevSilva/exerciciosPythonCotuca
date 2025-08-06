def expandir_intervalos(texto):
    resultado = ""
    i = 0
    while i < len(texto):
        if i+2 < len(texto) and texto[i+1] == '-' and texto[i].isalnum() and texto[i+2].isalnum():
            inicio = texto[i]
            fim = texto[i+2]
            if ord(inicio) <= ord(fim):
                for c in range(ord(inicio), ord(fim)+1):
                    resultado += chr(c)
                i += 3  # Pula o padrão <Char>-<Char>
            else:
                resultado += texto[i]
                i += 1
        else:
            resultado += texto[i]
            i += 1
    return resultado

# Teste
entrada = "qweA-Epio0-4mbn"
saida = expandir_intervalos(entrada)
print(saida)  # Deve imprimir: qweABCDEpio01234mbn
