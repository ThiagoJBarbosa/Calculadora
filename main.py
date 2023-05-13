from funcoes import *


print(f'1 - SOMA \n'
      f'2 - SUBTRAÇÃO \n'
      f'3 - MULTIPLICAÇÃO \n'
      f'4 - DIVISÃO \n'
      f'5 - POTENCIAÇÃO \n'
      f'6 - PORCENTAGEM \n')

op = int(input(f'Qual operação você deseja fazer? '))

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

match op:
    case 1:
        soma = soma(n1,n2)
        print(f"Resultadoda soma: {soma}")
    case 2:
        sub = subtracao(n1,n2)
        print(f"Resultado da subtração: {sub}")
    case 3:
        mult = multiplicacao(n1,n2)
        print(f"Resultado da multiplicação: {mult}")
    case 4:
        divisao = divisao(n1, n2)
        print(f"Resultado da multiplicação: {divisao}")
