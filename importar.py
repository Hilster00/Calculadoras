#importar
import os

def importar_numero():

    while True:
        sinal=""
        os.system("cls")
        valor=input("Digite um numero:")
        
        if valor != "":
            if valor[0] == "-":
                    valor=valor[1:]
                    sinal="-"

        if valor.isnumeric() == True or valor.lower() == "sair":
            break
    valor=f"{sinal}{valor}"
    
    return valor

#operacao
def importar_operacao():

    operacoes=["+","-","*","/","**","^","v","sair"]
    while True:
        os.system("cls")
        operacao=input("Digite a operacao desejada (+, -, /, *, [** ou ^], v):")
        if operacao.lower() in operacoes:
            break

    return operacao
