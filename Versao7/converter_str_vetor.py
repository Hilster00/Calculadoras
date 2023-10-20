
#1+1(1+2)
operacoes=["sen","cos","tan","sen'","cos'","tan'","som","fat","log","ln",'lg',"e","π"]
valor_proprio=["e","π"]
caracteres="sencotamflgπ"

#faz o tratamento adequado dos caracteres para o padrão que será
#interpretado
def conversor(string):
    #conversão de caracteres para o padrão do programa
    antigo=[".",",","**","infinity","inf","[","]","{","}","√"]
    novo=["_",".","^","inf","#","(",")","(",")","r"]
    for i in zip(antigo,novo):
        string=string.replace(i[0],i[1])
    return criar_lista(string)

def  criar_lista(string):

    #retorno será uma lista com os valores e os operadores
    retorno=[]
    operacao=""
    cadeia=""
    
    #laço para iterar sobre os caracteres da string
    i=0
    while i < len(string):
        
        #linsta interna
        if string[i] in "()":
            #cria uma sub-lista para parenteses internos
            if string[i] == "(":
                temp=criar_lista(string[i+1:])
                #quantidade de caracteres percorridos 
                i+=temp[1]
                retorno.append(temp[0])
                
            #retorna a sub-lista interior    
            elif string[i] == ")":
                if cadeia != "":
                    retorno.append(cadeia)
                #sub-lista e indices percorridos    
                return retorno,i+1
            
        elif string[i] in "+-*/^!#r%sencomfatlgπ'" :

            
            #nao adiciona caracteres vazios
            if cadeia != "":
                retorno.append(cadeia)
                cadeia=""
                    
            
            if string[i] in caracteres:
                operacao+=string[i]
                if operacao in operacoes:
                    if operacao in ["sen","cos","tan"]:
                        if string[i+1] == "'":
                            i+=1
                            operacao+=string[i]
                            print(operacao)
                    retorno.append(operacao)
                    operacao=""
            else:
                retorno.append(string[i])
        else:
            cadeia+=string[i]
   
        i+=1

        
    if cadeia != "":
        retorno.append(cadeia)
        
    return retorno
    
    
if __name__=="__main__":
    print(conversor("1+2.5+(1+(12*3)+2)+2+inf"))
    print(conversor("sen'90"))
    print(conversor("fat6"))
