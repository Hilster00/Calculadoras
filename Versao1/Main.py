#main
import os
import operacoes
from importar import importar_numero,importar_operacao

os.system("title Calculadora 1")
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
    
    elif operacao == "+":
        p=operacoes.soma(valor1,valor2)
    elif operacao == "-":
        p=operacoes.subtracao(valor1,valor2)
    elif operacao == "*":
        p=operacoes.multiplicacao(valor1,valor2) 
    elif operacao == "/":
        p=operacoes.divisao(valor1,valor2)
    elif operacao == "^" or operacao == "**":
        p=operacoes.potencia(valor1,valor2)
    elif operacao == "v":
        p=operacoes.raiz(valor1,valor2)
    else:
        p=f'Operacao {operacao} é inválida'
    print(p)
    os.system("pause")
    
