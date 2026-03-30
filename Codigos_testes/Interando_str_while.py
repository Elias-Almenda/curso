frase = 'O Python é uma linguagem de programação' \
    'multiparadigma' \
    'Python Foi criado por Guido Van Rossum.'
    
i = 0
qtd_apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase [i]
    
    if letra_atual == " ":
        i += 1
        continue
    
    qtd_atual = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_que_mais_apareceu = letra_atual
        
    i += 1
    
print("a letra que apareceu mais vezes foi " 
    f"'{letra_que_mais_apareceu}' que apareceu "
    f"{qtd_apareceu_mais_vezes}x vezes"
)
