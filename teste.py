# senha = input("Digite sua senha:") or "Você não digitou nenhuma senha"

# print(senha)


# senha = input("Digite sua senha:")

# if not senha:
#     print("digitou nada rapaz")

nome = input('Digite o seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if not encontrar or not nome:
    print("tem que digitar algo chefe")
    
elif encontrar in nome:
    print(f'{encontrar= } está em {nome= }')
    
else:
    print(f'{encontrar= } não esta em {nome= }')
   