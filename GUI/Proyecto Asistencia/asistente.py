# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asistente.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class asistente_ui(object):
    def setupUi(self, asistente_ui):
        if not asistente_ui.objectName():
            asistente_ui.setObjectName(u"asistente_ui")
        asistente_ui.resize(273, 242)
        self.widget = QWidget(asistente_ui)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 234, 201))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.Nombre = QLineEdit(self.widget)
        self.Nombre.setObjectName(u"Nombre")

        self.gridLayout.addWidget(self.Nombre, 0, 1, 1, 2)

        self.Correo = QLineEdit(self.widget)
        self.Correo.setObjectName(u"Correo")

        self.gridLayout.addWidget(self.Correo, 1, 1, 1, 2)

        self.Contrasena = QLineEdit(self.widget)
        self.Contrasena.setObjectName(u"Contrasena")

        self.gridLayout.addWidget(self.Contrasena, 2, 1, 1, 2)

        self.Send_code = QPushButton(self.widget)
        self.Send_code.setObjectName(u"Send_code")

        self.gridLayout.addWidget(self.Send_code, 6, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.Enviar = QPushButton(self.widget)
        self.Enviar.setObjectName(u"Enviar")

        self.gridLayout.addWidget(self.Enviar, 3, 2, 1, 1)

        self.Archivo = QLineEdit(self.widget)
        self.Archivo.setObjectName(u"Archivo")

        self.gridLayout.addWidget(self.Archivo, 5, 1, 1, 1)

        self.Buscar = QPushButton(self.widget)
        self.Buscar.setObjectName(u"Buscar")

        self.gridLayout.addWidget(self.Buscar, 5, 2, 1, 1)


        self.retranslateUi(asistente_ui)

        QMetaObject.connectSlotsByName(asistente_ui)
    # setupUi

    def retranslateUi(self, asistente_ui):
        asistente_ui.setWindowTitle(QCoreApplication.translate("asistente_ui", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("asistente_ui", u"Correo", None))
        self.label_5.setText(QCoreApplication.translate("asistente_ui", u"Buscar archivo", None))
        self.label_4.setText(QCoreApplication.translate("asistente_ui", u"Contrase\u00f1a", None))
        self.Send_code.setText(QCoreApplication.translate("asistente_ui", u"Enviar C\u00f3digo", None))
        self.label_2.setText(QCoreApplication.translate("asistente_ui", u"Nombre", None))
        self.Enviar.setText(QCoreApplication.translate("asistente_ui", u"Enviar", None))
        self.Buscar.setText(QCoreApplication.translate("asistente_ui", u"Buscar", None))
    # retranslateUi

