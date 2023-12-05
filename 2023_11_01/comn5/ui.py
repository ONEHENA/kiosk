# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designergMIHNx.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 443)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 160, 110, 40))
        font = QFont()
        font.setFamilies([u"\ud568\ucd08\ub86c\ub3cb\uc6c0"])
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(50, 290, 256, 131))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 110, 110, 40))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(120, 210, 110, 40))
        self.pushButton_3.setFont(font)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 30, 110, 40))
        self.pushButton_4.setFont(font)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(130, 30, 110, 40))
        font1 = QFont()
        font1.setFamilies([u"\ud568\ucd08\ub86c\ub3cb\uc6c0"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.pushButton_5.setFont(font1)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(240, 30, 110, 40))
        self.pushButton_6.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uce74\ud398\ub77c\ub5bc", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uc544\uba54\ub9ac\uce74\ub178", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ubc14\ub2d0\ub77c\ub77c\ub5bc", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"HOT DRINK", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"COLD DRINK", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"BEVERAGE", None))
    # retranslateUi

