#1+1(1+2)
def limpagem(lista):
    r=[]
    for i in lista:
        if type(i) != str:
            r.append(limpagem(i))
        elif i in "+/*-^":
            r.append(i)
        elif ("." in i) or (i in "#"):
            if i in "#":
                i = "inf"
            r.append(float(i))
        else:
            r.append(int(i))
            
    if r[0] == "-" or r[0] == "+":
        r.insert(0,0)
        
    return r
    
def conversor(string):
    
    #conversão de caracteres para o padrão do programa
    antigo=[",","**","infinity","inf","[","]","{","}"]
    novo=[".","^","inf","#","(",")","(",")"]
    for i in zip(antigo,novo):
        string=string.replace(i[0],i[1])
    
    #retorno será uma lista com os valores e os operadores
    retorno=[]
    cadeia=""
    
    #laço para iterar sobre os caracteres da string
    i=0
    while i < len(string):
        if string[i] in "+-*/^()#" :
            
            #nao adiciona caracteres vazios
            if cadeia != "":
                retorno.append(cadeia)
                cadeia=""
                
            #cria uma sub-lista para parenteses internos
            if string[i] == "(":
                temp=conversor(string[i+1:])
                i+=temp[1]+1
                #quantidade de caracteres percorridos 
                retorno.append(temp[0])
                
            #retorna a sub-lista interior    
            elif string[i] == ")":
            #sub-lista e indices percorridos
                return retorno,i
            else:
                retorno.append(string[i])
        else:
            cadeia+=string[i]
        i+=1
            
    if cadeia != "":
        retorno.append(cadeia)
    return limpagem(retorno)
    
    
if __name__=="__main__":
    print(conversor("1+2.5+(1+(12*3)+2)+2+inf"))
