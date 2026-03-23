"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int(input("Qual é a hora atual: "))
nome = input("Digite seu nome: ")

if 0 <= horario <= 11:
    print(f"Bom dia {nome}")
elif 12 <= horario <= 17:
    print(f"Boa tarde {nome}")
elif 18 <= horario <= 23:
    print(f"Boa noite {nome}")
else:
    print(f"Vai dormir {nome}")
    
    