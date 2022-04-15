# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainnSWfsI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 267)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ProgressBarContainer = QFrame(self.centralwidget)
        self.ProgressBarContainer.setObjectName("ProgressBarContainer")
        self.ProgressBarContainer.setFrameShape(QFrame.StyledPanel)
        self.ProgressBarContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ProgressBarContainer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ProgressBar = roundProgressBar(self.ProgressBarContainer)
        self.ProgressBar.setObjectName("ProgressBar")
        self.ProgressBar.setMinimumSize(QSize(200, 200))
        self.ProgressBar.setMaximumSize(QSize(200, 200))

        self.verticalLayout_2.addWidget(
            self.ProgressBar, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )

        self.verticalLayout.addWidget(self.ProgressBarContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )

    # retranslateUi
