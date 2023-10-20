import Bracked
import sys
import calcular_vetor
import converter_str_vetor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit

def calcular_string(string):
    if Bracked.bracked(string):
        try:
            r=string.replace("(inf)","inf")
            r=calcular_vetor.calcular(converter_str_vetor.conversor(string))
            return str(r)
        except:
            return "Erro"
    return "Erro"


class caixa_texto(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        #bloqueio de caracteres
        self.caracteres_permitidos=[str(i) for i in range(10)]
        self.caracteres_permitidos.extend(['-','+','*','/','(',')',"#","^"])

        #calcular resultado
        self.textChanged.connect(self.text_changed)
        self.__deteccao=True
        self.__limpar=False#Limpar com a próxima tecla
        self.__texto_antigo=""
        self.__operacao=""
        self.__memoria=0

        
    #detecção de teclas   
    def keyPressEvent(self, event):

        #teclas permitidas
        if event.text() in self.caracteres_permitidos:
            super().keyPressEvent(event)

        #apagar
        elif event.key() == Qt.Key_Backspace:
            self.backspace()
        elif event.key() == Qt.Key_Delete:
            posicao = self.cursorPosition()
            self.setCursorPosition(posicao + 1)
            self.backspace()

        #mover    
        elif event.key() == Qt.Key_Left:
            posicao = self.cursorPosition()
            self.setCursorPosition(posicao - 1)
        elif event.key() == Qt.Key_Right:
            posicao = self.cursorPosition()
            self.setCursorPosition(posicao + 1)
        elif event.key() == Qt.Key_Home:
            self.setCursorPosition(0)
        elif event.key() == Qt.Key_End:
            self.setCursorPosition(len(self.text()))

        #selecao
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_A:
            self.selectAll()

        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.calcular()

        #atalhos
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            #ctrl + c
            self.copy()
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_V:
            #ctrl + v
            self.paste()
            temp=""
            for i in self.text():
                if i in self.caracteres_permitidos:
                    temp+=i
            self.setText(temp)
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_X:
            #ctrl + x
            self.copy()
            self.clear()
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Z:
            #ctrl + z
            self.__deteccao=False
            self.setText(self.__texto_antigo)
            self.__deteccao=True
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_S:
            self.calcular()
            with open("resultado.txt","a") as resultado:
                if self.__operacao != "" and  self.text() != "Erro":
                    resultado.write(f'{self.__operacao} = {self.text()}\n')

        #memoria
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_M:
            self.calcular()
            if self.__memoria != "Erro":
                self.__memoria=self.text()


    def text_changed(self,text):
        #limpar texto antigo
        if self.__limpar and self.__deteccao:
            self.__deteccao=False
            temp=self.text().replace(self.__texto_antigo,"")
            self.setText(temp)
            if self.__texto_antigo == "Erro":
                self.__texto_antigo=""
            self.__limpar=False
            self.__deteccao=True
            self.setStyleSheet("color: black")

    def calcular(self):
        self.__deteccao=False
        resultado=calcular_string(self.text())
        self.__operacao=self.text()

        if resultado == "Erro":
            self.setStyleSheet("color: red")
        else:
            with open("historico.txt","a") as h:
                h.write(f'{self.__operacao} = {resultado}\n')

        self.setText(resultado)
        self.__texto_antigo=self.text()
        self.__deteccao=True
        self.__limpar=True
