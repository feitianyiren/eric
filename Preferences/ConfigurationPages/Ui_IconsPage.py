# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/IconsPage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IconsPage(object):
    def setupUi(self, IconsPage):
        IconsPage.setObjectName("IconsPage")
        IconsPage.resize(539, 371)
        self.gridlayout = QtWidgets.QGridLayout(IconsPage)
        self.gridlayout.setObjectName("gridlayout")
        self.headerLabel = QtWidgets.QLabel(IconsPage)
        self.headerLabel.setObjectName("headerLabel")
        self.gridlayout.addWidget(self.headerLabel, 0, 0, 1, 2)
        self.line10 = QtWidgets.QFrame(IconsPage)
        self.line10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line10.setObjectName("line10")
        self.gridlayout.addWidget(self.line10, 1, 0, 1, 2)
        self.TextLabel1_2_2_2_2 = QtWidgets.QLabel(IconsPage)
        self.TextLabel1_2_2_2_2.setObjectName("TextLabel1_2_2_2_2")
        self.gridlayout.addWidget(self.TextLabel1_2_2_2_2, 2, 0, 1, 2)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.deleteIconDirectoryButton = QtWidgets.QPushButton(IconsPage)
        self.deleteIconDirectoryButton.setEnabled(False)
        self.deleteIconDirectoryButton.setObjectName("deleteIconDirectoryButton")
        self.hboxlayout.addWidget(self.deleteIconDirectoryButton)
        self.addIconDirectoryButton = QtWidgets.QPushButton(IconsPage)
        self.addIconDirectoryButton.setEnabled(False)
        self.addIconDirectoryButton.setObjectName("addIconDirectoryButton")
        self.hboxlayout.addWidget(self.addIconDirectoryButton)
        self.iconDirectoryEdit = QtWidgets.QLineEdit(IconsPage)
        self.iconDirectoryEdit.setObjectName("iconDirectoryEdit")
        self.hboxlayout.addWidget(self.iconDirectoryEdit)
        self.iconDirectoryButton = QtWidgets.QToolButton(IconsPage)
        self.iconDirectoryButton.setObjectName("iconDirectoryButton")
        self.hboxlayout.addWidget(self.iconDirectoryButton)
        self.gridlayout.addLayout(self.hboxlayout, 4, 0, 1, 1)
        self.showIconsButton = QtWidgets.QPushButton(IconsPage)
        self.showIconsButton.setEnabled(False)
        self.showIconsButton.setObjectName("showIconsButton")
        self.gridlayout.addWidget(self.showIconsButton, 4, 1, 1, 1)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 209, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.upButton = QtWidgets.QPushButton(IconsPage)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName("upButton")
        self.vboxlayout.addWidget(self.upButton)
        self.downButton = QtWidgets.QPushButton(IconsPage)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName("downButton")
        self.vboxlayout.addWidget(self.downButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.vboxlayout, 3, 1, 1, 1)
        self.iconDirectoryList = QtWidgets.QListWidget(IconsPage)
        self.iconDirectoryList.setAlternatingRowColors(True)
        self.iconDirectoryList.setObjectName("iconDirectoryList")
        self.gridlayout.addWidget(self.iconDirectoryList, 3, 0, 1, 1)

        self.retranslateUi(IconsPage)
        QtCore.QMetaObject.connectSlotsByName(IconsPage)
        IconsPage.setTabOrder(self.iconDirectoryList, self.upButton)
        IconsPage.setTabOrder(self.upButton, self.downButton)
        IconsPage.setTabOrder(self.downButton, self.deleteIconDirectoryButton)
        IconsPage.setTabOrder(self.deleteIconDirectoryButton, self.iconDirectoryEdit)
        IconsPage.setTabOrder(self.iconDirectoryEdit, self.iconDirectoryButton)
        IconsPage.setTabOrder(self.iconDirectoryButton, self.showIconsButton)
        IconsPage.setTabOrder(self.showIconsButton, self.addIconDirectoryButton)

    def retranslateUi(self, IconsPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("IconsPage", "<b>Configure icon directories</b>"))
        self.TextLabel1_2_2_2_2.setText(_translate("IconsPage", "<font color=\"#FF0000\"><b>Note:</b> These settings are activated at the next startup of the application.</font>"))
        self.deleteIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to delete the selected directory from the list"))
        self.deleteIconDirectoryButton.setText(_translate("IconsPage", "Delete"))
        self.addIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to add the entered directory to the list"))
        self.addIconDirectoryButton.setText(_translate("IconsPage", "Add"))
        self.iconDirectoryEdit.setToolTip(_translate("IconsPage", "Enter a directory to be added"))
        self.iconDirectoryButton.setToolTip(_translate("IconsPage", "Press to select an icon directory via a selection dialog"))
        self.showIconsButton.setText(_translate("IconsPage", "Show"))
        self.upButton.setText(_translate("IconsPage", "Up"))
        self.downButton.setText(_translate("IconsPage", "Down"))
        self.iconDirectoryList.setToolTip(_translate("IconsPage", "List of icon directories"))

