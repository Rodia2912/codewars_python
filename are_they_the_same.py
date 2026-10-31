def comp(a1, a2):
    contador = 0
    if a2 is None or a1 is None:
        return False
    lado1 = sorted([numero ** 2 for numero in a1])
    lado2 = sorted(a2)
    if (len(lado1)) == (len(lado2)):
        pass
    else:
        return False
    for numeros in range(len(lado1)):
        if lado2[numeros] == lado1[numeros]:
            contador +=1
              
    return contador == (len(lado1))
        