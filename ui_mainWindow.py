# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(638, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 120, 47, 13))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 150, 47, 13))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 190, 47, 13))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 230, 31, 16))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 260, 41, 20))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 290, 31, 16))
        self.destX_spinBox = QSpinBox(self.groupBox)
        self.destX_spinBox.setObjectName(u"destX_spinBox")
        self.destX_spinBox.setGeometry(QRect(100, 120, 81, 22))
        self.destX_spinBox.setMaximum(500)
        self.destY_spinBox = QSpinBox(self.groupBox)
        self.destY_spinBox.setObjectName(u"destY_spinBox")
        self.destY_spinBox.setGeometry(QRect(100, 150, 81, 22))
        self.destY_spinBox.setMaximum(500)
        self.speed_spinBox = QSpinBox(self.groupBox)
        self.speed_spinBox.setObjectName(u"speed_spinBox")
        self.speed_spinBox.setGeometry(QRect(100, 190, 81, 22))
        self.speed_spinBox.setMaximum(99999)
        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setGeometry(QRect(100, 230, 81, 22))
        self.red_spinBox.setMaximum(255)
        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setGeometry(QRect(100, 260, 81, 22))
        self.green_spinBox.setMaximum(255)
        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setGeometry(QRect(100, 290, 81, 22))
        self.blue_spinBox.setMaximum(255)
        self.particle_PlainText = QPlainTextEdit(self.groupBox)
        self.particle_PlainText.setObjectName(u"particle_PlainText")
        self.particle_PlainText.setGeometry(QRect(260, 0, 321, 531))
        self.addToStart_pushButton = QPushButton(self.groupBox)
        self.addToStart_pushButton.setObjectName(u"addToStart_pushButton")
        self.addToStart_pushButton.setGeometry(QRect(20, 340, 91, 31))
        self.addEnd_pushButton = QPushButton(self.groupBox)
        self.addEnd_pushButton.setObjectName(u"addEnd_pushButton")
        self.addEnd_pushButton.setGeometry(QRect(120, 340, 91, 31))
        self.showListParticle_pushButton = QPushButton(self.groupBox)
        self.showListParticle_pushButton.setObjectName(u"showListParticle_pushButton")
        self.showListParticle_pushButton.setGeometry(QRect(50, 380, 131, 31))
        self.originX_label = QLabel(self.groupBox)
        self.originX_label.setObjectName(u"originX_label")
        self.originX_label.setGeometry(QRect(40, 60, 47, 13))
        self.originY_label = QLabel(self.groupBox)
        self.originY_label.setObjectName(u"originY_label")
        self.originY_label.setGeometry(QRect(40, 90, 47, 13))
        self.originY_spinBox = QSpinBox(self.groupBox)
        self.originY_spinBox.setObjectName(u"originY_spinBox")
        self.originY_spinBox.setGeometry(QRect(100, 90, 81, 22))
        self.originY_spinBox.setMaximum(500)
        self.originX_spinBox = QSpinBox(self.groupBox)
        self.originX_spinBox.setObjectName(u"originX_spinBox")
        self.originX_spinBox.setGeometry(QRect(100, 60, 81, 22))
        self.originX_spinBox.setMaximum(500)
        self.originX_label_2 = QLabel(self.groupBox)
        self.originX_label_2.setObjectName(u"originX_label_2")
        self.originX_label_2.setGeometry(QRect(70, 20, 21, 16))
        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setGeometry(QRect(100, 20, 81, 22))
        self.id_spinBox.setMaximum(500)

        self.horizontalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 638, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rojo:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Verde:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Azul:", None))
        self.addToStart_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.addEnd_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.showListParticle_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.originX_label.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.originY_label.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.originX_label_2.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
    # retranslateUi

