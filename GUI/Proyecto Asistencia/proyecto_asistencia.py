import sys
from PySide2.QtWidgets import *

import socket
import pickle

from estudiante import Estudiante
from asistente import asistente_ui


class Asistencia_Gui(QMainWindow):
    def __init__(self):
        super(Asistencia_Gui, self).__init__()
        self.ui = asistente_ui()
        self.ui.setupUi(self)

        self.ui.Buscar.clicked.connect(self.buscar)
        self.ui.Enviar.clicked.connect(self.enviar)
        self.ui.Send_code.clicked.connect(self.send_code)

        self.s = socket.socket()
        self.host = '3.16.226.150'
        self.port = 9997

    def buscar(self):
        filename, _ = QFileDialog.getOpenFileName(filter='*zip')
        self.ui.Archivo.setText(filename)

    def enviar(self):
        self.s.connect((self.host, self.port))

        estudiante = Estudiante(f'{self.ui.Nombre.text()}', f'{self.ui.Correo.text()}', f'{self.ui.Contrasena.text()}')

        estudiante_serializado = pickle.dumps(estudiante)

        self.s.send(estudiante_serializado)

        ans = self.s.recv(1024)
        print(f'Respuesta: \t{ans.decode()}')

    def send_code(self):
        filename = self.ui.Archivo.text()
        file = open(filename, 'rb')
        seguir = True
        inicio = 0
        file_serializado = pickle.dumps(file.read())

        self.s.send(b'INI')
        ans = self.s.recv(1024)
        print(f'Respuesta: \t{ans.decode()}')

        while seguir:

            chunks = file_serializado[inicio:inicio + 1024]

            if not chunks:
                seguir = False
                continue

            self.s.send(chunks)
            ans = self.s.recv(1024)
            print(f'Respuesta: \t{ans.decode()}')
            inicio += 1024

        self.s.send(b'FIN')
        ans = self.s.recv(1024)
        print(f'Respuesta: \t{ans.decode()}')

        input('Oprime ENTER para cerrar conexion')
        self.s.close()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Asistencia_Gui()
    window.show()
    sys.exit(App.exec_())
