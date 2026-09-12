# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# retorne o total para uma variavel e mostre o valor dela

def multiplicacao(*args):
    total = 1
    for num in args:
        total *= num
    
    return total


resultado = multiplicacao(5,3)
print(resultado)

print(5*3)


# def impar_par(i):
#     if i % 2 == 0:
#         print("Seu número é par")
#     else:
#         print("Seu número é impar")
        

# impar_par(3)


def par_impar(i):
    multiplo_dois = i % 2 == 0
    
    if multiplo_dois:
        return 'par'
    return'impar'


print(par_impar(2))
print(par_impar(3))
print(par_impar(6))