frase = '           olha so que, daora            '

lista_frases = frase.split(', ')
lista_nova = []
for i, frase in enumerate(lista_frases):
    
    lista_nova.append(lista_frases[i].strip()) 

# print(lista_frases,lista_nova)

frases_unidas = ' - '.join(lista_nova)

print(frases_unidas)