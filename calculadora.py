import modulo_matematico

print("Bem-vindo(a) Calculadora")

while True:
  print("\n1. somar\n2. multiplicar\n3. subtrair\n4. divisão\n5. potencia \n6. raiz\n7. juros compostos\n8. sair")
  choice = input("Escolha: ")
  if choice == '8':
        print("Saindo...")
        break

  elif choice == '6':
        print("\nTipos de raiz:")
        print("2 - Raiz quadrada")
        print("3 - Raiz cúbica")
        print("4 - Raiz quarta")
  if choice == '7':
    i = float(input("Qual o valor inicial?: "))
    t = float(input("Qual a taxa?: "))
    m = int(input("Quantos meses?: "))
    
    print(f'O resultado do seu juros é: {modulo_matematico.juros_composto(i,t,m,):.2f}')
    
  else:
     n1 = float(input("Digite o primeiro número: "))
     n2 = float(input("Digite o segundo número: "))  
  
  if choice == '1':
      print(f'Resultado da soma de {n1} e {n2} é: ',modulo_matematico.somar(n1,n2))
  elif choice == '2':
      print(f'Resultado da multiplicação de {n1} e {n2} é: ',modulo_matematico.multiplicar(n1,n2))
  elif choice == '3':
      print(f'Resultado da subtração de {n1} e {n2} é: ',modulo_matematico.subtrair(n1,n2))
  elif choice == '4':
      print(f'Resultado da divisão de {n1} e {n2} é: ',modulo_matematico.divisao(n1,n2))
  elif choice == '5':
      print(f'Resultado da potencia/raiz de {n1} e {n2} é: ',modulo_matematico.potencial(n1,n2))
  elif choice == '6':
      print(f'Resultado da raiz de {n1} e {n2} é: ',modulo_matematico.raiz(n1,n2))
  elif choice == '7':
      continue
  else:
      print("Opção inválida.")