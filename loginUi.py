# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(685, 535)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 165, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.registerButton = QPushButton(Form)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout.addWidget(self.registerButton)

        self.loginButton = QPushButton(Form)
        self.loginButton.setObjectName(u"loginButton")

        self.horizontalLayout.addWidget(self.loginButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.registerButton.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
    # retranslateUi

