# Form implementation generated from reading ui file 'asset/GUI/gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 342)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(-2, 1, 417, 303))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, -2, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 11, 76, 30))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 10, 111, 36))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Kelas = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.Kelas.setObjectName("Kelas")
        self.verticalLayout_2.addWidget(self.Kelas)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(192, 12, 201, 30))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 243, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.Buka_File = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.Buka_File.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.Buka_File.setObjectName("Buka_File")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 108, 191, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.TR = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.TR.setGeometry(QtCore.QRect(60, 20, 81, 22))
        self.TR.setObjectName("TR")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 40, 19))
        self.label_6.setObjectName("label_6")
        self.Nilai_TR = QtWidgets.QTextEdit(parent=self.groupBox_3)
        self.Nilai_TR.setGeometry(QtCore.QRect(60, 47, 121, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Nilai_TR.setFont(font)
        self.Nilai_TR.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Nilai_TR.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Nilai_TR.setObjectName("Nilai_TR")
        self.Simpan_TR = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.Simpan_TR.setGeometry(QtCore.QRect(70, 100, 111, 23))
        self.Simpan_TR.setObjectName("Simpan_TR")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(parent=self.groupBox_3)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(50, 70, 148, 22))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(220, 108, 191, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.TA = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.TA.setGeometry(QtCore.QRect(60, 20, 81, 22))
        self.TA.setObjectName("TA")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 40, 19))
        self.label_9.setObjectName("label_9")
        self.Nilai_TA = QtWidgets.QTextEdit(parent=self.groupBox_4)
        self.Nilai_TA.setGeometry(QtCore.QRect(60, 47, 121, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Nilai_TA.setFont(font)
        self.Nilai_TA.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Nilai_TA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Nilai_TA.setObjectName("Nilai_TA")
        self.Simpan_TA = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.Simpan_TA.setGeometry(QtCore.QRect(70, 100, 111, 23))
        self.Simpan_TA.setObjectName("Simpan_TA")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(parent=self.groupBox_4)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(50, 70, 145, 22))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 53, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 96, 37))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(190, 16, 218, 22))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.NIM = QtWidgets.QTextEdit(parent=self.groupBox_2)
        self.NIM.setGeometry(QtCore.QRect(68, 16, 115, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NIM.sizePolicy().hasHeightForWidth())
        self.NIM.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.NIM.setFont(font)
        self.NIM.setToolTipDuration(-9)
        self.NIM.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.NIM.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.NIM.setAcceptRichText(True)
        self.NIM.setObjectName("NIM")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_About = QtWidgets.QMenu(parent=self.menubar)
        self.menu_About.setObjectName("menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Open_File = QtGui.QAction(parent=MainWindow)
        self.Open_File.setObjectName("Open_File")
        self.Quit = QtGui.QAction(parent=MainWindow)
        self.Quit.setObjectName("Quit")
        self.About = QtGui.QAction(parent=MainWindow)
        self.About.setObjectName("About")
        self.menu_File.addAction(self.Open_File)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.Quit)
        self.menu_About.addAction(self.About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)
        self.Quit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EZRecap"))
        self.groupBox.setTitle(_translate("MainWindow", "KELAS"))
        self.label.setText(_translate("MainWindow", "KELAS :"))
        self.label_2.setText(_translate("MainWindow", "*Pilih kelas disini"))
        self.groupBox_5.setTitle(_translate("MainWindow", "ACTION"))
        self.Buka_File.setText(_translate("MainWindow", "BUKA FILE"))
        self.groupBox_3.setTitle(_translate("MainWindow", "TUGAS RUMAH"))
        self.label_5.setText(_translate("MainWindow", "TR      :"))
        self.label_6.setText(_translate("MainWindow", "NILAI :"))
        self.Nilai_TR.setPlaceholderText(_translate("MainWindow", "0 s/d 100"))
        self.Simpan_TR.setText(_translate("MainWindow", "SIMPAN NILAI TR"))
        self.label_7.setText(_translate("MainWindow", "*Masukkan nilai TR disini"))
        self.groupBox_4.setTitle(_translate("MainWindow", "TEST AWAL"))
        self.label_8.setText(_translate("MainWindow", "TA      :"))
        self.label_9.setText(_translate("MainWindow", "NILAI :"))
        self.Nilai_TA.setPlaceholderText(_translate("MainWindow", "0 s/d 100"))
        self.Simpan_TA.setText(_translate("MainWindow", "SIMPAN NILAI TA"))
        self.label_10.setText(_translate("MainWindow", "*Masukkan nilai TA disini"))
        self.groupBox_2.setTitle(_translate("MainWindow", "NIM"))
        self.label_3.setText(_translate("MainWindow", "NIM     :"))
        self.label_4.setText(_translate("MainWindow", "*Masukkan NIM praktikan disini"))
        self.NIM.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Semibold\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.NIM.setPlaceholderText(_translate("MainWindow", "ex: 202111129"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_About.setTitle(_translate("MainWindow", "&About"))
        self.Open_File.setText(_translate("MainWindow", "&Pilih File"))
        self.Quit.setText(_translate("MainWindow", "&Keluar"))
        self.About.setText(_translate("MainWindow", "&About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
