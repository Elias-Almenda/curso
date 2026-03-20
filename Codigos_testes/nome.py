

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
letra = nome[::]


if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
elif '' in nome:
    print('Seu nome contem espaços')
    
    
    

print(f"Seu nome é {nome} ele invertido é {nome[::-1]} , seu nome tem essa quantidade de letras= {len(nome)}")
print(f'A primeira letra do seu nome é {letra[0:1]}')
print(f'A ultima letra do seu nome é {nome[-1]}')
