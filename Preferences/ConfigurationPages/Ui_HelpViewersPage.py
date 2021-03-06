# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/HelpViewersPage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpViewersPage(object):
    def setupUi(self, HelpViewersPage):
        HelpViewersPage.setObjectName("HelpViewersPage")
        HelpViewersPage.resize(613, 634)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(HelpViewersPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headerLabel = QtWidgets.QLabel(HelpViewersPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_3.addWidget(self.headerLabel)
        self.line17 = QtWidgets.QFrame(HelpViewersPage)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setObjectName("line17")
        self.verticalLayout_3.addWidget(self.line17)
        self.groupBox = QtWidgets.QGroupBox(HelpViewersPage)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.customViewerEdit = QtWidgets.QLineEdit(self.groupBox)
        self.customViewerEdit.setEnabled(False)
        self.customViewerEdit.setObjectName("customViewerEdit")
        self.hboxlayout.addWidget(self.customViewerEdit)
        self.customViewerSelectionButton = QtWidgets.QToolButton(self.groupBox)
        self.customViewerSelectionButton.setEnabled(False)
        self.customViewerSelectionButton.setObjectName("customViewerSelectionButton")
        self.hboxlayout.addWidget(self.customViewerSelectionButton)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 4)
        self.customViewerButton = QtWidgets.QRadioButton(self.groupBox)
        self.customViewerButton.setObjectName("customViewerButton")
        self.gridlayout.addWidget(self.customViewerButton, 0, 3, 1, 1)
        self.qtAssistantButton = QtWidgets.QRadioButton(self.groupBox)
        self.qtAssistantButton.setObjectName("qtAssistantButton")
        self.gridlayout.addWidget(self.qtAssistantButton, 0, 1, 1, 1)
        self.helpBrowserButton = QtWidgets.QRadioButton(self.groupBox)
        self.helpBrowserButton.setChecked(True)
        self.helpBrowserButton.setObjectName("helpBrowserButton")
        self.gridlayout.addWidget(self.helpBrowserButton, 0, 0, 1, 1)
        self.webBrowserButton = QtWidgets.QRadioButton(self.groupBox)
        self.webBrowserButton.setObjectName("webBrowserButton")
        self.gridlayout.addWidget(self.webBrowserButton, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(479, 121, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(HelpViewersPage)
        self.customViewerButton.toggled['bool'].connect(self.customViewerEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(HelpViewersPage)
        HelpViewersPage.setTabOrder(self.helpBrowserButton, self.qtAssistantButton)
        HelpViewersPage.setTabOrder(self.qtAssistantButton, self.webBrowserButton)
        HelpViewersPage.setTabOrder(self.webBrowserButton, self.customViewerButton)
        HelpViewersPage.setTabOrder(self.customViewerButton, self.customViewerEdit)
        HelpViewersPage.setTabOrder(self.customViewerEdit, self.customViewerSelectionButton)

    def retranslateUi(self, HelpViewersPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("HelpViewersPage", "<b>Configure help viewers</b>"))
        self.groupBox.setTitle(_translate("HelpViewersPage", "Help Viewer"))
        self.customViewerEdit.setToolTip(_translate("HelpViewersPage", "Enter the custom viewer to be used"))
        self.customViewerSelectionButton.setToolTip(_translate("HelpViewersPage", "Press to select the custom viewer via a file selection dialog"))
        self.customViewerButton.setToolTip(_translate("HelpViewersPage", "Select to use a custom viewer"))
        self.customViewerButton.setText(_translate("HelpViewersPage", "Custom"))
        self.qtAssistantButton.setToolTip(_translate("HelpViewersPage", "Select to use Qt Assistant"))
        self.qtAssistantButton.setText(_translate("HelpViewersPage", "Qt Assistant"))
        self.helpBrowserButton.setToolTip(_translate("HelpViewersPage", "Select to use the Eric Web Browser"))
        self.helpBrowserButton.setText(_translate("HelpViewersPage", "Eric Web Browser"))
        self.webBrowserButton.setToolTip(_translate("HelpViewersPage", "Select to use the configured web browser of the system"))
        self.webBrowserButton.setText(_translate("HelpViewersPage", "System Web Browser"))

