import math
"""
as funções calculam criando uma lista, e então coloca os valores nele.
caso seja o operador que a função calcula, ela faz a operação com o valor
anterior ao operador e posterior ao mesmo, e então coloca o resultado na 
posição anterior ao operador, e não adiciona o operador ou o valor posterior a ele
na lista, do contrário ele adiciona o valor e o operador para a próxima função calcular.
"""
def fat(n):
    r=1
    for i in range(2,n+1):
        r*=i
    return r
operadores={
	"sen":[lambda n:math.sin(math.radians(n)),
	lambda n:math.sin(n)],
	"cos":[lambda n:math.cos(math.radians(n)),
	lambda n:math.cos(n)],
	"tan":[lambda n:math.tan(math.radians(n)),
        lambda n:math.tan(n)],
        "sen'":[lambda n:math.asin(n),
	lambda n:math.degrees(math.asin(n))],
	"cos'":[lambda n:math.acos(n),
	lambda n:math.degrees(math.acos(n))],
	"tan'":[lambda n:math.atan(n),
	lambda n:math.degrees(math.atan(n))],
	"log":lambda n: math.log(n,10),
	"ln":lambda n: math.log(n,math.e),
	"lg":lambda n: math.log(n,2),
	"fat":lambda n: fat(n),
	"!": lambda n: fat(n),
	"^": lambda n,m:n**m,
	"r": lambda n: n**0.5,
       
}

def calcular_especial(operacao=[None],radiano=True):
    if len(operacao) == 0:
        raise ValueError("ERRO")    
    resultado=list()
    operador=None
    quantidade=0
    for i in operacao:
        if type(i) == str:
            #verifica se o operador não é do tipo desejado
            if i not in(["^","r","sen","cos","tan","som","fat","!","log","ln","lg","sen'","cos'","tan'"]):
                resultado.append(i)
                quantidade+=1
            else:
                operador=i
        else:
            if operadores.get(operador) != None:
                fun=operadores[operador]
                
                #funcao aplicada ao ultimo numero
                if operador in "^!":
                    #funcao de duas entradas
                    if operador == "^":
                        resultado[quantidade-1]=fun(resultado[quantidade-1],i)
                    else:
                        resultado[quantidade-1]=fun(i)
                        
                #funcao aplicada ao proximo numero
                else:
                    
                    #verifica se esta em radiano ou nao
                    if operador in ["sen","cos","tan","sen'","cos'","tan'"]:
                        fun=fun[0]if radiano else fun[1]
                        
                    resultado.append(fun(i))
                    quantidade+=1
                    
                operador=None
            
           
            else:
                #adiciona o valor caso não seja possível realizar o cálculo
                resultado.append(i)
                quantidade+=1
    if operador != None:
        if operador == "!":
            resultado[quantidade-1]=fat(resultado[quantidade-1])
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
                if i == "%":
                    if(quantidade-1 < 0 ):
                        raise ValueError("Erro")
                    resultado[quantidade-1]/=100
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
    resultado=operacao[0]
    operador=None
    for i in operacao:
        if type(i) == str:
                operador=i
        else:
            if operador == "+":
                resultado+=i
            elif operador == "-":
                resultado-=i
            operador=None   
    return resultado
    
    

"""
Percorre toda a lista procurando sub-listas, e então se chama dentro delas e pede
o resultado e coloca na posição que a lista oculpava, e então entrega a lista com os
operadores e valores para as funções, seguindo a ordem de precedencia, para que eles apenas
calculem as operações de seus operadores e mantenham o restante da lista intácta, e então
depois de passar por todos os operadores, ele retorna o resultado.
"""


def calcular(operacao=[None],radiano=True):
    if len(operacao) == 0:
        raise ValueError("ERRO")
    resultado=list()
    
    for i in operacao:
        temp=i
        if type(i)==list:
            temp=calcular(i,radiano)
        resultado.append(temp)
    temp=[]
    for i in resultado:
        if i == "π":
            temp.append(math.pi)
        elif i == "e":
            temp.append(math.e)
        else:
            temp.append(i)
    resultado=temp
    temp=[resultado[0]]
    for i in resultado[1:]:
        if type(temp[-1]) in [int,float] and type(i) in [int,float]:
            temp.append("*")
        elif type(i) == type(temp[-1]) == str:
            if temp[-1] in "-+" and i in "-+":
                temp[-1]="+" if temp[-1] == i else "-"
                continue
            else:
                raise ValueError("Erro")
        temp.append(i)


    #chama as funções para resolver seguindo a ordem de precedencia
    resultado=calcular_especial(temp,radiano)
    resultado=calcular_multiplicacao(resultado)
    if resultado == "Erro":
        return "Erro"
    resultado=calcular_soma(resultado)  
    return resultado

if __name__=="__main__":
    print(calcular(["fat",3]))
    print(calcular(["sen",3]))
    print(calcular(["cos",3]))
    print(calcular(["tan",3]))
    print(calcular([3,"!"]))
    print(calcular([3,"^",2]))
    print(calcular(["r",9]))
    print(calcular(["sen'",[1]],False))
    print(calcular(["sen'",[1]]))
    print(calcular(["fat",[6]]))
    
