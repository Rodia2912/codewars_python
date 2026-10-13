def permute_a_palindrome(input):
    impares = 0
    for caracter in set(input):
        if input.count(caracter) % 2 == 1:
            impares += 1
    return impares <= 1