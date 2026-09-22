pessoa = {
    
}


chave = 'primeiro_nome'



pessoa[chave] = 'elias' #adcionando algo nela
pessoa['sobrenome'] = 'padilha'

print(pessoa[chave])

pessoa[chave] = 'julia'


# del pessoa['sobrenome']

# print(pessoa)


if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
    