velocidade = int(input('Qual era a sua velocidade: '))
local_carro = int(input('Qual era o seu KM: '))

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

inicio_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
fim_radar1 = local_carro <= (LOCAL_1 + RADAR_RANGE) 

carro_passou_radar1 = inicio_radar1 and fim_radar1
vel_carro_pass_radar1 = velocidade > RADAR_1

carro_multado_radar1 = carro_passou_radar1 and vel_carro_pass_radar1

if carro_passou_radar1 and vel_carro_pass_radar1:
    print('Você excedeu o limite de velocidade')

if carro_passou_radar1:
    print("Carro passou por radar 1")

if carro_multado_radar1:
    print("Carro multado em radar 1")