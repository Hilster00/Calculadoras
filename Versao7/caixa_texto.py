import sys
import separador
import calcular_string
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QColor

tabela_troca={
    "^":["**","pow","potencia"],
    "-":["-+","+-"],
    "+":["++","--"],
    "√":["//","raiz"],
    "π":["pi"],
    "cos(":["cosseno"],
    "sen(":["sin","seno"],
    "tan(":["tangente"],
}

class caixa_texto(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #cor
        self.__cor = QColor()
        self.__cor.setRgb(0, 0, 0)

        #bloqueio de caracteres
        self.caracteres_permitidos=[str(i) for i in range(10)]
        self.caracteres_permitidos.extend(['-',
        '+','*','/','(',')',"#","^","{","}","[",
        "]",",",".",'√',"%","s","e","n","c","o",
        "t","a","m","f","l","g","p","i","r","z","w","'"])

        #calcular resultado
        self.textChanged.connect(self.text_changed)
        
        #detecção decção de mudanças de texto internas e externas
        self.__deteccao=True

        #apaga texto na próxima tecla
        self.__limpar=False
        
        #apagar texto na próxima tecla ativa
        self.__limpar_ativo=True
        
        self.__texto_antigo=""

        #Uso futuro
        #self.__memoria=0
        self.radiano=True

    @property
    def limpar_ativo(self):
        return self.__limpar_ativo
    
    @limpar_ativo.setter
    def limpar_ativo(self,valor):
        self.__limpar_ativo=valor

    
    def cor(self,c=[0,0,0]):
        self.__cor.setRgb(c[0],c[1],c[2])
        self.setStyleSheet(f"color: {self.__cor.name()}")

    def setText(self,texto,cor=None):
        QLineEdit.setText(self,texto)
        if cor != None:
            self.cor(cor)

     
    #detecção de teclas   
    def keyPressEvent(self, event):

        #teclas permitidas
        if event.text() in self.caracteres_permitidos:
            super().keyPressEvent(event)

        #APAGAR
        elif event.key() == Qt.Key_Backspace:
            self.backspace()
        elif event.key() == Qt.Key_Delete:
            posicao = self.cursorPosition()
            self.setCursorPosition(posicao + 1)
            self.backspace()
            
        #MOVER   
        #<-
        elif event.key() == Qt.Key_Left:
            posicao = self.cursorPosition()
            self.setCursorPosition(posicao - 1)
        #->
        elif event.key() == Qt.Key_Right:
            posicao = self.cursorPosition()
            self.setCursorPosition(posicao + 1)
        #HOME
        elif event.key() == Qt.Key_Home:
            self.setCursorPosition(0)
        #END
        elif event.key() == Qt.Key_End:
            self.setCursorPosition(len(self.text()))
            

        #Atalhos
        #Enter(ambos teclados)    
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.calcular(self.radiano)
            
        #ctrl
        elif event.modifiers() == Qt.ControlModifier:

            #ctrl + a
            if event.key() == Qt.Key_A:
                self.selectAll()
                
            #ctrl + c
            elif event.key() == Qt.Key_C:
                self.copy()

            #ctrl + x        
            elif event.key() == Qt.Key_X:
                self.copy()
                self.clear()
                
            #ctrl + z
            elif event.key() == Qt.Key_Z:
                self.__deteccao=False
                self.setText(self.__texto_antigo)
                self.__deteccao=True

            #ctrl + s
            elif event.key() == Qt.Key_S:
                self.calcular()
                with open('historico.txt', 'r',encoding="utf-8") as historico:
                    linhas = historico.readlines()
                    ultima_linha = linhas[-1]
                    with open("resultado.txt","a",encoding="utf-8") as resultado:
                        resultado.write(ultima_linha)
                    
            #ctrl + v    
            elif event.key() == Qt.Key_V:
                self.paste()
                #texto final
                temp=""
                for i in self.text():
                    if i in self.caracteres_permitidos:
                        #só adiciona os caracteres permitidos
                        temp+=i
                #seta texto limpo
                self.setText(temp)
                
            """
            uso futuro
            #ctrl + m
            elif event.key() == Qt.Key_M:
                #memoria
                self.calcular()
                if self.__memoria != "Erro":
                    self.__memoria=self.text()"""

            
    def text_changed(self,text):
        #limpar texto antigo
        if self.__deteccao:
            self.__deteccao=False
            if self.__limpar:
                #se tiver selecionado opcao de limpar texto ou texto for Erro
                if self.limpar_ativo or self.__texto_antigo == "Erro":
                    temp=text.replace(self.__texto_antigo,"")
                    self.setText(temp)
                    self.__texto_antigo=""
                    self.__limpar=False
                    self.cor()
            else:
                texto=self.text()
                for novo,antigos in tabela_troca.items():
                    for antigo in antigos:
                        texto=texto.replace(antigo,novo) 
                self.setText(texto)
            self.__deteccao=True

                
    def calcular(self,radianos=True):
        self.__deteccao=False
        #texto vazio
        if self.text() == "":
            #cor vermelha e resultado 0
            resultado="0"
            self.cor([255,0,0])
            
        #texto não vazio    
        else:
            #calcula o resultado
            resultado=calcular_string.calcular_string(self.text(),radianos)
            #resultado invalido
            if resultado == "Erro" or resultado == "nan":
                self.cor([255,0,0])
                
            #resultado valido
            else:
                #arredondamento para 3 casas
                resultado=f"{float(resultado):.3f}"

                #limpa a parte flutuante
                resultado=float(resultado)
                temp_int=int(resultado)
                if resultado == temp_int:
                    resultado=temp_int

                #tira o sinal antes da formatação
                sinal=""
                if resultado<0:
                    resultado*=-1
                    sinal+="-"

                #formata texto para padrão brasileiro
                resultado=f"{sinal}{separador.formatar_leitura(str(resultado))}"

                #salva no historico
                with open("historico.txt","a",encoding="utf-8") as h:
                    h.write(f'{self.text()} = {resultado}\n')
        
        self.__limpar=True#proxima tecla precionada limpa o texto
        self.setText(resultado)#mostra o resultado
        self.__texto_antigo=self.text()
        self.__deteccao=True#reativa deteccao
        
