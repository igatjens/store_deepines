# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guis/card.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(230, 252)
        Frame.setMinimumSize(QtCore.QSize(226, 249))
        Frame.setMaximumSize(QtCore.QSize(230, 16777215))
        Frame.setStyleSheet("#Frame{\n"
"    background-color: transparent;\n"
"}\n"
"QToolTip {\n"
"    border: 2px solid #419fd9;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-size: 12px;\n"
"    color: white;\n"
"    background-color: transparent;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_app = QtWidgets.QLabel(Frame)
        self.image_app.setMinimumSize(QtCore.QSize(208, 158))
        self.image_app.setMaximumSize(QtCore.QSize(208, 158))
        self.image_app.setStyleSheet("#image_app{\n"
"  background-color: rgb(45, 45, 45);\n"
"  border: 10px outset rgb(45, 45, 45);\n"
"}")
        self.image_app.setText("")
        self.image_app.setScaledContents(False)
        self.image_app.setAlignment(QtCore.Qt.AlignCenter)
        self.image_app.setObjectName("image_app")
        self.verticalLayout.addWidget(self.image_app)
        self.lbl_name_app = QtWidgets.QLabel(Frame)
        self.lbl_name_app.setMinimumSize(QtCore.QSize(0, 25))
        self.lbl_name_app.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lbl_name_app.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.lbl_name_app.setText("")
        self.lbl_name_app.setScaledContents(False)
        self.lbl_name_app.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name_app.setWordWrap(True)
        self.lbl_name_app.setObjectName("lbl_name_app")
        self.verticalLayout.addWidget(self.lbl_name_app)
        self.btn_select_app = QtWidgets.QPushButton(Frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setItalic(False)
        self.btn_select_app.setFont(font)
        self.btn_select_app.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select_app.setStyleSheet("#btn_select_app{\n"
"padding: 7px;\n"
"color: white;\n"
"border-radius: 5px;\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"#btn_select_app:hover{\n"
"border: 1px solid rgb(142, 231, 255);\n"
"padding: 7px;\n"
"color:white;\n"
"background-color: rgb(65, 159, 217);\n"
"border-radius: 5px;\n"
"}")
        self.btn_select_app.setObjectName("btn_select_app")
        self.verticalLayout.addWidget(self.btn_select_app)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Card"))
        self.btn_select_app.setText(_translate("Frame", "Instalar"))
