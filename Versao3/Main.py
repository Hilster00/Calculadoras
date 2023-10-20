import os
import platform
from calcular_vetor import calcular
from converter_str_vetor import conversor
limpar="cls" if platform.system() == "Windows" else "clear"
os.system("title Calculadora 3")
while True:
    entrada=input("Digite a operação:")
    if entrada == "sair":
        break
    os.system(limpar)
    lista=conversor(entrada)
    print(f"Lista gerada pela função conversor:{lista}\n")
    print(f"Resultado obtido pela função calcular:{calcular(lista)}\n")
