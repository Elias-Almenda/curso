pessoa = {
    'nome': 'elias',
    'sobrenome': 'padilha',
    'idade': '18',
    'altura': '1,75',
    'endereços': [
        {'rua': 'bla bla', 'número': 123},
        {'rua': 'bla tla', 'número': 321},
    ],
    
}

# pessoa = {} dicionario
# pessoa = [] lista
# pessoa = dict(nome = 'elias', sobrenome = 'padilha') conversão 

print(pessoa['nome'])

print(pessoa['sobrenome'])

for i in pessoa:
    print(i, pessoa[i])