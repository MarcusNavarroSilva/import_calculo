import math
import calculo
op  = 0
while True:
    print
    ("""
         Selecione a opção 
         1 - dobro
         2 - triplo
         3 - quadrado
         4 - sair
         """ )
    op = int(input("digite sua opção "))
    num =int(input("digite o seu numero "))
    
    if op == 1:
        num = calculo.dobro(num)
        print(num)
    elif op == 2:
        num = calculo.triplo(num)
        print(num)
    elif op == 3:
        num = calculo.quadrado(num)
        print(num)
    elif op == 4:
        break
    else:
        print("opção inválida") 