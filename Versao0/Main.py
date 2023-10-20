#main
import os
from soma import soma
from subtracao import subtracao
from divisao import divisao
from multiplicacao import multiplicacao
from importar import importar_numero
from importar import importar_operacao

os.system("title Calculadora 0")
while True:

    valor1=importar_numero()

    if valor1 == "sair":
        break
    
    operacao=importar_operacao()
    if operacao == "sair":
        
        break

    valor2=importar_numero()
    if valor2 == "sair":
        break

    os.system("cls")
    if operacao == "+":
        print(soma(valor1,valor2))

    elif operacao == "-":
        print(subtracao(valor1,valor2))

    elif operacao == "*":
        print(multiplicacao(valor1,valor2))  
        
    else:
        print(divisao(valor1,valor2))
    os.system("pause")
