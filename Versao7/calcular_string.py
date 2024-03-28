import Bracked
import concertar_string
import converter_str_vetor
import limpar_vetor
import calcular_vetor

def calcular_string(string,radianos):
    
    if Bracked.bracked(string) == False:
        teste_bracked=Bracked.bracked(string,True)[1]
        quantidade=teste_bracked.get("P",0)
        if quantidade > 0:
            string=string+")"*quantidade
            if Bracked.bracked(string) == False:
                return "Erro"
        else:
            return "Erro"

    
    try:
        
        r=concertar_string.converter_string(string)
        r=r.replace("(inf)","inf")
        r=converter_str_vetor.conversor(r)
        r=limpar_vetor.limpagem(r)
       
        r=calcular_vetor.calcular(r,radianos)
        return str(r)
    except:
        return "Erro"
   
