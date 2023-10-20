operacoes_tam4 = ["sen'", "cos'", "tan'"]
operacoes_tam3 = ["sen", "cos", "tan", "som", "fat", "log"]
operacoes_tam2 = ["ln", "lg"]
operacoes_tam1 = ['r',"√"]
num = [str(i) for i in range(10)]
num.extend(["e","π",".",",","_"])

def converter_string(string,recursao=False):
    if not string:
        if recursao:
            return "",0
        return ""
    tam=len(string)
    retorno=""
    i=0
    parenteses=0
    while i < tam:
        if tam-i > 4:
            if string[i:4+i] in operacoes_tam4:
                retorno+=f"({string[i:4+i]}("
                temp=converter_string(string[4+i:],True)
                retorno+=temp[0]
                retorno+="))"
                i+=temp[1]+4
                continue
        if tam-i > 3:
            if string[i:3+i] in operacoes_tam3:
                retorno+=f"({string[i:3+i]}("
                temp=converter_string(string[3+i:],True)
                retorno+=temp[0]
                retorno+="))"
                i+=temp[1]+3
                continue
        if tam-i > 2:
            if string[i:2+i] in operacoes_tam2:
               retorno+=f"({string[i:2+i]}("
               temp=converter_string(string[2+i:],True)
               retorno+=temp[0]
               retorno+="))"
               i+=temp[1]+2
               continue
        if tam-i > 1:
            if string[i:1+i] in operacoes_tam1:
                retorno+=f"({string[i:1+i]}("
                temp=converter_string(string[1+i:],True)
                retorno+=temp[0]
                retorno+="))"
                i+=temp[1]+1
                continue

                

                        

        if (recursao) and (string[i] not in num):
            #valida entradas no padrao sen-180,cos+90,tan-45
            if i == 0 and string[i] in "-+":
                retorno+=string[i]
                i+=1
                continue
            #valida entradas no padrao sen(90),cos((90)),tan(90-(90/2))
            if string[i] in "()":
                parenteses+=1 if string[i] == "(" else -1
                if parenteses == 0:
                    return retorno,i
                retorno+=string[i]
                i+=1
                continue
            return [retorno,i]
        retorno+=string[i]
    
        
        i+=1
    if recursao:
        return [retorno,i]
    return retorno

if __name__ == "__main__":
    print(converter_string("3*x+cos3*sensen3+r3+rr3"))
    print(converter_string("sencossencos90"))
    print(converter_string("sen90-sen90"))
    print(converter_string("sen90+sen-90"))
    print(converter_string("cos90/cos90"))
    print(converter_string("cos(90)/cos(90)"))
    print(converter_string("sen((90))"))
    print(converter_string("sen'9"))
    print(converter_string("fat9"))




    
