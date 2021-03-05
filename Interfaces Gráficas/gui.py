from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()

window.show()

sys.exit(app.exec_())
