# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 360)
        Form.setMinimumSize(QSize(400, 290))
        Form.setMaximumSize(QSize(500, 360))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEditInfo = QPlainTextEdit(Form)
        self.plainTextEditInfo.setObjectName(u"plainTextEditInfo")
        self.plainTextEditInfo.setMaximumSize(QSize(500, 350))
        font = QFont()
        font.setPointSize(20)
        self.plainTextEditInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.plainTextEditInfo)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.getWeatherBTN = QPushButton(self.widget)
        self.getWeatherBTN.setObjectName(u"getWeatherBTN")
        self.getWeatherBTN.setMaximumSize(QSize(140, 25))
        self.getWeatherBTN.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.getWeatherBTN)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.latitude = QLineEdit(self.widget)
        self.latitude.setObjectName(u"latitude")

        self.horizontalLayout.addWidget(self.latitude)

        self.longitude = QLineEdit(self.widget)
        self.longitude.setObjectName(u"longitude")

        self.horizontalLayout.addWidget(self.longitude)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.spinBoxDelay = QSpinBox(Form)
        self.spinBoxDelay.setObjectName(u"spinBoxDelay")
        self.spinBoxDelay.setMinimum(2)
        self.spinBoxDelay.setMaximum(25)
        self.spinBoxDelay.setValue(10)

        self.verticalLayout.addWidget(self.spinBoxDelay)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.getWeatherBTN.setText(QCoreApplication.translate("Form", u"Get Weather Info ", None))
        self.latitude.setPlaceholderText(QCoreApplication.translate("Form", u"latitude", None))
        self.longitude.setPlaceholderText(QCoreApplication.translate("Form", u"longitude", None))
        self.label.setText(QCoreApplication.translate("Form", u"Delay", None))
    # retranslateUi

