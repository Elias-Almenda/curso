

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

erro = False

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
    erro = True
    
elif ' ' in nome:
    print('Seu nome contem espaços')
    erro = True


print(f"""
Nome: {nome}
Invertido: {nome[::-1]}
Quantidade de letras: {len(nome)}
Primeira letra: {nome[0]}
Última letra: {nome[-1]} 
""")