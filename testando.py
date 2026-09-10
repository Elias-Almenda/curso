# limite = int(input("Até qual número você quer somar?: "))
# soma = 0

# for numero in range(limite + 1):
#      soma += numero
    
# print(soma)


# o soma += numero a cada volta do loop ele adiciona no soma o numero do for ate bater o range dele que é dado pelo limite
# ja o por que o soma no final inves de numero pq o numero ele esta rodando no for ate o limite do range então ele vai ate o 5
# ja o soma esta guardando tudo que foi somado nele ate bater o limite do for




# while True:
#     print ('Opção 1- Olá \nopção 2- Tudo bem? \nOpção 3- Sair')
#     escolha = input("Qual opção voce deseja? (1, 2 ou 3): ")
#     if escolha == '1':
#         print("Olá")
#     elif escolha == '2':
#         print("Tudo bem?")
#     elif escolha == '3':
#         break
#     else:
#         print("escolha uma das opções")

# negativos = 0
# positivos = 0
# zero = 0 
# for i in range(5):
#     escolha = int(input("Diga 5 números positivos ou negativos:"))
   
#     if escolha < 0:
#         negativos += 1
#     elif escolha > 0:
#         positivos += 1
#     elif escolha == 0:
#         zero += 1
        
# print(f"Voce tem\n{positivos} positvos\n{negativos} negativos \n{zero} zeros ")



# negativos = 0
# positivos = 0
# zero = 0 


# while True:
#     escolha = int(input("Digita quantos números tu quiser ai meu compatriota: "))
   
#     if escolha < 0:
#         negativos += 1
#     elif escolha > 0:
#         positivos += 1
#     else:
#         break

# print(f"Voce tem\n{positivos} positvos\n{negativos} negativos")

# Exercício — Caixa eletrônico

# Faça um programa que peça ao usuário um valor inteiro de dinheiro para saque.

# O programa deve:

# Verificar se o valor é positivo.
# Verificar se o valor é múltiplo de 10.
# Se for inválido, mostrar uma mensagem explicando o motivo.
# Se for válido, mostrar quantas notas de 100, 50, 20 e 10 serão entregues.
# O programa deve continuar pedindo um valor até que o usuário informe um valor válido.

# 1- pedir o núemro para o usuario
# 2- abrir um while True pq o usuario pode mandar um numero invalido
# 3- verificar se o numero é multiplo de 10
# 4- verificar se o número é positivo numero > 0 ai passa se não avisar que não passa pois é negativo
# 5- pego o número que o usuario quer sacar e pego o // do valor dele para ver quantas notas de 100 dá
# 6- depois pego e faço isso com o % da divisão dele para ver quantas notas diferentes vão ter que dar e vou divindo eles com o % ate chegar no resultado final
# 7- ir pegando o restante de cada % em uma variavel restante primeiro pega quantas cabem nela depois quanto sobrou para ai sim continuar
# 8- o progama continua enquanto o usuario não falar um número valido
# 9-
# 10-




# while True:
    
#     num_user = int(input("Quanto voce dejesa sacar?: "))
#     if num_user <= 0:
#         print("ele é negativo não pode prosseguir, digite um número valido")
#         continue
#     elif num_user % 10 !=0:
#         print("ele não é multiplo de 10 não pode prosseguir, digite um número valido")
#         continue
        
#     saque = num_user
#     notas_100 = saque // 100
#     saque = saque % 100
    
#     notas_50 = saque // 50
#     saque = saque % 50
    
#     notas_20 = saque // 20
#     saque = saque % 20
    
#     notas_10 = saque // 10  
    
#     print(f'Você ira receber {notas_100} de 100\n{notas_50} de 50\n{notas_20} de 20\n{notas_10} de 10')
#     break


# pedir 10 número dentro de um for
# verificar se eles são par ou impar
# criar uma variavel de par e impar para guardar neles
# e somar todos os pares e depois todos os impares


# pares = 0
# impares = 0
# soma_pares = 0
# soma_impares = 0

# for numero in range(10):
#     num_user = int(input("Digite 10 números: "))
#     if num_user % 2 == 0:
#         pares += 1
#         soma_pares += num_user
           
#     elif num_user % 2 != 0:
#         impares += 1
#         soma_impares += num_user
        

# print(f'Quantidade de pars: {pares}\nQuantidade de impars: {impares}\nSoma imp: {soma_impares}\nsoma pares: {soma_pares}')

# criar um for 
# pedir os 10 numeros inteiros
# criar as variaveis de posito, negativo, par e impar
# verificar quais são positivos 
# verificar quais são negativos
# verificar quais são pares
# verificar quais são impares
# somar todos os números
# pegar o maior número max()
# pegar o menor número min()

# par = 0
# impar = 0
# negativo = 0
# positivos = 0
# lista_numeros = []
# soma = 0

# for num in range(10):
#     num_user = int(input("Diga 10 números inteiros: "))
    
    
#     if num_user < 0:
#         negativo += 1
        
#     else:
#         positivos += 1
        
#     if num_user % 2 == 0:
#         par += 1
        
#     else:
#         impar += 1
         
#     soma += num_user
    
#     lista_numeros.append(num_user)
# maximo = max(lista_numeros)
# minimo = min(lista_numeros)

# print(f'par {par}\nimpar {impar}\nnegativos {negativo}\npositivos {positivos}\nlista de numeros {lista_numeros}\nmax {maximo}\nminimo {minimo}\nsoma{ soma}')



# criar uma lista nomes
# depois em um for enumerar esses nomes e mostrar para o usuario
# pedir para o usuario um nome e mostrar em qual posição esse nome esta
# caso não esteja falar que não esta


# nomes = ['Elias','João','Nick','Ana','Carlos']

# nome_user = input("Diga um dos nomes da lista: ")

# print(nomes)
# for indice, nome in enumerate(nomes, start= 1):
    
#     if nome_user == nome:
#         print(f'Esse nome está na lista o indice é: {indice}')
#         break
# else:
#     print("O nome não esta na lista")


# criar uma lista de alunos com listas dentro dos alunos
# depois em um for enumerar esses nomes e mostrar para o usuario
# pedir para o usuario um nome e mostrar em qual posição esse nome esta
# caso não esteja falar que não esta
# ver se a nota do alunos esta aprovada ou não >= 7


# alunos = [
#     ["Elias", 8.5],
#     ["João", 6.0],
#     ["Ana", 7.0],
#     ["Carlos", 4.0],
#     ["Nick", 9.5]
# ]
# print(alunos)

# alunos_user = input("Digite um nome de um aluno: ")


# for indice, nome in enumerate(alunos, start = 1):  
#     nota = nome[1] 
    
#     if alunos_user in nome:
#         print(f'Aluno é: {nome[0]}\nNota: {nome[1]}')
#         if nota >= 7:
#             print("Aprovado")
#         else:
#             print("Reprovado")  
#     break  
# else:
#     print(f'{alunos_user} não encontrado/não é um aluno')



# alunos = [
#      ["Elias", 8.5],
#      ["João", 6.0],
#      ["Ana", 7.0],
#      ["Carlos", 4.0],
#      ["Nick", 9.5]
#      ]

# soma = 0
# maior_nota = alunos[0][1]
# menor_nota = alunos [0][1]
# aluno_maior = alunos [0][0]
# aluno_menor = alunos [0][0]
# for indice, nome in enumerate(alunos, start = 1):
#          soma += nome[1] 
#          print(f'{indice} - {nome[0]}: {nome[1]}')
         
#          if nome[1] > maior_nota:
#              maior_nota = nome[1]
#              aluno_maior = nome[0]
#          if nome[1] < menor_nota:
#              menor_nota = nome[1]
#              aluno_menor = nome[0]

# media = soma / len(alunos)

# print(f'A media da turma: {media}')
# print(f'Maior nota: {aluno_maior} - {maior_nota}\nMenor nota: {aluno_menor} - {menor_nota}')







# print("Bem vindo a calculadora 2.0")


# while True:
#     num_user = int(input("Quanto você quer sacar?: "))
    
#     if num_user > 0 and num_user % 10 == 0:
#         saque = num_user
            
#         notas100 = saque // 100
#         saque = saque % 100
            
#         notas50 = saque // 50
#         saque = saque % 50
            
#         notas20 = saque // 20
#         saque = saque % 20
            
#         notas10 = saque // 10
#         saque = saque % 10
#         print(f'Notas de 100: {notas100}\nNotas de 50: {notas50}\nNotas de 20: {notas20}\nNotas de 10: {notas10}')
#         break     
#     else:
#         print("O número tem que ser positivo e multiplo de 10")
    



# lista = []
# while True:
#     escolha_user = input("O que voce deseja fazer\n [L] Listar [I] Inserir[A] Apagar [S] Sair?: ")
#     if escolha_user == "L":
#         for indice, nome in enumerate(lista, start=1):
#             print(f'{indice} - {nome}')
#     if escolha_user == "I":
#         inserir = input("O que voce deseja inserir?: ")
#         lista.append(inserir)
#     elif escolha_user == "A":
#         apagar = int(input("Qual indice você deseja apagar?: "))
#         apagar = apagar - 1
#         del lista[apagar]
#     elif escolha_user == "S":
#         print("saindo...")
#         break


inicial = float(input("Quanto voce deseja investir?: "))
taxa = float(input("Qual a taxa?: "))
meses = int(input("Em quantos meses?: "))

taxa = (taxa / 100) + 1

montante =  (taxa ** meses) * inicial

print(f'{montante:.2f}')