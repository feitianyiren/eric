# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/TranslationPropertiesDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TranslationPropertiesDialog(object):
    def setupUi(self, TranslationPropertiesDialog):
        TranslationPropertiesDialog.setObjectName("TranslationPropertiesDialog")
        TranslationPropertiesDialog.resize(592, 543)
        TranslationPropertiesDialog.setSizeGripEnabled(True)
        self._2 = QtWidgets.QVBoxLayout(TranslationPropertiesDialog)
        self._2.setObjectName("_2")
        self._3 = QtWidgets.QGridLayout()
        self._3.setObjectName("_3")
        self.transBinPathEdit = QtWidgets.QLineEdit(TranslationPropertiesDialog)
        self.transBinPathEdit.setObjectName("transBinPathEdit")
        self._3.addWidget(self.transBinPathEdit, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(TranslationPropertiesDialog)
        self.label.setObjectName("label")
        self._3.addWidget(self.label, 2, 0, 1, 2)
        self.transPatternEdit = QtWidgets.QLineEdit(TranslationPropertiesDialog)
        self.transPatternEdit.setObjectName("transPatternEdit")
        self._3.addWidget(self.transPatternEdit, 1, 0, 1, 1)
        self.textLabel1_3 = QtWidgets.QLabel(TranslationPropertiesDialog)
        self.textLabel1_3.setWordWrap(True)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self._3.addWidget(self.textLabel1_3, 0, 0, 1, 2)
        self.transPatternButton = QtWidgets.QToolButton(TranslationPropertiesDialog)
        self.transPatternButton.setObjectName("transPatternButton")
        self._3.addWidget(self.transPatternButton, 1, 1, 1, 1)
        self.transBinPathButton = QtWidgets.QToolButton(TranslationPropertiesDialog)
        self.transBinPathButton.setObjectName("transBinPathButton")
        self._3.addWidget(self.transBinPathButton, 3, 1, 1, 1)
        self._2.addLayout(self._3)
        self.exceptionsGroup = QtWidgets.QGroupBox(TranslationPropertiesDialog)
        self.exceptionsGroup.setObjectName("exceptionsGroup")
        self._4 = QtWidgets.QGridLayout(self.exceptionsGroup)
        self._4.setObjectName("_4")
        self.exceptDirButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.exceptDirButton.setObjectName("exceptDirButton")
        self._4.addWidget(self.exceptDirButton, 2, 3, 1, 1)
        self.exceptFileButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.exceptFileButton.setObjectName("exceptFileButton")
        self._4.addWidget(self.exceptFileButton, 2, 2, 1, 1)
        self.addExceptionButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.addExceptionButton.setEnabled(False)
        self.addExceptionButton.setObjectName("addExceptionButton")
        self._4.addWidget(self.addExceptionButton, 2, 1, 1, 1)
        self.deleteExceptionButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.deleteExceptionButton.setEnabled(False)
        self.deleteExceptionButton.setObjectName("deleteExceptionButton")
        self._4.addWidget(self.deleteExceptionButton, 2, 0, 1, 1)
        self.exceptionEdit = QtWidgets.QLineEdit(self.exceptionsGroup)
        self.exceptionEdit.setObjectName("exceptionEdit")
        self._4.addWidget(self.exceptionEdit, 1, 0, 1, 4)
        self.exceptionsList = QtWidgets.QListWidget(self.exceptionsGroup)
        self.exceptionsList.setAlternatingRowColors(True)
        self.exceptionsList.setObjectName("exceptionsList")
        self._4.addWidget(self.exceptionsList, 0, 0, 1, 4)
        self._2.addWidget(self.exceptionsGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(TranslationPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self._2.addWidget(self.buttonBox)
        self.label.setBuddy(self.transBinPathEdit)
        self.textLabel1_3.setBuddy(self.transPatternEdit)

        self.retranslateUi(TranslationPropertiesDialog)
        self.buttonBox.accepted.connect(TranslationPropertiesDialog.accept)
        self.buttonBox.rejected.connect(TranslationPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TranslationPropertiesDialog)
        TranslationPropertiesDialog.setTabOrder(self.transPatternEdit, self.transPatternButton)
        TranslationPropertiesDialog.setTabOrder(self.transPatternButton, self.transBinPathEdit)
        TranslationPropertiesDialog.setTabOrder(self.transBinPathEdit, self.transBinPathButton)
        TranslationPropertiesDialog.setTabOrder(self.transBinPathButton, self.exceptionsList)
        TranslationPropertiesDialog.setTabOrder(self.exceptionsList, self.exceptionEdit)
        TranslationPropertiesDialog.setTabOrder(self.exceptionEdit, self.deleteExceptionButton)
        TranslationPropertiesDialog.setTabOrder(self.deleteExceptionButton, self.addExceptionButton)
        TranslationPropertiesDialog.setTabOrder(self.addExceptionButton, self.exceptFileButton)
        TranslationPropertiesDialog.setTabOrder(self.exceptFileButton, self.exceptDirButton)

    def retranslateUi(self, TranslationPropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        TranslationPropertiesDialog.setWindowTitle(_translate("TranslationPropertiesDialog", "Translation Properties"))
        self.transBinPathEdit.setToolTip(_translate("TranslationPropertiesDialog", "Enter the path for the binary translation files (*.qm)"))
        self.transBinPathEdit.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Binary Translations Path</b>\n"
"<p>Enter the directory for the binary translation files (*.qm). Leave it empty to store them together with the *.ts files.</p>"))
        self.label.setText(_translate("TranslationPropertiesDialog", "&Binary Translations Path:"))
        self.transPatternEdit.setToolTip(_translate("TranslationPropertiesDialog", "Enter the path pattern for the translation files"))
        self.transPatternEdit.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Translation Pattern</b>\n"
"<p>Enter the path pattern for the translation files using %language% at the place of the language code (e.g. /path_to_eric/i18n/eric6_%language%.ts). This will result in translation files like /path_to_eric/i18n/eric6_de.ts.</p>"))
        self.textLabel1_3.setText(_translate("TranslationPropertiesDialog", "&Translation Path Pattern:\n"
"(Use \'%language%\' where the language code should be inserted, e.g. i18n/eric6_%language%.ts)"))
        self.transPatternButton.setToolTip(_translate("TranslationPropertiesDialog", "Show directory selection dialog"))
        self.transPatternButton.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Translation Pattern</b>\n"
"<p>Select a translation file via a file selection dialog.</p>"))
        self.transBinPathButton.setToolTip(_translate("TranslationPropertiesDialog", "Show directory selection dialog"))
        self.transBinPathButton.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Binary Translations Path</b>\n"
"<p>Select the directory for the binary translations via a directory selection dialog.</p>"))
        self.exceptionsGroup.setTitle(_translate("TranslationPropertiesDialog", "Exclude from translation"))
        self.exceptDirButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to select a directory via a selection dialog"))
        self.exceptDirButton.setText(_translate("TranslationPropertiesDialog", "Select d&irectory..."))
        self.exceptFileButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to select a file via a selection dialog"))
        self.exceptFileButton.setText(_translate("TranslationPropertiesDialog", "Select &file..."))
        self.addExceptionButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to add the entered path or file to the list"))
        self.addExceptionButton.setText(_translate("TranslationPropertiesDialog", "&Add"))
        self.deleteExceptionButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to delete the selected entry from the list"))
        self.deleteExceptionButton.setText(_translate("TranslationPropertiesDialog", "&Delete"))
        self.exceptionEdit.setToolTip(_translate("TranslationPropertiesDialog", "Enter a path or file to be added"))
        self.exceptionsList.setToolTip(_translate("TranslationPropertiesDialog", "List of paths or files to excude from translation"))
        self.exceptionsList.setSortingEnabled(True)

