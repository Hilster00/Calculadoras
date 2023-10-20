import Bracked
import converter_string
import converter_str_vetor
import limpar_vetor
import calcular_vetor

def calcular_string(string,radianos):
    if Bracked.bracked(string) == False:
        teste_bracked=Bracked.bracked(string,True)
        if teste_bracked[1][:3] == "P(A":
            quantidade=""
            for i in teste_bracked[1]:
                if i == ",":
                    break
                quantidade+=i
            quantidade=quantidade[3:]
            quantidade=int(quantidade[:-1])
            string=string+")"*quantidade
        else:
            return "Erro"

    
    try:
        
        r=converter_string.converter_string(string)
        r=r.replace("(inf)","inf")
        r=converter_str_vetor.conversor(r)
        r=limpar_vetor.limpagem(r)
       
        r=calcular_vetor.calcular(r,radianos)
        return str(r)
    except:
        return "Erro"
   
