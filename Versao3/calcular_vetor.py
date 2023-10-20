"""
as funções calculam criando uma lista, e então coloca os valores nele.
caso seja o operador que a função calcula, ela faz a operação com o valor
anterior ao operador e posterior ao mesmo, e então coloca o resultado na 
posição anterior ao operador, e não adiciona o operador ou o valor posterior a ele
na lista, do contrário ele adiciona o valor e o operador para a próxima função calcular.
"""

def calcular_pow(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
        
    resultado=list()
    operador=None
    quantidade=0
    
    for i in operacao:
        if type(i) == str:
            #verifica se o operador não é do tipo desejado
            if i != "^" and i != "r":
                resultado.append(i)
                quantidade+=1
            else:
                operador=i
        else:
            #verifica se o operador é do tipo desejado
            if operador == "^":
                #modifica o resultado do indice anterior,e tira o indice da lista
                resultado[quantidade-1]**=i
                operador=None#zera o operador 
            elif operador == 'r':
                resultado.append(i**0.5)
                quantidade+=1
                operador=None#zera o operador 
            else:
                #adiciona o valor caso não seja possível realizar o cálculo
                resultado.append(i)
                quantidade+=1
            
    return resultado
 
 
def calcular_multiplicacao(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
        
    resultado=list()
    operador=None
    quantidade=0
    
    for i in operacao:
        if type(i) == str:
            if i != "*" and i != "/" and i != "%":
                resultado.append(i)
                quantidade+=1
            else:
                """if i == "%":
                    if(quantidade-1 < 0 ):
                        raise ValueError("Erro")
                    resultado[quantidade-1]/=100"""
                operador=i
        else:
            
            if operador == "*":
                resultado[quantidade-1]*=i
            elif operador == "/":
                if i == 0:
                    raise ValueError("Erro")
                resultado[quantidade-1]/=i
            else:
                resultado.append(i)
                quantidade+=1
            operador=None
        
    return resultado
    
def calcular_soma(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
    resultado=list()
    operador=None
    quantidade=0
    for i in operacao:
       
        if type(i) == str:
            if i != "+" and i != "-":
                resultado.append(i)
                quantidade+=1
            else:
                operador=i
        else:
            if operador == "+":
                resultado[quantidade-1]+=i
            elif operador == "-":
                resultado[quantidade-1]-=i
            else:
                resultado.append(i)
                quantidade+=1
            operador=None
    return resultado
    
    

"""
Percorre toda a lista procurando sub-listas, e então se chama dentro delas e pede
o resultado e coloca na posição que a lista oculpava, e então entrega a lista com os
operadores e valores para as funções, seguindo a ordem de precedencia, para que eles apenas
calculem as operações de seus operadores e mantenham o restante da lista intácta, e então
depois de passar por todos os operadores, ele retorna o resultado.
"""


def calcular(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
    resultado=list()
    
    for i in operacao:
        temp=i
        if type(i)==list:
            temp=calcular(i)
        resultado.append(temp)
        
    temp=[resultado[0]]
    for i in resultado[1:]:
        if type(temp[-1]) in [int,float] and type(i) in [int,float]:
            temp.append("*")
        elif type(temp[-1]) == type(i) == str:
            if temp[-1] in "-+" and i in "-+":
                temp[-1]="+" if temp[-1] == i else "-"
                continue
            else:
                raise ValueError("Erro")
        temp.append(i)
    resultado=temp
    resultado=calcular_pow(resultado) 
    resultado=calcular_multiplicacao(resultado)
    if resultado == "Erro":
        return "Erro"
    resultado=calcular_soma(resultado)  
    
    return resultado[0]
