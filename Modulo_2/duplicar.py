

numero = int(input("Digite o seu número: "))
def duplicar ():
    return numero * 2


def triplicar():
    return numero * 3
    

def quadriplicar():
    return numero * 4

duplicacao = duplicar()
print(f'O resultado da duplicação é {duplicar()}')
print(f'O resultado da triplicação é {triplicar()}')
print(f'O resultado da quadriplicação é {quadriplicar()}')


# def multiplicao():
    
#     def duplicar ():
#         return numero * 2
#     def triplicar():
#         return numero * 3
#     def quadra():
#         return numero * 4
#     return duplicar, triplicar,quadra



# duplicacao = multiplicao()
# triplicacao = multiplicao()
# quadri = multiplicao() 
# print(f'O resultado da duplicação é: {duplicacao()}')
# print(f'O resultado da triplicação é: {triplicacao()}')
# print(f'O resultado da quadriplicação é: {quadri()} ')


# careca version

def criar_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadriplicar = criar_multiplicacao(4)

print(f'{duplicar(2)}')
print(f'{triplicar(2)}')
print(f'{quadriplicar(2)}')