import platform
import os

def limpar():
    #comando para limpar a tela
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")
