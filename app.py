from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from funcs.Funcs import calcular_delta, calcular_raizes
from funcs.Texts import*

class CalculadoraQuadratica(QMainWindow):
    def __init__(self):
        super(CalculadoraQuadratica, self).__init__()
        uic.loadUi('frames/frame.ui', self)
        
        self.results.setText(reset_info())
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpar.clicked.connect(self.limpar)
        self.actionSobre.triggered.connect(self.sobre)
        self.actionZerar_valores.triggered.connect(self.limpar)
        self.actionAjuda.triggered.connect(self.ajuda)
        self.results.setWordWrap(True)
        
        self.show()

    def calcular(self):
            a=self.valA.value()
            b=self.valB.value()
            c=self.valC.value()
            delta=calcular_delta(a,b,c)
            text=calcular_raizes(delta, a,b)
            self.results.setText(
            '''
    Valor de A: {}
    Valor de B: {}
    Valor de C: {}

    DELTA:{}

    {}'''.format(a,b,c,delta,text)
         )
    #Limpar valores do spin box
            self.resetSpinBox()

    def limpar(self):
            self.results.setText('')
            self.resetSpinBox()

    def sobre(self):   
            self.results.setText(about_info())

    def resetSpinBox (self):
        self.valA.setValue(1)
        self.valB.setValue(0)
        self.valC.setValue(0)

    def ajuda(self):
        self.results.setText(help_info())

if __name__=="__main__":
        import sys
        app = QApplication(sys.argv)
        JanelaPrincipal = CalculadoraQuadratica()
        sys.exit(app.exec_())

