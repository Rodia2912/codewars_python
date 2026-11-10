def duplicate_encode(word):
    contador = {}
    resultado = ""
    for letra in word.lower():
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    for letra in word.lower():
        if contador[letra] > 1:
            resultado += ")"
        else:
            resultado += "("
    return resultado





if __name__ == "__main__":

    assert(duplicate_encode("din") == ("((("))
    assert(duplicate_encode("recede")==("()()()"))
    assert(duplicate_encode("Success")==(")())())"))
    assert(duplicate_encode("(( @") == ("))(("))