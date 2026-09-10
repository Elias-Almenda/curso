salas = [
    ['Maria', 'Helena', ],  # 0

    ['Elaine', ],  # 1
    
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

lista = ["A","B",[1,2,3],"C"]

a,b, *_, c = lista
# Funciona para strings tuplas e listas resumindo tudo que é interavel

print(a,b,c)
print(*salas, end= ' ', sep= '\n')