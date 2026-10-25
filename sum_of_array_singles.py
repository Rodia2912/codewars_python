def repeats(arr):
    from collections import Counter
    no_rep = list(arr)
    conteo = Counter(no_rep)
    resultado = [x for x in no_rep if conteo[x] == 1]
    suma = sum(resultado)
    return suma