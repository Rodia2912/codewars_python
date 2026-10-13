def to_camel_case(text):
    # Cambiamos los guiones por guiones bajos para tener un solo separador
    text = text.replace("-", "_")

    # Separamos en palabras
    palabras = text.split("_")

    # La primera palabra se queda tal cual
    resultado = palabras[0]

    # Las demás las ponemos con la primera letra en mayúscula
    for i in range(1, len(palabras)):
        palabra = palabras[i]
        if palabra != "":
            resultado = resultado + palabra[0].upper() + palabra[1:]

    return resultado