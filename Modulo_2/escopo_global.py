x = 1

def escopo():
    
    x = 10 # Aqui é o escopo da funcao "escopo"
    
    def outra_funcao():
    
            y = 2
            x = 11 # Aqui ela pega o valor do escopo da "outra_funcao"
            print(x,y) # Esse print vai com o valor do escopo da "outra_funcao"
                    
    outra_funcao()
    print(x)  # Esse print vai com o escopo da funcao "escopo"
    
    
print(x)
escopo()
print(x) # Aqui ela pega o valor do escopo global


# def escopo():
    #   global x so o da funcao "escopo vira global"
#     x = 10 # Aqui é o escopo da funcao "escopo"
    

#     def outra_funcao():
#             y = 2
#             x = 11 # Aqui ela pega o valor do escopo da "outra_funcao" o desse não vira global continua o dela
#             print(x,y) # Esse print vai com o valor do escopo da "outra_funcao"
      
#     outra_funcao()
#     print(x)  # Esse print vai com o escopo da funcao "escopo"
