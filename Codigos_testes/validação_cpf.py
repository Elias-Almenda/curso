cpf = '55432765080'
nove_digitos = cpf [:9]

contador_1 = 10
contador_2 = 11

resultado_1 = 0
resultado_2 = 0

for digito in nove_digitos:
    
    resultado_1 += int(digito) * contador_1
    contador_1 -= 1

primeiro_digito = (resultado_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = nove_digitos + str(primeiro_digito)

for digito_2 in dez_digitos:
    
     resultado_2 += int(digito) * contador_2
     contador_2 -= 1
     
segundo_digito = (resultado_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

onze_digitos = dez_digitos + str(segundo_digito)
cpf_python = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_python:
    print(f'{cpf_python} valido')
else:
    print(f'{cpf_python} invalido')