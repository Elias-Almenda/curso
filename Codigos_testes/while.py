condicao = True

# while condicao:
#     nome= input("Qual seu nome: ")
#     print(f"Seu nome é {nome}")
#     if nome == "parar":
#         print("Você parou o loop")
#         break  
    
    
    
    
# contador = 0

# while contador <= 100:
#     contador += 1
    
#     if contador == 6:
#         print("Não quero o 6")
#         continue
    
#     if contador >= 10 and contador <= 27:
#         print("Quero não")
#         continue
    
#     print(contador)
    
    
#     if contador == 40:
#        break


# print("finalizou")

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    colunas = 1
    
    
    while colunas <= qtd_colunas:
        print(f"{linha=},{colunas=}")
        colunas += 1
    linha +=1
    

print("Acabou as linhas e colunas")


