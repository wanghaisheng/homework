# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_account.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 615)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 70, 461, 491))
        self.groupBox.setObjectName("groupBox")
        self.label_account = QtWidgets.QLabel(self.groupBox)
        self.label_account.setGeometry(QtCore.QRect(20, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_account.setFont(font)
        self.label_account.setStyleSheet("")
        self.label_account.setAlignment(QtCore.Qt.AlignCenter)
        self.label_account.setObjectName("label_account")
        self.label_web = QtWidgets.QLabel(self.groupBox)
        self.label_web.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_web.setFont(font)
        self.label_web.setAlignment(QtCore.Qt.AlignCenter)
        self.label_web.setObjectName("label_web")
        self.label_desc = QtWidgets.QLabel(self.groupBox)
        self.label_desc.setGeometry(QtCore.QRect(20, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_desc.setFont(font)
        self.label_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_desc.setObjectName("label_desc")
        self.label_caption = QtWidgets.QLabel(self.groupBox)
        self.label_caption.setGeometry(QtCore.QRect(20, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_caption.setFont(font)
        self.label_caption.setAlignment(QtCore.Qt.AlignCenter)
        self.label_caption.setObjectName("label_caption")
        self.label_title_tags = QtWidgets.QLabel(self.groupBox)
        self.label_title_tags.setGeometry(QtCore.QRect(20, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_title_tags.setFont(font)
        self.label_title_tags.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_tags.setObjectName("label_title_tags")
        self.label_tags = QtWidgets.QLabel(self.groupBox)
        self.label_tags.setGeometry(QtCore.QRect(20, 280, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_tags.setFont(font)
        self.label_tags.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tags.setObjectName("label_tags")
        self.label_title = QtWidgets.QLabel(self.groupBox)
        self.label_title.setGeometry(QtCore.QRect(20, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_type = QtWidgets.QLabel(self.groupBox)
        self.label_type.setGeometry(QtCore.QRect(20, 360, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_type.setFont(font)
        self.label_type.setAlignment(QtCore.Qt.AlignCenter)
        self.label_type.setObjectName("label_type")
        self.account = QtWidgets.QLineEdit(self.groupBox)
        self.account.setGeometry(QtCore.QRect(140, 40, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.account.setFont(font)
        self.account.setObjectName("account")
        self.web = QtWidgets.QComboBox(self.groupBox)
        self.web.setGeometry(QtCore.QRect(140, 80, 271, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.web.setFont(font)
        self.web.setObjectName("web")
        self.web.addItem("")
        self.web.addItem("")
        self.title = QtWidgets.QLineEdit(self.groupBox)
        self.title.setGeometry(QtCore.QRect(140, 120, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.description = QtWidgets.QLineEdit(self.groupBox)
        self.description.setGeometry(QtCore.QRect(140, 160, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.caption = QtWidgets.QLineEdit(self.groupBox)
        self.caption.setGeometry(QtCore.QRect(140, 200, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.caption.setFont(font)
        self.caption.setObjectName("caption")
        self.title_tags = QtWidgets.QLineEdit(self.groupBox)
        self.title_tags.setGeometry(QtCore.QRect(140, 240, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_tags.setFont(font)
        self.title_tags.setObjectName("title_tags")
        self.tags = QtWidgets.QLineEdit(self.groupBox)
        self.tags.setGeometry(QtCore.QRect(140, 280, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tags.setFont(font)
        self.tags.setObjectName("tags")
        self.type = QtWidgets.QComboBox(self.groupBox)
        self.type.setGeometry(QtCore.QRect(140, 360, 271, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.finished_btn = QtWidgets.QPushButton(self.groupBox)
        self.finished_btn.setGeometry(QtCore.QRect(170, 450, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.finished_btn.setFont(font)
        self.finished_btn.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.finished_btn.setObjectName("finished_btn")
        self.user_file_title = QtWidgets.QComboBox(self.groupBox)
        self.user_file_title.setGeometry(QtCore.QRect(140, 400, 271, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_file_title.setFont(font)
        self.user_file_title.setObjectName("user_file_title")
        self.user_file_title.addItem("")
        self.user_file_title.addItem("")
        self.label_user_file_title = QtWidgets.QLabel(self.groupBox)
        self.label_user_file_title.setGeometry(QtCore.QRect(20, 400, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_user_file_title.setFont(font)
        self.label_user_file_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_file_title.setObjectName("label_user_file_title")
        self.video_path = QtWidgets.QLineEdit(self.groupBox)
        self.video_path.setGeometry(QtCore.QRect(140, 320, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.video_path.setFont(font)
        self.video_path.setObjectName("video_path")
        self.label_video_path = QtWidgets.QLabel(self.groupBox)
        self.label_video_path.setGeometry(QtCore.QRect(20, 320, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_video_path.setFont(font)
        self.label_video_path.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video_path.setObjectName("label_video_path")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "添加账号"))
        self.label_account.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">account</span></p></body></html>"))
        self.label_web.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">web</span></p></body></html>"))
        self.label_desc.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">description</span></p></body></html>"))
        self.label_caption.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">caption</span></p></body></html>"))
        self.label_title_tags.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">title_tags</span></p></body></html>"))
        self.label_tags.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">tags</span></p></body></html>"))
        self.label_title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">title</span></p></body></html>"))
        self.label_type.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">type</span></p></body></html>"))
        self.web.setItemText(0, _translate("Dialog", "youtube"))
        self.web.setItemText(1, _translate("Dialog", "douyin"))
        self.type.setItemText(0, _translate("Dialog", "short"))
        self.type.setItemText(1, _translate("Dialog", "long"))
        self.finished_btn.setText(_translate("Dialog", "完成"))
        self.user_file_title.setItemText(0, _translate("Dialog", "true"))
        self.user_file_title.setItemText(1, _translate("Dialog", "false"))
        self.label_user_file_title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">use_file_title</span></p></body></html>"))
        self.label_video_path.setText(_translate("Dialog", "<html><head/><body><p>video_path</p></body></html>"))

