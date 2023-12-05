# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cafe_with_viewOztFVa.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(304, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(100, 50, 90, 30))
        font = QFont()
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(100, 310, 90, 30))
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)
        self.lineEdit1 = QLineEdit(self.centralwidget)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(40, 100, 220, 180))
        self.lineEdit2 = QLineEdit(self.centralwidget)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(40, 360, 220, 180))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"view", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\ub300\uae30 \ubc88\ud638", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc \ubc88\ud638", None))
    # retranslateUi

