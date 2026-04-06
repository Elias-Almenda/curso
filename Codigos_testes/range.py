# numeros = range(0,10,2)

# for numero in numeros:
#     print(numero)
    
texto = "Elias"

iterador = iter(texto)

while True:
    try:
       letra = next(iterador)
       print(letra)
    except StopIteration:
        break

