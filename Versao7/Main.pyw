import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMainWindow, QAction, QPlainTextEdit
from functools import partial
from caixa_texto import caixa_texto

teclas = [
    "L",    "C",    "<X",   "-",    "INV",  "RAD",  "%",
    "7",    "8",    "9",    "+",    "sen",  "cos",  "tan",
    "4",    "5",    "6",    "*",    "ln",   "log",  "!",
    "1",    "2",    "3",    "/",    "π",    "e",    "^",  
    ",",    "0",    "=",   "(",  ")",    "√"
]
teclas_especiais = [
    "INV",  "RAD",  "%",
    "sen",  "cos",  "tan",
    "ln",   "log",  "!",
    "π",    "e",    "^",
    "(",    ")",    "√"
]
teclas_invertidas = {
    "sen": "sen'",
    "cos": "cos'",
    "tan": "tan'",
    "log": "10^",
    "ln": "e^",
    "√": "^2",
}
posicao_telcas_invertidas = []
nao_implementado = []
q_linhas = 5
q_colunas = 7

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora 7")
        self.setFixedSize(20 + q_colunas * 50, 90 + q_linhas * 50)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)
        icone_path = os.path.join(base_path, 'assets', 'icone.ico')
        icon = QIcon(icone_path)
        self.setWindowIcon(icon)

        #resultado
        self.__resultado = caixa_texto(self)
        self.__resultado.setGeometry(10, 30, 50 * q_colunas, 40)

        #historico
        self.__historico = QPlainTextEdit(self)
        self.__historico.setGeometry(10, 30, 50 * q_colunas, (q_linhas+1) * 50)
        self.__historico.setVisible(False)
        self.__historico.setReadOnly(True)

        
        #barra de menu
        main_menu = QMainWindow.menuBar(self)
        conf = main_menu.addMenu("Conf")
        historico = main_menu.addMenu("Hist")

        #alternar entre os modos da calculadora
        calculadora_especial1 = QAction('Calculadora Especial', self)
        calculadora_especial2 = QAction('Calculadora Especial', self)
        calculadora_especial1.setShortcut('Ctrl+E')
        calculadora_especial2.setShortcut('F5')
        calculadora_especial1.triggered.connect(lambda : self.calculadora_especial())
        calculadora_especial2.triggered.connect(lambda : self.calculadora_especial())
        conf.addAction(calculadora_especial1)        
        self.addAction(calculadora_especial2)

        #ver historico
        ver_historico1= QAction("Historico", self)
        ver_historico2= QAction("Historico", self)
        ver_historico1.setShortcut('Ctrl+H')
        ver_historico2.setShortcut('F11')
        ver_historico1.triggered.connect(lambda: self.historico())
        historico.addAction(ver_historico1)
        ver_historico2.triggered.connect(lambda: self.historico())
        self.addAction(ver_historico2)
        
        #limpar historico
        limpar_historico1 = QAction("Limpar Historico", self)
        limpar_historico2 = QAction("Limpar Historico", self)
        limpar_historico1.setShortcut("Ctrl+Shift+L")
        limpar_historico2.setShortcut("F12")
        limpar_historico1.triggered.connect(lambda: self.limpar_historico())
        limpar_historico2.triggered.connect(lambda: self.limpar_historico())
        historico.addAction(limpar_historico1)
        self.addAction(limpar_historico2)
        
        #atalho de fechar janela
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        self.addAction(exit_action)
        
        
        #teste= QAction("Print", self)
        #teste.setShortcut('Ctrl+M')
        #teste.triggered.connect(lambda: self.__resultado.setText("Hilster"))
        
        
        #variaveis de configuracoes
        self.__radiano = True #modo radiano ativo
        self.__historico_v=False #historico visivel
        self.__inv = False #inversao de funcoes
        self.__calculadora_completa = True #calculadora com todos botoes


        self.__botoes = [QPushButton(self) for i in teclas]
        j = 0
        k = 0
        self.__lista_botoes = {}
        for i, operador in enumerate(teclas):
            self.__botoes[i].setText(f'{operador}')
            self.__lista_botoes[operador] = (self.__botoes[i], i)

            if operador == "=":
                self.__botoes[i].clicked.connect(self.calcular)
                tecla_resultado = i
            elif operador == "C":
                self.__botoes[i].clicked.connect(self.resetar)
            elif operador == "<X":
                self.__botoes[i].clicked.connect(self.delet)
            elif operador == "L":
                self.__botoes[i].clicked.connect(partial(self.limpar_proximo, i))
            elif operador == "RAD":
                self.__botoes[i].clicked.connect(partial(self.alternar_rad, i))
            elif operador == "INV":
                self.__botoes[i].clicked.connect(partial(self.inv, i))
            elif (operador == "..." or "") or operador in nao_implementado:
                self.__botoes[i].clicked.connect(self.uso_futuro)
            elif teclas_invertidas.get(operador) is not None:
                self.__botoes[i].clicked.connect(partial(self.invertida, operador))
                posicao_telcas_invertidas.append([i, operador])
            else:
                self.__botoes[i].clicked.connect(partial(self.clique, operador))

            if operador != "0":
                self.__botoes[i].setGeometry(10 + 50 * j, 80 + 50 * k, 50, 50)
                j += 1
            else:
                self.__botoes[i].setGeometry(10 + 50 * j, 80 + 50 * k, 100, 50)
                j += 2

            if j == q_colunas:
                j = 0
                k += 1

        self.calculadora_especial()
        self.__historico.raise_()
        

    #funcoes simples
    def resetar(self):
        self.__resultado.setText("")

    def delet(self):
        temp = self.__resultado.text()
        self.__resultado.setText(temp[:-1])
        
    def calcular(self):
        self.__resultado.calcular(self.__radiano)

    #funcao temporaria,
    def uso_futuro(self):
        print("Uso Futuro")

    #clique de qualquer botão sem comum(0-9 e outras funcoes matematicas)
    def clique(self, novo):
        temp = self.__resultado.text() + f"{novo}"
        self.__resultado.setText(temp)

    #alterna entre radianos e graus
    def alternar_rad(self, posicao):
        self.__radiano = not (self.__radiano)
        texto = "RAD" if self.__radiano else "GRAUS"
        self.__botoes[posicao].setText(texto)
        self.__resultado.radiano = self.__radiano

    #inverte as funcoes matematicas    
    def invertida(self, operador):
        if self.__inv:
            self.clique(teclas_invertidas[operador])
        else:
            self.clique(operador)

    def inv(self, posicao):
        self.__inv = not (self.__inv)
        cor = "color: red;" if self.__inv else "color: black;"
        self.__botoes[posicao].setStyleSheet(cor)
        for i, operador in posicao_telcas_invertidas:
            texto = teclas_invertidas[operador] if self.__inv else operador
            self.__botoes[i].setText(texto)

            

    #limpar o resultado, ou manter para proximos calculos
    def limpar_proximo(self,posicao):
        self.__resultado.limpar_ativo=not self.__resultado.limpar_ativo
        cor="color: black;" if self.__resultado.limpar_ativo else "color: red;"
        self.__botoes[posicao].setStyleSheet(cor)


    #alternar entre calculadora completa ou simples
    def calculadora_especial(self):
        self.__calculadora_completa = not self.__calculadora_completa
        for tecla in teclas_especiais:
            self.__lista_botoes[tecla][0].setVisible(self.__calculadora_completa)
        temp = 7 if self.__calculadora_completa else 4
        self.setFixedSize(20 + temp * 50, 90 + q_linhas * 50)
        self.__resultado.setGeometry(10, 30, 50 * temp, 40)
        self.__historico.setGeometry(10, 30, 50 * temp, (q_linhas+1) * 50)

    

    def historico(self):
        try:
            with open("historico.his", "r") as historico:
                texto = historico.read()
        except FileNotFoundError:
            texto = ""

        self.__historico_v=not(self.__historico_v)
        self.__historico.setVisible(self.__historico_v)
        self.__historico.setPlainText(texto)
        temp = 7 if self.__calculadora_completa else 4
        self.__historico.setGeometry(10, 30, 50 * temp, (q_linhas+1) * 50)

    def limpar_historico(self):
        try:
            with open("historico.his", "w") as historico:
                historico.write("")
        except FileNotFoundError:
            ...
        self.__historico.setPlainText("")


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec_())
