# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ejemplo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Ejemplo(object):
    def setupUi(self, Ejemplo):
        if not Ejemplo.objectName():
            Ejemplo.setObjectName(u"Ejemplo")
        Ejemplo.resize(238, 131)
        self.formLayoutWidget = QWidget(Ejemplo)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(9, 9, 211, 74))
        self.gridLayout_2 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nombreL = QLabel(self.formLayoutWidget)
        self.nombreL.setObjectName(u"nombreL")

        self.gridLayout_2.addWidget(self.nombreL, 0, 0, 1, 1)

        self.nombreLE = QLineEdit(self.formLayoutWidget)
        self.nombreLE.setObjectName(u"nombreLE")

        self.gridLayout_2.addWidget(self.nombreLE, 0, 1, 1, 1)

        self.correoL = QLabel(self.formLayoutWidget)
        self.correoL.setObjectName(u"correoL")

        self.gridLayout_2.addWidget(self.correoL, 1, 0, 1, 1)

        self.correoLE = QLineEdit(self.formLayoutWidget)
        self.correoLE.setObjectName(u"correoLE")

        self.gridLayout_2.addWidget(self.correoLE, 1, 1, 1, 1)

        self.contraL = QLabel(self.formLayoutWidget)
        self.contraL.setObjectName(u"contraL")

        self.gridLayout_2.addWidget(self.contraL, 2, 0, 1, 1)

        self.contraLE = QLineEdit(self.formLayoutWidget)
        self.contraLE.setObjectName(u"contraLE")

        self.gridLayout_2.addWidget(self.contraLE, 2, 1, 1, 1)

        self.guardarB = QPushButton(Ejemplo)
        self.guardarB.setObjectName(u"guardarB")
        self.guardarB.setGeometry(QRect(0, 100, 75, 23))

        self.retranslateUi(Ejemplo)

        QMetaObject.connectSlotsByName(Ejemplo)
    # setupUi

    def retranslateUi(self, Ejemplo):
        Ejemplo.setWindowTitle(QCoreApplication.translate("Ejemplo", u"Ejemplo", None))
        self.nombreL.setText(QCoreApplication.translate("Ejemplo", u"Nombre:", None))
        self.correoL.setText(QCoreApplication.translate("Ejemplo", u"Correo:", None))
        self.contraL.setText(QCoreApplication.translate("Ejemplo", u"Contase\u00f1a:", None))
        self.guardarB.setText(QCoreApplication.translate("Ejemplo", u"Guardar", None))
    # retranslateUi

