

def criar_sudacao(saudacao):
    
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_sudacao('bom dia')
falar_boa_noite = criar_sudacao('boa noite')

# print(falar_bom_dia('elias'))
# print(falar_boa_noite('elias'))

for nome in['elias','julio','carol']:
    print(falar_boa_noite(nome))
    print(falar_bom_dia(nome))
