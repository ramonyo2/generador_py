import random
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "z"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letras_seleccionadas = random.choices(abecedario, k=10)
numeros_seleccionados = random.choices(numeros, k=20)
numeros_seleccionados = list(map(str, numeros_seleccionados))
combinacion = letras_seleccionadas + numeros_seleccionados
cadena_resultante = ''.join(combinacion)
print(cadena_resultante)
