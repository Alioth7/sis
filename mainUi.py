# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(834, 673)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.student_id = QLineEdit(self.centralwidget)
        self.student_id.setObjectName(u"student_id")

        self.gridLayout.addWidget(self.student_id, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.className = QComboBox(self.centralwidget)
        self.className.addItem("")
        self.className.addItem("")
        self.className.addItem("")
        self.className.addItem("")
        self.className.addItem("")
        self.className.addItem("")
        self.className.setObjectName(u"className")
        self.className.setMouseTracking(False)

        self.gridLayout.addWidget(self.className, 2, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(608, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.input_choice = QComboBox(self.centralwidget)
        self.input_choice.addItem("")
        self.input_choice.addItem("")
        self.input_choice.addItem("")
        self.input_choice.addItem("")
        self.input_choice.addItem("")
        self.input_choice.addItem("")
        self.input_choice.setObjectName(u"input_choice")

        self.horizontalLayout_2.addWidget(self.input_choice)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.score = QLineEdit(self.centralwidget)
        self.score.setObjectName(u"score")

        self.horizontalLayout_2.addWidget(self.score)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(678, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.query_choice = QComboBox(self.centralwidget)
        self.query_choice.addItem("")
        self.query_choice.addItem("")
        self.query_choice.addItem("")
        self.query_choice.addItem("")
        self.query_choice.addItem("")
        self.query_choice.addItem("")
        self.query_choice.setObjectName(u"query_choice")

        self.horizontalLayout_5.addWidget(self.query_choice)

        self.query_button = QPushButton(self.centralwidget)
        self.query_button.setObjectName(u"query_button")

        self.horizontalLayout_5.addWidget(self.query_button)

        self.average_score_query_button = QPushButton(self.centralwidget)
        self.average_score_query_button.setObjectName(u"average_score_query_button")

        self.horizontalLayout_5.addWidget(self.average_score_query_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.total_score_query_button = QPushButton(self.centralwidget)
        self.total_score_query_button.setObjectName(u"total_score_query_button")

        self.horizontalLayout_6.addWidget(self.total_score_query_button)

        self.rank_query_button = QPushButton(self.centralwidget)
        self.rank_query_button.setObjectName(u"rank_query_button")

        self.horizontalLayout_6.addWidget(self.rank_query_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_4 = QSpacerItem(428, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 834, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6210\u7ee9\u7ba1\u7406\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7", None))
        self.student_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5b66\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7", None))
        self.className.setItemText(0, QCoreApplication.translate("MainWindow", u"2401", None))
        self.className.setItemText(1, QCoreApplication.translate("MainWindow", u"2402", None))
        self.className.setItemText(2, QCoreApplication.translate("MainWindow", u"2403", None))
        self.className.setItemText(3, QCoreApplication.translate("MainWindow", u"2404", None))
        self.className.setItemText(4, QCoreApplication.translate("MainWindow", u"2405", None))
        self.className.setItemText(5, QCoreApplication.translate("MainWindow", u"2406", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6210\u7ee9\u5f55\u5165", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u79d1\u76ee", None))
        self.input_choice.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5fae\u79ef\u5206", None))
        self.input_choice.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u4ee3\u6570", None))
        self.input_choice.setItemText(2, QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u6570\u5b66", None))
        self.input_choice.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6982\u7387\u8bba\u4e0e\u6570\u7406\u7edf\u8ba1", None))
        self.input_choice.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u8bc6\u522b", None))
        self.input_choice.setItemText(5, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u63a7\u5236\u539f\u7406", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6210\u7ee9", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6210\u7ee9\u67e5\u8be2\u4e0e\u7edf\u8ba1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u79d1\u76ee", None))
        self.query_choice.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5fae\u79ef\u5206", None))
        self.query_choice.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u4ee3\u6570", None))
        self.query_choice.setItemText(2, QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u6570\u5b66", None))
        self.query_choice.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6982\u7387\u8bba\u4e0e\u6570\u7406\u7edf\u8ba1", None))
        self.query_choice.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u8bc6\u522b", None))
        self.query_choice.setItemText(5, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u63a7\u5236\u539f\u7406", None))

        self.query_button.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.average_score_query_button.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u73ed\u7ea7\u5e73\u5747\u5206", None))
        self.total_score_query_button.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u603b\u5206", None))
        self.rank_query_button.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u73ed\u7ea7\u6392\u540d", None))
    # retranslateUi

