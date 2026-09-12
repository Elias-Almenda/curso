# x,y,*resto = 1,2,3,4
# print(x,y,*resto)

# def soma(x,y):
#     return x + y

def soma(*args):
    total = 0 
    for num in args:
        total += num
    return total

soma_1_2_3 = soma (1,2,3)
print(soma_1_2_3)

numeros = 1,2,3,4,5,6,10,67

soma_4_5_6 = soma (*numeros)
print(soma_4_5_6)



# print(sum(numeros))