# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sysinfoui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(570, 198)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(552, 180))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSlider = QSlider(self.frame)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMinimumSize(QSize(25, 150))
        self.verticalSlider.setMaximumSize(QSize(150, 300))
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(60)
        self.verticalSlider.setValue(1)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.verticalSlider)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcdDelay = QLCDNumber(self.frame)
        self.lcdDelay.setObjectName(u"lcdDelay")
        self.lcdDelay.setMinimumSize(QSize(160, 75))
        self.lcdDelay.setProperty("value", 1.000000000000000)

        self.verticalLayout.addWidget(self.lcdDelay)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcdCPU = QLCDNumber(self.frame)
        self.lcdCPU.setObjectName(u"lcdCPU")
        self.lcdCPU.setMinimumSize(QSize(160, 75))

        self.verticalLayout_2.addWidget(self.lcdCPU)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lcdRAM = QLCDNumber(self.frame)
        self.lcdRAM.setObjectName(u"lcdRAM")
        self.lcdRAM.setMinimumSize(QSize(160, 75))

        self.verticalLayout_3.addWidget(self.lcdRAM)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"delay", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"CPU utilization", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"RAM used", None))
    # retranslateUi

