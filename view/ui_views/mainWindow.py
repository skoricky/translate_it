# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.createToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.createToolButton.setObjectName("createToolButton")
        self.horizontalLayout_4.addWidget(self.createToolButton)
        self.openToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.openToolButton.setObjectName("openToolButton")
        self.horizontalLayout_4.addWidget(self.openToolButton)
        self.saveToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.saveToolButton.setObjectName("saveToolButton")
        self.horizontalLayout_4.addWidget(self.saveToolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.exitToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.exitToolButton.setObjectName("exitToolButton")
        self.horizontalLayout_4.addWidget(self.exitToolButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        self.originalPartWidget = QtWidgets.QWidget(self.centralwidget)
        self.originalPartWidget.setObjectName("originalPartWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.originalPartWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.originalListWidget = QtWidgets.QListWidget(self.originalPartWidget)
        self.originalListWidget.setMinimumSize(QtCore.QSize(600, 458))
        self.originalListWidget.setMaximumSize(QtCore.QSize(10000, 10000000))
        self.originalListWidget.setWordWrap(True)
        self.originalListWidget.setObjectName("originalListWidget")
        self.gridLayout.addWidget(self.originalListWidget, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.originalPartWidget, 1, 0, 1, 1)
        self.translatedPartStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.translatedPartStackedWidget.setSizeIncrement(QtCore.QSize(2, 0))
        self.translatedPartStackedWidget.setObjectName("translatedPartStackedWidget")
        self.listPage = QtWidgets.QWidget()
        self.listPage.setObjectName("listPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.listPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.translatedListWidget = QtWidgets.QListWidget(self.listPage)
        self.translatedListWidget.setMinimumSize(QtCore.QSize(600, 458))
        self.translatedListWidget.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.translatedListWidget.setWordWrap(True)
        self.translatedListWidget.setObjectName("translatedListWidget")
        self.gridLayout_2.addWidget(self.translatedListWidget, 0, 0, 1, 1)
        self.translatedPartStackedWidget.addWidget(self.listPage)
        self.editorPage = QtWidgets.QWidget()
        self.editorPage.setObjectName("editorPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.editorPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.saveBlockPushButton = QtWidgets.QPushButton(self.editorPage)
        self.saveBlockPushButton.setObjectName("saveBlockPushButton")
        self.horizontalLayout_3.addWidget(self.saveBlockPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.translateApiPushButton = QtWidgets.QPushButton(self.editorPage)
        self.translateApiPushButton.setObjectName("translateApiPushButton")
        self.horizontalLayout_2.addWidget(self.translateApiPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.originalTextEdit = QtWidgets.QTextEdit(self.editorPage)
        self.originalTextEdit.setReadOnly(True)
        self.originalTextEdit.setFontPointSize(9.0)
        self.originalTextEdit.setObjectName("originalTextEdit")
        self.gridLayout_3.addWidget(self.originalTextEdit, 1, 0, 1, 1)
        self.translatedTextEdit = QtWidgets.QTextEdit(self.editorPage)
        self.translatedTextEdit.setObjectName("translatedTextEdit")
        self.translatedTextEdit.setFontPointSize(9.0)
        self.gridLayout_3.addWidget(self.translatedTextEdit, 2, 0, 1, 1)
        self.translatedPartStackedWidget.addWidget(self.editorPage)
        self.gridLayout_4.addWidget(self.translatedPartStackedWidget, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.workWithBlockPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.workWithBlockPushButton.setObjectName("workWithBlockPushButton")
        self.horizontalLayout.addWidget(self.workWithBlockPushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.translatedPartStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createToolButton.setText(_translate("MainWindow", "..."))
        self.openToolButton.setText(_translate("MainWindow", "..."))
        self.saveToolButton.setText(_translate("MainWindow", "..."))
        self.exitToolButton.setText(_translate("MainWindow", "..."))
        self.saveBlockPushButton.setText(_translate("MainWindow", "Сохранить блок"))
        self.translateApiPushButton.setText(_translate("MainWindow", "Перевести"))
        self.workWithBlockPushButton.setText(_translate("MainWindow", "Перевести блок"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Создать"))
        self.action_3.setText(_translate("MainWindow", "Открыть"))
        self.action_5.setText(_translate("MainWindow", "Сохранить"))
        self.action_7.setText(_translate("MainWindow", "Выйти"))

