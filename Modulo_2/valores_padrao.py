


def soma(x, y=None, z = None):
    # Definição
    if z is not None:
        print(f'{x= } + {y= } + {z= }', x + y + z)
    else:
        print(f'{x= } + {y= }', x + y)
    
    
soma(1,2)
soma(8,9,0)
soma(z=8,y=9,x=0)
