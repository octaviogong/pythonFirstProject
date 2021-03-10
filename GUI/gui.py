from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from ejemplo import *

# [PV] No se conecta a la BD
# [PV] La tarea se trataba de hacer GUI para la tarea 4

class Ejemplo(QMainWindow):

    def __init__(self):
        super(Ejemplo, self).__init__()
        self.ui = Ui_Ejemplo()
        self.ui.setupUi(self)

        self.ui.guardarB.clicked.connect(self.botonPresionado)
        self.ui.guardarB.setEnabled(False)
        self.ui.nombreLE.textEdited.connect(self.textoEditado)
        self.ui.correoLE.textEdited.connect(self.textoEditado)
        self.ui.contraLE.textEdited.connect(self.textoEditado)

#Slots
    def botonPresionado(self):
        print("Se ha presionado boton guardar")
        pass

    def textoEditado(self):
        if self.ui.nombreLE.text() and self.ui.correoLE.text() and self.ui.contraLE.text():
            self.ui.guardarB.setEnabled(True)
        else:
            self.ui.guardarB.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Ejemplo()

    window.show()

    sys.exit(app.exec_())
