# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LectionRepeatForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(486, 91)
        Form.setMinimumSize(QSize(486, 91))
        Form.setMaximumSize(QSize(486, 91))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditSource = QLineEdit(Form)
        self.lineEditSource.setObjectName(u"lineEditSource")

        self.horizontalLayout.addWidget(self.lineEditSource)

        self.lineEditResult = QLineEdit(Form)
        self.lineEditResult.setObjectName(u"lineEditResult")

        self.horizontalLayout.addWidget(self.lineEditResult)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEditSource.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442", None))
        self.lineEditResult.setPlaceholderText(QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

