# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/WizardPlugins/QRegExpWizard/QRegExpWizardRepeatDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QRegExpWizardRepeatDialog(object):
    def setupUi(self, QRegExpWizardRepeatDialog):
        QRegExpWizardRepeatDialog.setObjectName("QRegExpWizardRepeatDialog")
        QRegExpWizardRepeatDialog.resize(331, 197)
        QRegExpWizardRepeatDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(QRegExpWizardRepeatDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtWidgets.QGroupBox(QRegExpWizardRepeatDialog)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1_6 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_6.setObjectName("textLabel1_6")
        self.gridlayout.addWidget(self.textLabel1_6, 2, 2, 1, 1)
        self.textLabel1_7 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_7.setObjectName("textLabel1_7")
        self.gridlayout.addWidget(self.textLabel1_7, 3, 2, 1, 1)
        self.textLabel1_5 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_5.setObjectName("textLabel1_5")
        self.gridlayout.addWidget(self.textLabel1_5, 1, 2, 1, 1)
        self.lowerSpin = QtWidgets.QSpinBox(self.groupBox)
        self.lowerSpin.setEnabled(False)
        self.lowerSpin.setAlignment(QtCore.Qt.AlignRight)
        self.lowerSpin.setProperty("value", 1)
        self.lowerSpin.setObjectName("lowerSpin")
        self.gridlayout.addWidget(self.lowerSpin, 4, 1, 1, 1)
        self.upperSpin = QtWidgets.QSpinBox(self.groupBox)
        self.upperSpin.setEnabled(False)
        self.upperSpin.setAlignment(QtCore.Qt.AlignRight)
        self.upperSpin.setProperty("value", 1)
        self.upperSpin.setObjectName("upperSpin")
        self.gridlayout.addWidget(self.upperSpin, 4, 3, 1, 1)
        self.textLabel6 = QtWidgets.QLabel(self.groupBox)
        self.textLabel6.setObjectName("textLabel6")
        self.gridlayout.addWidget(self.textLabel6, 4, 2, 1, 1)
        self.betweenButton = QtWidgets.QRadioButton(self.groupBox)
        self.betweenButton.setObjectName("betweenButton")
        self.gridlayout.addWidget(self.betweenButton, 4, 0, 1, 1)
        self.exactSpin = QtWidgets.QSpinBox(self.groupBox)
        self.exactSpin.setEnabled(False)
        self.exactSpin.setAlignment(QtCore.Qt.AlignRight)
        self.exactSpin.setProperty("value", 1)
        self.exactSpin.setObjectName("exactSpin")
        self.gridlayout.addWidget(self.exactSpin, 3, 1, 1, 1)
        self.exactButton = QtWidgets.QRadioButton(self.groupBox)
        self.exactButton.setObjectName("exactButton")
        self.gridlayout.addWidget(self.exactButton, 3, 0, 1, 1)
        self.maxSpin = QtWidgets.QSpinBox(self.groupBox)
        self.maxSpin.setEnabled(False)
        self.maxSpin.setAlignment(QtCore.Qt.AlignRight)
        self.maxSpin.setProperty("value", 1)
        self.maxSpin.setObjectName("maxSpin")
        self.gridlayout.addWidget(self.maxSpin, 2, 1, 1, 1)
        self.maxButton = QtWidgets.QRadioButton(self.groupBox)
        self.maxButton.setObjectName("maxButton")
        self.gridlayout.addWidget(self.maxButton, 2, 0, 1, 1)
        self.minButton = QtWidgets.QRadioButton(self.groupBox)
        self.minButton.setObjectName("minButton")
        self.gridlayout.addWidget(self.minButton, 1, 0, 1, 1)
        self.minSpin = QtWidgets.QSpinBox(self.groupBox)
        self.minSpin.setEnabled(False)
        self.minSpin.setAlignment(QtCore.Qt.AlignRight)
        self.minSpin.setProperty("value", 1)
        self.minSpin.setObjectName("minSpin")
        self.gridlayout.addWidget(self.minSpin, 1, 1, 1, 1)
        self.unlimitedButton = QtWidgets.QRadioButton(self.groupBox)
        self.unlimitedButton.setObjectName("unlimitedButton")
        self.gridlayout.addWidget(self.unlimitedButton, 0, 0, 1, 4)
        self.vboxlayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(QRegExpWizardRepeatDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(QRegExpWizardRepeatDialog)
        self.minButton.toggled['bool'].connect(self.minSpin.setEnabled)
        self.maxButton.toggled['bool'].connect(self.maxSpin.setEnabled)
        self.exactButton.toggled['bool'].connect(self.exactSpin.setEnabled)
        self.betweenButton.toggled['bool'].connect(self.lowerSpin.setEnabled)
        self.betweenButton.toggled['bool'].connect(self.upperSpin.setEnabled)
        self.buttonBox.accepted.connect(QRegExpWizardRepeatDialog.accept)
        self.buttonBox.rejected.connect(QRegExpWizardRepeatDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QRegExpWizardRepeatDialog)
        QRegExpWizardRepeatDialog.setTabOrder(self.unlimitedButton, self.minButton)
        QRegExpWizardRepeatDialog.setTabOrder(self.minButton, self.minSpin)
        QRegExpWizardRepeatDialog.setTabOrder(self.minSpin, self.maxButton)
        QRegExpWizardRepeatDialog.setTabOrder(self.maxButton, self.maxSpin)
        QRegExpWizardRepeatDialog.setTabOrder(self.maxSpin, self.exactButton)
        QRegExpWizardRepeatDialog.setTabOrder(self.exactButton, self.exactSpin)
        QRegExpWizardRepeatDialog.setTabOrder(self.exactSpin, self.betweenButton)
        QRegExpWizardRepeatDialog.setTabOrder(self.betweenButton, self.lowerSpin)
        QRegExpWizardRepeatDialog.setTabOrder(self.lowerSpin, self.upperSpin)

    def retranslateUi(self, QRegExpWizardRepeatDialog):
        _translate = QtCore.QCoreApplication.translate
        QRegExpWizardRepeatDialog.setWindowTitle(_translate("QRegExpWizardRepeatDialog", "Number of repetitions"))
        self.textLabel1_6.setText(_translate("QRegExpWizardRepeatDialog", "times"))
        self.textLabel1_7.setText(_translate("QRegExpWizardRepeatDialog", "times"))
        self.textLabel1_5.setText(_translate("QRegExpWizardRepeatDialog", "times"))
        self.textLabel6.setText(_translate("QRegExpWizardRepeatDialog", "and"))
        self.betweenButton.setText(_translate("QRegExpWizardRepeatDialog", "Between"))
        self.exactButton.setText(_translate("QRegExpWizardRepeatDialog", "Exactly"))
        self.maxButton.setText(_translate("QRegExpWizardRepeatDialog", "Maximum"))
        self.minButton.setText(_translate("QRegExpWizardRepeatDialog", "Minimum"))
        self.unlimitedButton.setText(_translate("QRegExpWizardRepeatDialog", "Unlimited (incl. zero times)"))
