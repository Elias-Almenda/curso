"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = float(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print(f"O {numero} é par")
else:
    print(f"O {numero} não é par")
    

if numero % 1 == 0:
    print(f"O {numero} é inteiro")
else:
    print(f"O {numero} não é inteiro")