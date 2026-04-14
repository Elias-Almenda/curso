# lista = [123, True, "Elias", 1.2, []]
# lista[-3] = 'Maria'



# print(lista)
# print(lista[2], type(lista[2]))


lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista [3]
# print(lista)
# print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
lista.append("BBBB")
ultimo_valor= lista.pop(3)

print(lista, "Removido",ultimo_valor)