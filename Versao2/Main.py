#main
import os
from calculo import *
from ajustes import ajustar

os.system("title Calculadora 2")
while True:

    operacao=ajustar(input("digite a operacao:"))
    
    if operacao.lower() == "sair":
        break
    try:
        print(f"resultado:{calculo(operacao)}")
    except ZeroDivisionError:
        print("ERRO, não é possível dividir por 0")
        continue
    except:
        print(f"{operacao} ainda não é suportada")
