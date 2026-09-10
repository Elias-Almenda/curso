# texto = "Python"

# novo_texto = " "

# for letra in texto:
#     novo_texto += f"*{letra}"
    
#     print(letra)
    
# print(novo_texto)


for i in range (10):
    if i == 2:
        print("i é 2, pulando...")
        continue
    
    if i == 8:
        print("i é 8, seu else não será feito")
        break
    for j in range (1,3):
         print(i,j)
else:
    print("For terminado")
