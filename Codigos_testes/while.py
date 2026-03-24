condicao = True

# while condicao:
#     nome= input("Qual seu nome: ")
#     print(f"Seu nome é {nome}")
#     if nome == "parar":
#         print("Você parou o loop")
#         break  
    
    
    
    
contador = int(input("Onde você gostaria que seu contador começase:  "))
tamanho_contador = int(input("Ate quanto você gostaria de contar: "))
while contador <= tamanho_contador -1 :
    contador = contador + 1
    print(contador)


print("finalizou")