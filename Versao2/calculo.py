operadores=["^","*","/","-","+"]
def calcular(operacao,operador):
    if operador in ["**","^"]:
        retorno=calculo(operacao[0])
        for i in operacao[1:]:
            retorno**=calculo(i)
        if type(retorno)==complex:
            retorno=-1*calculo(operacao[0])
            for i in operacao[1:]:
                retorno**=calculo(i)
            retorno=complex(f"{retorno}j")
        return retorno
        
    if operador == "*":
        retorno=1
        for i in operacao:
            retorno*=calculo(i)
        return retorno
        
    if operador == "/":
        
        retorno=calculo(operacao[0])
        for i in operacao[1:]:
            retorno/=calculo(i)
        return retorno
        
    if operador in ["+","-"]:
        retorno=0
        for i in operacao:
            retorno+=calculo(i)
        return retorno
  
def calculo(operacao):
    t=0
    r=1
    for operador in operadores:
        if operador in operacao:
            operacao=operacao.split(operador)
            while "" in operacao:
                operacao.remove("")
            t=1
            r=calcular(operacao,operador)
    
    if t==0:
        operacao=operacao.replace("@","-")
        if "!" in operacao:
            operacao=operacao.replace("!","")
            operacao=int(operacao)
            resultado=1
            for i in range(2,operacao+1):
                resultado*=i
            return resultado
        return float(operacao)
    return r
