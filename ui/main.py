# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("*{\n"
"    font-family: \'Circe\';\n"
"    color: white;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"#question {\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: rgba(255, 255, 255, 128);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 160, 160, 128);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(180, 180, 180, 128);\n"
"}\n"
"\n"
"QPushButton:disabled:hover {\n"
"    background-color: rgba(192, 57, 43, 128);\n"
"}\n"
"\n"
"#centralwidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0.531, y1:0, x2:0.559, y2:1, stop:0.145251 rgba(127, 0, 93, 255), stop:0.836158 rgba(0, 0, 70, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"/*\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"\n"
"qlineargradient(to top, #505285 0%, #585e92 12%, #65689f 25%, #7474b0 37%, #7e7ebb 50%, #8389c7 62%, #9795d4 75%, #a2a1dc 87%, #b5aee4 100%);\n"
"*/")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Circe")
        font.setPointSize(18)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size: 18pt;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.question = QtWidgets.QTextBrowser(self.centralwidget)
        self.question.setStyleSheet("font-size: 18pt;\n"
"background-color: rgba(255, 255, 255, 128);\n"
"border: 1px solid white;\n"
"border-radius: 24px;")
        self.question.setObjectName("question")
        self.verticalLayout.addWidget(self.question)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(20)
        self.frame.setMidLineWidth(9)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.answer_0 = QtWidgets.QPushButton(self.centralwidget)
        self.answer_0.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_0.sizePolicy().hasHeightForWidth())
        self.answer_0.setSizePolicy(sizePolicy)
        self.answer_0.setStyleSheet("font-size: 32pt;")
        self.answer_0.setObjectName("answer_0")
        self.horizontalLayout_2.addWidget(self.answer_0)
        self.answer_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_1.sizePolicy().hasHeightForWidth())
        self.answer_1.setSizePolicy(sizePolicy)
        self.answer_1.setStyleSheet("font-size: 32pt;")
        self.answer_1.setObjectName("answer_1")
        self.horizontalLayout_2.addWidget(self.answer_1)
        self.answer_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_2.sizePolicy().hasHeightForWidth())
        self.answer_2.setSizePolicy(sizePolicy)
        self.answer_2.setStyleSheet("font-size: 32pt;")
        self.answer_2.setObjectName("answer_2")
        self.horizontalLayout_2.addWidget(self.answer_2)
        self.answer_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_3.sizePolicy().hasHeightForWidth())
        self.answer_3.setSizePolicy(sizePolicy)
        self.answer_3.setStyleSheet("font-size: 32pt;")
        self.answer_3.setObjectName("answer_3")
        self.horizontalLayout_2.addWidget(self.answer_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, 20, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_prev_question = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prev_question.setObjectName("btn_prev_question")
        self.horizontalLayout.addWidget(self.btn_prev_question)
        self.btn_next_question = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next_question.sizePolicy().hasHeightForWidth())
        self.btn_next_question.setSizePolicy(sizePolicy)
        self.btn_next_question.setObjectName("btn_next_question")
        self.horizontalLayout.addWidget(self.btn_next_question)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 107)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.test_time = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_time.sizePolicy().hasHeightForWidth())
        self.test_time.setSizePolicy(sizePolicy)
        self.test_time.setStyleSheet("font-family: \"Circe ExtraBold\";\n"
"font-size: 70pt;")
        self.test_time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.test_time.setAlignment(QtCore.Qt.AlignCenter)
        self.test_time.setObjectName("test_time")
        self.verticalLayout_2.addWidget(self.test_time)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Circe")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.current_question = QtWidgets.QSpinBox(self.groupBox)
        self.current_question.setMouseTracking(False)
        self.current_question.setFocusPolicy(QtCore.Qt.NoFocus)
        self.current_question.setStyleSheet("color: black;\n"
"background-color: rgba(255, 255, 255, 128);")
        self.current_question.setFrame(False)
        self.current_question.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.current_question.setObjectName("current_question")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.current_question)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.answered_count = QtWidgets.QLabel(self.groupBox)
        self.answered_count.setObjectName("answered_count")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.answered_count)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Circe")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.test_theme = QtWidgets.QLabel(self.groupBox)
        self.test_theme.setObjectName("test_theme")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.test_theme)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.show_unanswered = QtWidgets.QPushButton(self.groupBox_2)
        self.show_unanswered.setAutoDefault(False)
        self.show_unanswered.setDefault(False)
        self.show_unanswered.setFlat(False)
        self.show_unanswered.setObjectName("show_unanswered")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.show_unanswered)
        self.finish_test_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.finish_test_btn.setObjectName("finish_test_btn")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.finish_test_btn)
        self.show_theory_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.show_theory_btn.setObjectName("show_theory_btn")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.show_theory_btn)
        self.gridLayout_2.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа для тестирования"))
        self.label_4.setText(_translate("MainWindow", "Выберите правильный ответ"))
        self.question.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Circe\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdfsdfsdfsdf</p></body></html>"))
        self.answer_0.setText(_translate("MainWindow", "а"))
        self.answer_0.setShortcut(_translate("MainWindow", "А"))
        self.answer_1.setText(_translate("MainWindow", "б"))
        self.answer_1.setShortcut(_translate("MainWindow", "Б"))
        self.answer_2.setText(_translate("MainWindow", "в"))
        self.answer_2.setShortcut(_translate("MainWindow", "В"))
        self.answer_3.setText(_translate("MainWindow", "г"))
        self.answer_3.setShortcut(_translate("MainWindow", "Г"))
        self.btn_prev_question.setText(_translate("MainWindow", "<<<"))
        self.btn_prev_question.setShortcut(_translate("MainWindow", "Left"))
        self.btn_next_question.setText(_translate("MainWindow", ">>>"))
        self.btn_next_question.setShortcut(_translate("MainWindow", "Right"))
        self.test_time.setText(_translate("MainWindow", "00:00"))
        self.groupBox.setTitle(_translate("MainWindow", "Вопросы"))
        self.label.setText(_translate("MainWindow", "Текущий вопрос"))
        self.label_2.setText(_translate("MainWindow", "Кол-во отвеченных:"))
        self.answered_count.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Тема теста:"))
        self.test_theme.setText(_translate("MainWindow", "{theme}"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Управление тестом"))
        self.show_unanswered.setText(_translate("MainWindow", "Показать вопросы без ответов"))
        self.finish_test_btn.setText(_translate("MainWindow", "Завершить тест"))
        self.show_theory_btn.setText(_translate("MainWindow", "Теория по тесту"))