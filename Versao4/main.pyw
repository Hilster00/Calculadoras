import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton


class Calculadora(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora 4")
        self.setFixedSize( 220, 270)

        #resultado
        self.__texto=""
        self.__resultado = QLineEdit(self)
        self.__resultado.setGeometry(10,10,150,40)
    
        #limpar
        self.__limpar=QPushButton(self)
        self.__limpar.setGeometry(160,10,50,40)
        self.__limpar.setText('c')
        self.__limpar.clicked.connect(self.resetar)
        
        #lista de botões
        self.__botoes=[]
        
        #Botão 0
        botao = QPushButton(self)
        botao.setGeometry(10, 210, 100, 50)
        botao.setText('0')
        self.__botoes.append(botao)

        #demias botões
        j=0
        k=0
        for i in range(1,10):
            botao = QPushButton(self)
            botao.setGeometry(10+50*j,10+50*k+50, 50, 50)
            botao.setText(f'{i}')
            self.__botoes.append(botao)
            j+=1
            if j == 3:
                j=0
                k+=1
        self.__botoes[0].clicked.connect(self.clique0)
        self.__botoes[1].clicked.connect(self.clique1)
        self.__botoes[2].clicked.connect(self.clique2)
        self.__botoes[3].clicked.connect(self.clique3)
        self.__botoes[4].clicked.connect(self.clique4)
        self.__botoes[5].clicked.connect(self.clique5)
        self.__botoes[6].clicked.connect(self.clique6)
        self.__botoes[7].clicked.connect(self.clique7)
        self.__botoes[8].clicked.connect(self.clique8)
        self.__botoes[9].clicked.connect(self.clique9)

        self.__operadores=[]
        botao = QPushButton(self)
        botao.setGeometry(110,210, 50, 50)
        botao.setText(f'=')
        self.__operadores.append(botao)
        
        for i,operador in enumerate(["-","+","*","/"]):
            botao = QPushButton(self)
            botao.setGeometry(160,60+50*i, 50, 50)
            botao.setText(f'{operador}')
            self.__operadores.append(botao)
            
        self.__operadores[0].clicked.connect(self.operador0)    
        self.__operadores[1].clicked.connect(self.operador1)
        self.__operadores[2].clicked.connect(self.operador2)
        self.__operadores[3].clicked.connect(self.operador3)
        self.__operadores[4].clicked.connect(self.operador4)
        
       
        
    def operador0(self):
        r=eval(self.__resultado.text())
        self.resetar()
        self.redefinir(f'{r}')
        
    def operador1(self):
        self.redefinir("-")
    def operador2(self):
        self.redefinir("+")
    def operador3(self):
        self.redefinir("*")
    def operador4(self):
        self.redefinir("/")

        
    def redefinir(self,novo):
        self.__texto+=novo
        self.__resultado.setText(self.__texto)
        
    def resetar(self):
        self.__texto=""
        self.__resultado.setText("")
        
    def clique0(self):
        self.redefinir("0")
        
    def clique1(self,):
        self.redefinir("1")

    def clique2(self):
        self.redefinir("2")

    def clique3(self):
        self.redefinir("3")

    def clique4(self):
        self.redefinir("4")

    def clique5(self):
       self.redefinir("5")

    def clique6(self):
       self.redefinir("6")

    def clique7(self):
       self.redefinir("7")

    def clique8(self):
        self.redefinir("8")

    def clique9(self):
        self.redefinir("9")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec_())
