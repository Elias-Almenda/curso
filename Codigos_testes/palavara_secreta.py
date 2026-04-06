"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os 

palavra_secreta = "Eyes"
letras_certas = ""
tentativas = 0

while True:
    letra_usuario = input("Digite uma letra: ")
    tentativas += 1
     
    if len(letra_usuario) > 1:
        print("Apenas uma letras")
        continue
    
    if letra_usuario in palavra_secreta:
        letras_certas += letra_usuario
    
    palavra_formada = ''
    for  letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print(tentativas)
    print("Palavra formada: ", palavra_formada)        
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("VOCÊ GANHOU!!!!")
        print("A Palavra era", palavra_secreta)
        print("Tentativas", tentativas)
        letras_certas = ""
        tentativas = 0
    