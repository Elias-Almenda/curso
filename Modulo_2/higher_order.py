def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)



# v = executa(saudacao, 'bom dia', 'elias')
# print(v)

print(
    executa(saudacao, 'bom dia', 'elias')
)

print(
    executa(saudacao, 'bom noite', 'elias')
)