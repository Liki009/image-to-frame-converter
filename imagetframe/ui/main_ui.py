# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/user/Documents/workdesk/project/imagetframe/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1150, 635)
        Dialog.setMinimumSize(QtCore.QSize(1150, 635))
        Dialog.setMaximumSize(QtCore.QSize(1150, 635))
        self.get_video = QtWidgets.QPushButton(Dialog)
        self.get_video.setGeometry(QtCore.QRect(120, 100, 141, 41))
        self.get_video.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.get_video.setObjectName("get_video")
        self.end_hr = QtWidgets.QSpinBox(Dialog)
        self.end_hr.setGeometry(QtCore.QRect(680, 320, 42, 22))
        self.end_hr.setObjectName("end_hr")
        self.end_min = QtWidgets.QSpinBox(Dialog)
        self.end_min.setGeometry(QtCore.QRect(750, 320, 42, 22))
        self.end_min.setMaximum(60)
        self.end_min.setObjectName("end_min")
        self.end_sec = QtWidgets.QSpinBox(Dialog)
        self.end_sec.setGeometry(QtCore.QRect(820, 320, 42, 22))
        self.end_sec.setMaximum(60)
        self.end_sec.setObjectName("end_sec")
        self.start_hr = QtWidgets.QSpinBox(Dialog)
        self.start_hr.setGeometry(QtCore.QRect(120, 320, 42, 22))
        self.start_hr.setObjectName("start_hr")
        self.start_min = QtWidgets.QSpinBox(Dialog)
        self.start_min.setGeometry(QtCore.QRect(190, 320, 42, 22))
        self.start_min.setMaximum(60)
        self.start_min.setObjectName("start_min")
        self.start_sec = QtWidgets.QSpinBox(Dialog)
        self.start_sec.setGeometry(QtCore.QRect(260, 320, 42, 22))
        self.start_sec.setMaximum(60)
        self.start_sec.setObjectName("start_sec")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 290, 181, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(690, 290, 181, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 320, 16, 16))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 320, 16, 16))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(730, 320, 16, 16))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(800, 320, 16, 16))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 570, 881, 31))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(50, 320, 61, 21))
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(620, 320, 51, 21))
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 610, 121, 16))
        self.label_11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.framerate = QtWidgets.QSpinBox(Dialog)
        self.framerate.setGeometry(QtCore.QRect(800, 110, 51, 31))
        self.framerate.setMinimum(1)
        self.framerate.setMaximum(120)
        self.framerate.setProperty("value", 10)
        self.framerate.setObjectName("framerate")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(710, 110, 81, 21))
        self.label_12.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(450, 230, 631, 31))
        self.label_13.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.open = QtWidgets.QLabel(Dialog)
        self.open.setGeometry(QtCore.QRect(70, 70, 501, 16))
        self.open.setObjectName("open")
        self.save_label = QtWidgets.QLabel(Dialog)
        self.save_label.setGeometry(QtCore.QRect(70, 150, 501, 16))
        self.save_label.setObjectName("save_label")
        self.save_frame = QtWidgets.QPushButton(Dialog)
        self.save_frame.setGeometry(QtCore.QRect(120, 190, 141, 41))
        self.save_frame.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.save_frame.setObjectName("save_frame")
        self.process = QtWidgets.QPushButton(Dialog)
        self.process.setGeometry(QtCore.QRect(670, 170, 201, 51))
        self.process.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.process.setObjectName("process")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(170, 430, 351, 31))
        self.label_14.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(170, 390, 261, 31))
        self.label_15.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(550, 360, 581, 192))
        self.textBrowser.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(360, 0, 451, 51))
        self.label_7.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.get_video.setText(_translate("Dialog", "open video file"))
        self.label.setText(_translate("Dialog", "hours              minutes           seconds"))
        self.label_2.setText(_translate("Dialog", "hours            minutes          seconds"))
        self.label_3.setText(_translate("Dialog", ":"))
        self.label_4.setText(_translate("Dialog", ":"))
        self.label_5.setText(_translate("Dialog", ":"))
        self.label_6.setText(_translate("Dialog", ":"))
        self.label_8.setText(_translate("Dialog", "warning: using excess frame rate can SERIOUSLY slow down your computer especially if you want to cut  long videos"))
        self.label_9.setText(_translate("Dialog", "start at:"))
        self.label_10.setText(_translate("Dialog", "end at:"))
        self.label_11.setText(_translate("Dialog", "made by likith c"))
        self.label_12.setText(_translate("Dialog", "framerate:"))
        self.label_13.setText(_translate("Dialog", "after selecting your file and a save  location please press process and wait for some time"))
        self.open.setText(_translate("Dialog", "open"))
        self.save_label.setText(_translate("Dialog", "save"))
        self.save_frame.setText(_translate("Dialog", "save frames at"))
        self.process.setText(_translate("Dialog", "process"))
        self.label_14.setText(_translate("Dialog", "total video length you selected:"))
        self.label_15.setText(_translate("Dialog", "video time:"))
        self.textBrowser.setPlaceholderText(_translate("Dialog", "current status"))
        self.label_7.setText(_translate("Dialog", "video to frame converter ver 1.0"))