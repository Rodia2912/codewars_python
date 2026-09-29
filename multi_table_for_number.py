def multiTable(n):
    multiplo = 1
    resultado = ""

    while multiplo <= 10:
        if multiplo == 10:
            resultado += f"{multiplo} * {n} = {multiplo * n}\n"
        else:
            resultado += f"{multiplo} * {n} = {multiplo * n}\n"
        multiplo += 1

    return resultado


print(multiTable(5))
