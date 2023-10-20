def ajustar(operacao):
    operacao=operacao.replace("-","-@")#correcao para permitir subtracao
    operacao=operacao.replace(",",".")#correcao de , para . para os reais
    operacao=operacao.replace("**","^")#subtracao de ** para ^ para potencias
    operacao=operacao.replace("infinito","infinity")#tradduz infinito para inf
    
    return operacao
