# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import join, abspath

ICONS_PATH = abspath("./view/ui_views/icons")
OPEN_FILE_ICON = "open_ico.png"


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 322)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.projectNameLabel = QtWidgets.QLabel(Dialog)
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.projectNameLabel)
        self.projectNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.projectNameLineEdit.setObjectName("projectNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.projectNameLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.authorNameLabel = QtWidgets.QLabel(Dialog)
        self.authorNameLabel.setObjectName("authorNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.authorNameLabel)
        self.authorNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.authorNameLineEdit.setObjectName("authorNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.authorNameLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.sourceLinkLabel = QtWidgets.QLabel(Dialog)
        self.sourceLinkLabel.setObjectName("sourceLinkLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sourceLinkLabel)
        self.sourceLinkLineEdit = QtWidgets.QLineEdit(Dialog)
        self.sourceLinkLineEdit.setObjectName("sourceLinkLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sourceLinkLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.filePathLabel = QtWidgets.QLabel(Dialog)
        self.filePathLabel.setObjectName("filePathLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.filePathLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filePathLineEdit = QtWidgets.QLineEdit(Dialog)
        self.filePathLineEdit.setAutoFillBackground(True)
        self.filePathLineEdit.setReadOnly(True)
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        self.filePathLineEdit.setStyleSheet("background-color: lightgrey")
        self.horizontalLayout.addWidget(self.filePathLineEdit)
        self.filePathToolButton = QtWidgets.QToolButton(Dialog)
        icon = QtGui.QIcon(join(ICONS_PATH, OPEN_FILE_ICON))
        self.filePathToolButton.setIcon(icon)
        self.filePathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.filePathToolButton.setObjectName("filePathToolButton")
        self.horizontalLayout.addWidget(self.filePathToolButton)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.createPushButton = QtWidgets.QPushButton(Dialog)
        self.createPushButton.setObjectName("createPushButton")
        self.horizontalLayout_2.addWidget(self.createPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(Dialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_2.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новый проект"))
        self.projectNameLabel.setText(_translate("Dialog", "Название проекта: "))
        self.authorNameLabel.setText(_translate("Dialog", "Имя автора: "))
        self.sourceLinkLabel.setText(_translate("Dialog", "Ссылка на источник:"))
        self.filePathLabel.setText(_translate("Dialog", "Файл: "))
        self.filePathToolButton.setText(_translate("Dialog", "..."))
        self.createPushButton.setText(_translate("Dialog", "Создать"))
        self.cancelPushButton.setText(_translate("Dialog", "Отмена"))