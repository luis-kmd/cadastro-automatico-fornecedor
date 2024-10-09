# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(414, 451)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"\n"
"    background-color: qlineargradient(\n"
"        spread: pad, x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #8B0000, stop: 1 #B22222\n"
"    );\n"
"    color: white;\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 231, 51))
        font = QFont()
        font.setFamilies([u"Malgun Gothic"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u" background-color: transparent;\n"
"")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(20, 110, 231, 51))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u" background-color: transparent;\n"
"")
        self.Lancar = QPushButton(Dialog)
        self.Lancar.setObjectName(u"Lancar")
        self.Lancar.setGeometry(QRect(19, 400, 381, 41))
        font1 = QFont()
        font1.setFamilies([u"Malgun Gothic"])
        font1.setBold(True)
        self.Lancar.setFont(font1)
        self.Lancar.setStyleSheet(u"background-color: rgb(209, 209, 209)")
        self.Consultar = QPushButton(Dialog)
        self.Consultar.setObjectName(u"Consultar")
        self.Consultar.setGeometry(QRect(240, 80, 161, 31))
        self.Consultar.setFont(font1)
        self.Consultar.setStyleSheet(u"background-color: rgb(209, 209, 209)")
        self.Dadosreceive = QPlainTextEdit(Dialog)
        self.Dadosreceive.setObjectName(u"Dadosreceive")
        self.Dadosreceive.setGeometry(QRect(20, 160, 381, 231))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.Dadosreceive.setFont(font2)
        self.Dadosreceive.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"    color: darkred;")
        self.CNPJreceive = QLineEdit(Dialog)
        self.CNPJreceive.setObjectName(u"CNPJreceive")
        self.CNPJreceive.setGeometry(QRect(240, 40, 161, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.CNPJreceive.setFont(font3)
        self.CNPJreceive.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"    color: black;")
        QWidget.setTabOrder(self.CNPJreceive, self.Consultar)
        QWidget.setTabOrder(self.Consultar, self.Dadosreceive)
        QWidget.setTabOrder(self.Dadosreceive, self.Lancar)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"kmd", None))
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Dialog", u"CNPJ que deseja cadastrar:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Dados encontrados:", None))
        self.Lancar.setText(QCoreApplication.translate("Dialog", u"Confirmar cadastro", None))
        self.Consultar.setText(QCoreApplication.translate("Dialog", u"Consultar Dados", None))
        self.CNPJreceive.setText("")
    # retranslateUi

