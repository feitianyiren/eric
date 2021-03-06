# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/FindFileNameDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FindFileNameDialog(object):
    def setupUi(self, FindFileNameDialog):
        FindFileNameDialog.setObjectName("FindFileNameDialog")
        FindFileNameDialog.resize(599, 478)
        self.vboxlayout = QtWidgets.QVBoxLayout(FindFileNameDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.textLabel1 = QtWidgets.QLabel(FindFileNameDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.vboxlayout.addWidget(self.textLabel1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.fileNameEdit = QtWidgets.QLineEdit(FindFileNameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileNameEdit.sizePolicy().hasHeightForWidth())
        self.fileNameEdit.setSizePolicy(sizePolicy)
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.hboxlayout.addWidget(self.fileNameEdit)
        self.extsepLabel = QtWidgets.QLabel(FindFileNameDialog)
        self.extsepLabel.setObjectName("extsepLabel")
        self.hboxlayout.addWidget(self.extsepLabel)
        self.fileExtEdit = QtWidgets.QLineEdit(FindFileNameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileExtEdit.sizePolicy().hasHeightForWidth())
        self.fileExtEdit.setSizePolicy(sizePolicy)
        self.fileExtEdit.setObjectName("fileExtEdit")
        self.hboxlayout.addWidget(self.fileExtEdit)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.searchDirCheckBox = QtWidgets.QCheckBox(FindFileNameDialog)
        self.searchDirCheckBox.setEnabled(False)
        self.searchDirCheckBox.setObjectName("searchDirCheckBox")
        self.hboxlayout1.addWidget(self.searchDirCheckBox)
        self.searchDirEdit = QtWidgets.QLineEdit(FindFileNameDialog)
        self.searchDirEdit.setObjectName("searchDirEdit")
        self.hboxlayout1.addWidget(self.searchDirEdit)
        self.searchDirButton = QtWidgets.QToolButton(FindFileNameDialog)
        self.searchDirButton.setObjectName("searchDirButton")
        self.hboxlayout1.addWidget(self.searchDirButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.projectCheckBox = QtWidgets.QCheckBox(FindFileNameDialog)
        self.projectCheckBox.setObjectName("projectCheckBox")
        self.hboxlayout2.addWidget(self.projectCheckBox)
        self.syspathCheckBox = QtWidgets.QCheckBox(FindFileNameDialog)
        self.syspathCheckBox.setObjectName("syspathCheckBox")
        self.hboxlayout2.addWidget(self.syspathCheckBox)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.fileList = QtWidgets.QTreeWidget(FindFileNameDialog)
        self.fileList.setRootIsDecorated(False)
        self.fileList.setObjectName("fileList")
        self.vboxlayout.addWidget(self.fileList)
        self.buttonBox = QtWidgets.QDialogButtonBox(FindFileNameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(FindFileNameDialog)
        self.buttonBox.rejected.connect(FindFileNameDialog.close)
        QtCore.QMetaObject.connectSlotsByName(FindFileNameDialog)
        FindFileNameDialog.setTabOrder(self.fileNameEdit, self.fileExtEdit)
        FindFileNameDialog.setTabOrder(self.fileExtEdit, self.searchDirEdit)
        FindFileNameDialog.setTabOrder(self.searchDirEdit, self.searchDirButton)
        FindFileNameDialog.setTabOrder(self.searchDirButton, self.searchDirCheckBox)
        FindFileNameDialog.setTabOrder(self.searchDirCheckBox, self.projectCheckBox)
        FindFileNameDialog.setTabOrder(self.projectCheckBox, self.syspathCheckBox)
        FindFileNameDialog.setTabOrder(self.syspathCheckBox, self.fileList)

    def retranslateUi(self, FindFileNameDialog):
        _translate = QtCore.QCoreApplication.translate
        FindFileNameDialog.setWindowTitle(_translate("FindFileNameDialog", "Find File"))
        self.textLabel1.setText(_translate("FindFileNameDialog", "Enter filename (? matches any single character, * matches everything)"))
        self.fileNameEdit.setToolTip(_translate("FindFileNameDialog", "Enter file name to search for "))
        self.extsepLabel.setText(_translate("FindFileNameDialog", "."))
        self.fileExtEdit.setToolTip(_translate("FindFileNameDialog", "Enter file extension to search for"))
        self.searchDirCheckBox.setToolTip(_translate("FindFileNameDialog", "Enabled to include the entered directory into the search"))
        self.searchDirCheckBox.setText(_translate("FindFileNameDialog", "Search Path:"))
        self.searchDirEdit.setToolTip(_translate("FindFileNameDialog", "Enter the directory, the file should be searched in"))
        self.searchDirButton.setToolTip(_translate("FindFileNameDialog", "Press to select the directory, the file should be searched in"))
        self.projectCheckBox.setToolTip(_translate("FindFileNameDialog", "Select to search in the project path"))
        self.projectCheckBox.setText(_translate("FindFileNameDialog", "Search in &project"))
        self.projectCheckBox.setShortcut(_translate("FindFileNameDialog", "Alt+P"))
        self.syspathCheckBox.setToolTip(_translate("FindFileNameDialog", "Select to search in sys.path"))
        self.syspathCheckBox.setText(_translate("FindFileNameDialog", "Search in &sys.path"))
        self.syspathCheckBox.setShortcut(_translate("FindFileNameDialog", "Alt+S"))
        self.fileList.setSortingEnabled(True)
        self.fileList.headerItem().setText(0, _translate("FindFileNameDialog", "Filename"))
        self.fileList.headerItem().setText(1, _translate("FindFileNameDialog", "Path"))

