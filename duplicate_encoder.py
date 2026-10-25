def duplicate_encode(word):
    from collections import Counter
    palabra = word.lower()
    resultado = ""
    conteo = Counter(palabra)
    for caracter in palabra:
        if conteo[caracter] == 1:
            resultado += "(" 
        else:
             resultado += ")"
    return resultado
