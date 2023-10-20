import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from functools import partial
from caixa_texto import caixa_texto

teclas=[
    "L","C","<X","π","-",
    "(","7","8","9","+",
    ")","4","5","6","*",
    "^","1","2","3","/",
    "√","0",".","=",

]

q_linhas=5
q_colunas=5
class Calculadora(QWidget):
    def __init__(self,parent=None):

        #construção da janela
        super().__init__(parent)
        self.setWindowTitle("Calculadora 6")
        self.setFixedSize(20+q_colunas*50,70+q_linhas*50)
        icon = QIcon("icone.png")
        self.setWindowIcon(icon)

        #resultado
        self.__resultado = caixa_texto(self)
        self.__resultado.setGeometry(10,10,50*q_colunas,40)
        
        #lista de botões
        self.__botoes=[QPushButton(self) for i in teclas]


        #construção de botões
        j=0
        k=0
        for i,operador in enumerate(teclas):
                self.__botoes[i].setText(f'{operador}')
                
                #definir função
                if operador == "=":
                    self.__botoes[i].clicked.connect(self.__resultado.calcular)
                    
                elif operador == "C":
                    self.__botoes[i].clicked.connect(self.resetar)
                    
                elif operador == "<X":
                    self.__botoes[i].clicked.connect(self.delet)
                    
                elif operador == "L":
                    self.__botoes[i].clicked.connect(partial(self.limpar_proximo, i))

                   
                elif operador == "...":  
                    self.__botoes[i].clicked.connect(self.uso_futuro)
                        
                else:
                    self.__botoes[i].clicked.connect(partial(self.clique, operador))
                    
                #definir dimensões
                if operador != "0":
                    self.__botoes[i].setGeometry(10+50*j,60+50*k, 50, 50)
                    j+=1#quantidade de colunas ocupadas
                else:
                    self.__botoes[i].setGeometry(10+50*j,60+50*k, 100, 50)
                    j+=2#quantidade de colunas ocupadas

                    
                if j == q_colunas:
                #vai para a linha de baixo caso tenha ocupado todas colunas
                    j=0
                    k+=1

    def limpar_proximo(self,posicao):
        self.__resultado.limpar_ativo=not self.__resultado.limpar_ativo
        cor="color: black;" if self.__resultado.limpar_ativo else "color: red;"
        self.__botoes[posicao].setStyleSheet(cor)
       
    
    def clique(self,novo):
        temp=self.__resultado.text()+f"{novo}"
        self.__resultado.setText(temp)
        
    def resetar(self):
        self.__resultado.setText("")
           
    def delet(self):
        temp=self.__resultado.text()
        self.__resultado.setText(temp[:-1])
           
    """def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Fechar',
            "Você tem certeza que deseja fechar a janela?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()"""

            
    def uso_futuro(self):
        print("Uso Futuro")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec_())
