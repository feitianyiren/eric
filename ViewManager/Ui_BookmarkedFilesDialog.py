# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ViewManager/BookmarkedFilesDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookmarkedFilesDialog(object):
    def setupUi(self, BookmarkedFilesDialog):
        BookmarkedFilesDialog.setObjectName("BookmarkedFilesDialog")
        BookmarkedFilesDialog.resize(475, 391)
        BookmarkedFilesDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(BookmarkedFilesDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.filesList = QtWidgets.QListWidget(BookmarkedFilesDialog)
        self.filesList.setAlternatingRowColors(True)
        self.filesList.setObjectName("filesList")
        self.gridlayout.addWidget(self.filesList, 0, 0, 6, 3)
        self.deleteButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.gridlayout.addWidget(self.deleteButton, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(87, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 5, 3, 1, 1)
        self.upButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName("upButton")
        self.gridlayout.addWidget(self.upButton, 3, 3, 1, 1)
        self.downButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName("downButton")
        self.gridlayout.addWidget(self.downButton, 4, 3, 1, 1)
        self.addButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName("addButton")
        self.gridlayout.addWidget(self.addButton, 0, 3, 1, 1)
        self.TextLabel1 = QtWidgets.QLabel(BookmarkedFilesDialog)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridlayout.addWidget(self.TextLabel1, 6, 0, 1, 1)
        self.changeButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.changeButton.setEnabled(False)
        self.changeButton.setObjectName("changeButton")
        self.gridlayout.addWidget(self.changeButton, 1, 3, 1, 1)
        self.fileEdit = QtWidgets.QLineEdit(BookmarkedFilesDialog)
        self.fileEdit.setObjectName("fileEdit")
        self.gridlayout.addWidget(self.fileEdit, 6, 1, 1, 1)
        self.fileButton = QtWidgets.QToolButton(BookmarkedFilesDialog)
        self.fileButton.setObjectName("fileButton")
        self.gridlayout.addWidget(self.fileButton, 6, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(BookmarkedFilesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.TextLabel1.setBuddy(self.fileEdit)

        self.retranslateUi(BookmarkedFilesDialog)
        self.buttonBox.accepted.connect(BookmarkedFilesDialog.accept)
        self.buttonBox.rejected.connect(BookmarkedFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarkedFilesDialog)
        BookmarkedFilesDialog.setTabOrder(self.filesList, self.addButton)
        BookmarkedFilesDialog.setTabOrder(self.addButton, self.changeButton)
        BookmarkedFilesDialog.setTabOrder(self.changeButton, self.deleteButton)
        BookmarkedFilesDialog.setTabOrder(self.deleteButton, self.upButton)
        BookmarkedFilesDialog.setTabOrder(self.upButton, self.downButton)
        BookmarkedFilesDialog.setTabOrder(self.downButton, self.fileEdit)
        BookmarkedFilesDialog.setTabOrder(self.fileEdit, self.fileButton)

    def retranslateUi(self, BookmarkedFilesDialog):
        _translate = QtCore.QCoreApplication.translate
        BookmarkedFilesDialog.setWindowTitle(_translate("BookmarkedFilesDialog", "Configure Bookmarked Files Menu"))
        self.deleteButton.setToolTip(_translate("BookmarkedFilesDialog", "Delete the selected entry"))
        self.deleteButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Delete</b>\n"
"<p>Delete the selected entry.</p>"))
        self.deleteButton.setText(_translate("BookmarkedFilesDialog", "&Delete"))
        self.deleteButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+D"))
        self.upButton.setToolTip(_translate("BookmarkedFilesDialog", "Move up"))
        self.upButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Move Up</b>\n"
"<p>Move the selected entry up.</p>"))
        self.upButton.setText(_translate("BookmarkedFilesDialog", "&Up"))
        self.upButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+U"))
        self.downButton.setToolTip(_translate("BookmarkedFilesDialog", "Move down"))
        self.downButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Move Down</b>\n"
"<p>Move the selected entry down.</p>"))
        self.downButton.setText(_translate("BookmarkedFilesDialog", "&Down"))
        self.downButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+D"))
        self.addButton.setToolTip(_translate("BookmarkedFilesDialog", "Add a new bookmarked file"))
        self.addButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Add</b>\n"
"<p>Add a new bookmarked file with the value entered below.</p>"))
        self.addButton.setText(_translate("BookmarkedFilesDialog", "&Add"))
        self.addButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+A"))
        self.TextLabel1.setText(_translate("BookmarkedFilesDialog", "&File:"))
        self.changeButton.setToolTip(_translate("BookmarkedFilesDialog", "Change the value of the selected entry"))
        self.changeButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Change</b>\n"
"<p>Change the value of the selected entry.</p>"))
        self.changeButton.setText(_translate("BookmarkedFilesDialog", "C&hange"))
        self.changeButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+H"))
        self.fileEdit.setToolTip(_translate("BookmarkedFilesDialog", "Enter the filename of the file"))
        self.fileEdit.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>File</b>\n"
"<p>Enter the filename of the bookmarked file.</p>"))
        self.fileButton.setToolTip(_translate("BookmarkedFilesDialog", "Select the file via a file selection dialog"))
        self.fileButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>File</b>\n"
"<p>Select the file to be bookmarked via a file selection dialog.</p>"))

