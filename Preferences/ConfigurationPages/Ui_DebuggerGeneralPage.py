# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/DebuggerGeneralPage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DebuggerGeneralPage(object):
    def setupUi(self, DebuggerGeneralPage):
        DebuggerGeneralPage.setObjectName("DebuggerGeneralPage")
        DebuggerGeneralPage.resize(643, 1367)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(DebuggerGeneralPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.headerLabel = QtWidgets.QLabel(DebuggerGeneralPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_6.addWidget(self.headerLabel)
        self.line11 = QtWidgets.QFrame(DebuggerGeneralPage)
        self.line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11.setObjectName("line11")
        self.verticalLayout_6.addWidget(self.line11)
        self.groupBox_3 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TextLabel1_2_3 = QtWidgets.QLabel(self.groupBox_3)
        self.TextLabel1_2_3.setObjectName("TextLabel1_2_3")
        self.gridLayout_2.addWidget(self.TextLabel1_2_3, 0, 0, 1, 3)
        self.allInterfacesButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.allInterfacesButton.setObjectName("allInterfacesButton")
        self.gridLayout_2.addWidget(self.allInterfacesButton, 1, 0, 1, 1)
        self.all6InterfacesButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.all6InterfacesButton.setObjectName("all6InterfacesButton")
        self.gridLayout_2.addWidget(self.all6InterfacesButton, 1, 1, 1, 1)
        self.selectedInterfaceButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.selectedInterfaceButton.setObjectName("selectedInterfaceButton")
        self.gridLayout_2.addWidget(self.selectedInterfaceButton, 1, 2, 1, 1)
        self.interfacesCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.interfacesCombo.setEnabled(False)
        self.interfacesCombo.setObjectName("interfacesCombo")
        self.gridLayout_2.addWidget(self.interfacesCombo, 2, 0, 1, 3)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 3, 1, 1, 1)
        self.deleteAllowedHostButton = QtWidgets.QPushButton(self.groupBox_4)
        self.deleteAllowedHostButton.setEnabled(False)
        self.deleteAllowedHostButton.setObjectName("deleteAllowedHostButton")
        self.gridlayout.addWidget(self.deleteAllowedHostButton, 2, 1, 1, 1)
        self.editAllowedHostButton = QtWidgets.QPushButton(self.groupBox_4)
        self.editAllowedHostButton.setEnabled(False)
        self.editAllowedHostButton.setObjectName("editAllowedHostButton")
        self.gridlayout.addWidget(self.editAllowedHostButton, 1, 1, 1, 1)
        self.addAllowedHostButton = QtWidgets.QPushButton(self.groupBox_4)
        self.addAllowedHostButton.setObjectName("addAllowedHostButton")
        self.gridlayout.addWidget(self.addAllowedHostButton, 0, 1, 1, 1)
        self.allowedHostsList = QtWidgets.QListWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allowedHostsList.sizePolicy().hasHeightForWidth())
        self.allowedHostsList.setSizePolicy(sizePolicy)
        self.allowedHostsList.setObjectName("allowedHostsList")
        self.gridlayout.addWidget(self.allowedHostsList, 0, 0, 4, 1)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.passiveDbgGroup = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.passiveDbgGroup.setObjectName("passiveDbgGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.passiveDbgGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.TextLabel1_2_2 = QtWidgets.QLabel(self.passiveDbgGroup)
        self.TextLabel1_2_2.setObjectName("TextLabel1_2_2")
        self.gridLayout.addWidget(self.TextLabel1_2_2, 0, 0, 1, 6)
        self.passiveDbgCheckBox = QtWidgets.QCheckBox(self.passiveDbgGroup)
        self.passiveDbgCheckBox.setObjectName("passiveDbgCheckBox")
        self.gridLayout.addWidget(self.passiveDbgCheckBox, 1, 0, 1, 6)
        self.passiveDbgPortLabel = QtWidgets.QLabel(self.passiveDbgGroup)
        self.passiveDbgPortLabel.setEnabled(False)
        self.passiveDbgPortLabel.setObjectName("passiveDbgPortLabel")
        self.gridLayout.addWidget(self.passiveDbgPortLabel, 2, 0, 1, 1)
        self.passiveDbgPortSpinBox = QtWidgets.QSpinBox(self.passiveDbgGroup)
        self.passiveDbgPortSpinBox.setEnabled(False)
        self.passiveDbgPortSpinBox.setMinimum(1024)
        self.passiveDbgPortSpinBox.setMaximum(65535)
        self.passiveDbgPortSpinBox.setProperty("value", 42424)
        self.passiveDbgPortSpinBox.setObjectName("passiveDbgPortSpinBox")
        self.gridLayout.addWidget(self.passiveDbgPortSpinBox, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.passiveDbgGroup)
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)
        self.passiveDbgBackendCombo = QtWidgets.QComboBox(self.passiveDbgGroup)
        self.passiveDbgBackendCombo.setEnabled(False)
        self.passiveDbgBackendCombo.setObjectName("passiveDbgBackendCombo")
        self.gridLayout.addWidget(self.passiveDbgBackendCombo, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 5, 1, 1)
        self.verticalLayout_6.addWidget(self.passiveDbgGroup)
        self.groupBox_2 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName("gridlayout1")
        self.execLabel = QtWidgets.QLabel(self.groupBox_2)
        self.execLabel.setEnabled(False)
        self.execLabel.setObjectName("execLabel")
        self.gridlayout1.addWidget(self.execLabel, 2, 0, 1, 1)
        self.execLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.execLineEdit.setEnabled(False)
        self.execLineEdit.setObjectName("execLineEdit")
        self.gridlayout1.addWidget(self.execLineEdit, 2, 1, 1, 1)
        self.hostLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.hostLineEdit.setEnabled(False)
        self.hostLineEdit.setObjectName("hostLineEdit")
        self.gridlayout1.addWidget(self.hostLineEdit, 1, 1, 1, 1)
        self.hostLabel = QtWidgets.QLabel(self.groupBox_2)
        self.hostLabel.setEnabled(False)
        self.hostLabel.setObjectName("hostLabel")
        self.gridlayout1.addWidget(self.hostLabel, 1, 0, 1, 1)
        self.remoteCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.remoteCheckBox.setObjectName("remoteCheckBox")
        self.gridlayout1.addWidget(self.remoteCheckBox, 0, 0, 1, 2)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.dbgPathTranslationGroup = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.dbgPathTranslationGroup.setObjectName("dbgPathTranslationGroup")
        self._2 = QtWidgets.QGridLayout(self.dbgPathTranslationGroup)
        self._2.setObjectName("_2")
        self.dbgPathTranslationCheckBox = QtWidgets.QCheckBox(self.dbgPathTranslationGroup)
        self.dbgPathTranslationCheckBox.setObjectName("dbgPathTranslationCheckBox")
        self._2.addWidget(self.dbgPathTranslationCheckBox, 0, 0, 1, 2)
        self.textLabel2_9 = QtWidgets.QLabel(self.dbgPathTranslationGroup)
        self.textLabel2_9.setEnabled(False)
        self.textLabel2_9.setObjectName("textLabel2_9")
        self._2.addWidget(self.textLabel2_9, 2, 0, 1, 1)
        self.dbgTranslationLocalEdit = QtWidgets.QLineEdit(self.dbgPathTranslationGroup)
        self.dbgTranslationLocalEdit.setEnabled(False)
        self.dbgTranslationLocalEdit.setObjectName("dbgTranslationLocalEdit")
        self._2.addWidget(self.dbgTranslationLocalEdit, 2, 1, 1, 1)
        self.dbgTranslationRemoteEdit = QtWidgets.QLineEdit(self.dbgPathTranslationGroup)
        self.dbgTranslationRemoteEdit.setEnabled(False)
        self.dbgTranslationRemoteEdit.setObjectName("dbgTranslationRemoteEdit")
        self._2.addWidget(self.dbgTranslationRemoteEdit, 1, 1, 1, 1)
        self.textLabel1_18 = QtWidgets.QLabel(self.dbgPathTranslationGroup)
        self.textLabel1_18.setEnabled(False)
        self.textLabel1_18.setObjectName("textLabel1_18")
        self._2.addWidget(self.textLabel1_18, 1, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.dbgPathTranslationGroup)
        self.groupBox_6 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_6.setObjectName("groupBox_6")
        self._4 = QtWidgets.QGridLayout(self.groupBox_6)
        self._4.setObjectName("_4")
        self.consoleDbgEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.consoleDbgEdit.setObjectName("consoleDbgEdit")
        self._4.addWidget(self.consoleDbgEdit, 1, 1, 1, 1)
        self.textLabel1_17 = QtWidgets.QLabel(self.groupBox_6)
        self.textLabel1_17.setObjectName("textLabel1_17")
        self._4.addWidget(self.textLabel1_17, 1, 0, 1, 1)
        self.consoleDbgCheckBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.consoleDbgCheckBox.setObjectName("consoleDbgCheckBox")
        self._4.addWidget(self.consoleDbgCheckBox, 0, 0, 1, 2)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_5 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_5.setObjectName("groupBox_5")
        self._3 = QtWidgets.QGridLayout(self.groupBox_5)
        self._3.setObjectName("_3")
        self.debugEnvironReplaceCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.debugEnvironReplaceCheckBox.setObjectName("debugEnvironReplaceCheckBox")
        self._3.addWidget(self.debugEnvironReplaceCheckBox, 0, 0, 1, 2)
        self.textLabel1_16 = QtWidgets.QLabel(self.groupBox_5)
        self.textLabel1_16.setObjectName("textLabel1_16")
        self._3.addWidget(self.textLabel1_16, 1, 0, 1, 1)
        self.debugEnvironEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.debugEnvironEdit.setObjectName("debugEnvironEdit")
        self._3.addWidget(self.debugEnvironEdit, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.groupBox = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.debugAutoSaveScriptsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.debugAutoSaveScriptsCheckBox.setObjectName("debugAutoSaveScriptsCheckBox")
        self.verticalLayout.addWidget(self.debugAutoSaveScriptsCheckBox)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_7 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.automaticResetCheckBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.automaticResetCheckBox.setObjectName("automaticResetCheckBox")
        self.verticalLayout_3.addWidget(self.automaticResetCheckBox)
        self.dontShowClientExitCheckBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.dontShowClientExitCheckBox.setObjectName("dontShowClientExitCheckBox")
        self.verticalLayout_3.addWidget(self.dontShowClientExitCheckBox)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.debugThreeStateBreakPoint = QtWidgets.QCheckBox(self.groupBox_8)
        self.debugThreeStateBreakPoint.setObjectName("debugThreeStateBreakPoint")
        self.verticalLayout_2.addWidget(self.debugThreeStateBreakPoint)
        self.verticalLayout_6.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.exceptionBreakCheckBox = QtWidgets.QCheckBox(self.groupBox_9)
        self.exceptionBreakCheckBox.setObjectName("exceptionBreakCheckBox")
        self.verticalLayout_4.addWidget(self.exceptionBreakCheckBox)
        self.verticalLayout_6.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(DebuggerGeneralPage)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.autoViewSourcecodeCheckBox = QtWidgets.QCheckBox(self.groupBox_10)
        self.autoViewSourcecodeCheckBox.setObjectName("autoViewSourcecodeCheckBox")
        self.verticalLayout_5.addWidget(self.autoViewSourcecodeCheckBox)
        self.verticalLayout_6.addWidget(self.groupBox_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.execLabel.setBuddy(self.execLineEdit)
        self.hostLabel.setBuddy(self.hostLineEdit)

        self.retranslateUi(DebuggerGeneralPage)
        self.passiveDbgCheckBox.toggled['bool'].connect(self.passiveDbgPortLabel.setEnabled)
        self.passiveDbgCheckBox.toggled['bool'].connect(self.passiveDbgPortSpinBox.setEnabled)
        self.remoteCheckBox.toggled['bool'].connect(self.execLineEdit.setEnabled)
        self.remoteCheckBox.toggled['bool'].connect(self.execLabel.setEnabled)
        self.remoteCheckBox.toggled['bool'].connect(self.hostLabel.setEnabled)
        self.remoteCheckBox.toggled['bool'].connect(self.hostLineEdit.setEnabled)
        self.selectedInterfaceButton.toggled['bool'].connect(self.interfacesCombo.setEnabled)
        self.passiveDbgCheckBox.toggled['bool'].connect(self.label.setEnabled)
        self.passiveDbgCheckBox.toggled['bool'].connect(self.passiveDbgBackendCombo.setEnabled)
        self.dbgPathTranslationCheckBox.toggled['bool'].connect(self.dbgTranslationRemoteEdit.setEnabled)
        self.dbgPathTranslationCheckBox.toggled['bool'].connect(self.textLabel1_18.setEnabled)
        self.dbgPathTranslationCheckBox.toggled['bool'].connect(self.textLabel2_9.setEnabled)
        self.dbgPathTranslationCheckBox.toggled['bool'].connect(self.dbgTranslationLocalEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DebuggerGeneralPage)
        DebuggerGeneralPage.setTabOrder(self.allInterfacesButton, self.all6InterfacesButton)
        DebuggerGeneralPage.setTabOrder(self.all6InterfacesButton, self.selectedInterfaceButton)
        DebuggerGeneralPage.setTabOrder(self.selectedInterfaceButton, self.interfacesCombo)
        DebuggerGeneralPage.setTabOrder(self.interfacesCombo, self.allowedHostsList)
        DebuggerGeneralPage.setTabOrder(self.allowedHostsList, self.addAllowedHostButton)
        DebuggerGeneralPage.setTabOrder(self.addAllowedHostButton, self.editAllowedHostButton)
        DebuggerGeneralPage.setTabOrder(self.editAllowedHostButton, self.deleteAllowedHostButton)
        DebuggerGeneralPage.setTabOrder(self.deleteAllowedHostButton, self.passiveDbgCheckBox)
        DebuggerGeneralPage.setTabOrder(self.passiveDbgCheckBox, self.passiveDbgPortSpinBox)
        DebuggerGeneralPage.setTabOrder(self.passiveDbgPortSpinBox, self.passiveDbgBackendCombo)
        DebuggerGeneralPage.setTabOrder(self.passiveDbgBackendCombo, self.remoteCheckBox)
        DebuggerGeneralPage.setTabOrder(self.remoteCheckBox, self.hostLineEdit)
        DebuggerGeneralPage.setTabOrder(self.hostLineEdit, self.execLineEdit)
        DebuggerGeneralPage.setTabOrder(self.execLineEdit, self.dbgPathTranslationCheckBox)
        DebuggerGeneralPage.setTabOrder(self.dbgPathTranslationCheckBox, self.dbgTranslationRemoteEdit)
        DebuggerGeneralPage.setTabOrder(self.dbgTranslationRemoteEdit, self.dbgTranslationLocalEdit)
        DebuggerGeneralPage.setTabOrder(self.dbgTranslationLocalEdit, self.consoleDbgCheckBox)
        DebuggerGeneralPage.setTabOrder(self.consoleDbgCheckBox, self.consoleDbgEdit)
        DebuggerGeneralPage.setTabOrder(self.consoleDbgEdit, self.debugEnvironReplaceCheckBox)
        DebuggerGeneralPage.setTabOrder(self.debugEnvironReplaceCheckBox, self.debugEnvironEdit)
        DebuggerGeneralPage.setTabOrder(self.debugEnvironEdit, self.debugAutoSaveScriptsCheckBox)
        DebuggerGeneralPage.setTabOrder(self.debugAutoSaveScriptsCheckBox, self.automaticResetCheckBox)
        DebuggerGeneralPage.setTabOrder(self.automaticResetCheckBox, self.dontShowClientExitCheckBox)
        DebuggerGeneralPage.setTabOrder(self.dontShowClientExitCheckBox, self.debugThreeStateBreakPoint)
        DebuggerGeneralPage.setTabOrder(self.debugThreeStateBreakPoint, self.exceptionBreakCheckBox)

    def retranslateUi(self, DebuggerGeneralPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("DebuggerGeneralPage", "<b>Configure general debugger settings</b>"))
        self.groupBox_3.setTitle(_translate("DebuggerGeneralPage", "Network Interface"))
        self.TextLabel1_2_3.setText(_translate("DebuggerGeneralPage", "<font color=\"#FF0000\"><b>Note:</b> These settings are activated at the next startup of the application.</font>"))
        self.allInterfacesButton.setToolTip(_translate("DebuggerGeneralPage", "Select to listen on all available network interfaces (IPv4 mode)"))
        self.allInterfacesButton.setText(_translate("DebuggerGeneralPage", "All network interfaces (IPv4)"))
        self.all6InterfacesButton.setToolTip(_translate("DebuggerGeneralPage", "Select to listen on all available network interfaces (IPv6 mode)"))
        self.all6InterfacesButton.setText(_translate("DebuggerGeneralPage", "All network interfaces (IPv6)"))
        self.selectedInterfaceButton.setToolTip(_translate("DebuggerGeneralPage", "Select to listen on the configured interface"))
        self.selectedInterfaceButton.setText(_translate("DebuggerGeneralPage", "Only selected interface"))
        self.interfacesCombo.setToolTip(_translate("DebuggerGeneralPage", "Select the network interface to listen on"))
        self.groupBox_4.setTitle(_translate("DebuggerGeneralPage", "Allowed hosts"))
        self.deleteAllowedHostButton.setText(_translate("DebuggerGeneralPage", "Delete"))
        self.editAllowedHostButton.setText(_translate("DebuggerGeneralPage", "Edit..."))
        self.addAllowedHostButton.setText(_translate("DebuggerGeneralPage", "Add..."))
        self.passiveDbgGroup.setTitle(_translate("DebuggerGeneralPage", "Passive Debugger"))
        self.TextLabel1_2_2.setText(_translate("DebuggerGeneralPage", "<font color=\"#FF0000\"><b>Note:</b> These settings are activated at the next startup of the application.</font>"))
        self.passiveDbgCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Enables the passive debug mode"))
        self.passiveDbgCheckBox.setWhatsThis(_translate("DebuggerGeneralPage", "<b>Passive Debugger Enabled</b>\n"
"<p>This enables the passive debugging mode. In this mode the debug client (the script) connects to the debug server (the IDE). The script is started outside the IDE. This way mod_python or Zope scripts can be debugged.</p>"))
        self.passiveDbgCheckBox.setText(_translate("DebuggerGeneralPage", "Passive Debugger Enabled"))
        self.passiveDbgPortLabel.setText(_translate("DebuggerGeneralPage", "Debug Server Port:"))
        self.passiveDbgPortSpinBox.setToolTip(_translate("DebuggerGeneralPage", "Enter the port the debugger should listen on"))
        self.passiveDbgPortSpinBox.setWhatsThis(_translate("DebuggerGeneralPage", "<b>Debug Server Port</b>\n"
"<p>Enter the port the debugger should listen on.</p>"))
        self.label.setText(_translate("DebuggerGeneralPage", "Debugger Type:"))
        self.passiveDbgBackendCombo.setToolTip(_translate("DebuggerGeneralPage", "Select the debugger type of the backend"))
        self.groupBox_2.setTitle(_translate("DebuggerGeneralPage", "Remote Debugger"))
        self.execLabel.setText(_translate("DebuggerGeneralPage", "Remote Execution:"))
        self.execLineEdit.setToolTip(_translate("DebuggerGeneralPage", "Enter the remote execution command."))
        self.execLineEdit.setWhatsThis(_translate("DebuggerGeneralPage", "<b>Remote Execution</b>\n"
"<p>Enter the remote execution command (e.g. ssh). This command is used to log into the remote host and execute the remote debugger.</p>"))
        self.hostLineEdit.setToolTip(_translate("DebuggerGeneralPage", "Enter the hostname of the remote machine."))
        self.hostLineEdit.setWhatsThis(_translate("DebuggerGeneralPage", "<b>Remote Host</b>\n"
"<p>Enter the hostname of the remote machine.</p>"))
        self.hostLabel.setText(_translate("DebuggerGeneralPage", "Remote Host:"))
        self.remoteCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Enable remote debugging"))
        self.remoteCheckBox.setWhatsThis(_translate("DebuggerGeneralPage", "This enables the remote debugger. Please enter the hostname of the remote machine and the command for the remote execution (e.g. ssh) below."))
        self.remoteCheckBox.setText(_translate("DebuggerGeneralPage", "Remote Debugging Enabled"))
        self.dbgPathTranslationGroup.setTitle(_translate("DebuggerGeneralPage", "Path Translation"))
        self.dbgPathTranslationCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Select to perform path translation"))
        self.dbgPathTranslationCheckBox.setText(_translate("DebuggerGeneralPage", "Perform Path Translation"))
        self.textLabel2_9.setText(_translate("DebuggerGeneralPage", "Local Path:"))
        self.dbgTranslationLocalEdit.setToolTip(_translate("DebuggerGeneralPage", "Enter the local path"))
        self.dbgTranslationRemoteEdit.setToolTip(_translate("DebuggerGeneralPage", "Enter the remote path"))
        self.textLabel1_18.setText(_translate("DebuggerGeneralPage", "Remote Path:"))
        self.groupBox_6.setTitle(_translate("DebuggerGeneralPage", "Console Debugger"))
        self.consoleDbgEdit.setToolTip(_translate("DebuggerGeneralPage", "Enter the console command (e.g. xterm -e)"))
        self.consoleDbgEdit.setWhatsThis(_translate("DebuggerGeneralPage", "<b>Console Command</b>\n"
"<p>Enter the console command (e.g. xterm -e). This command is used to open a command window for the debugger.</p>"))
        self.textLabel1_17.setText(_translate("DebuggerGeneralPage", "Console Command:"))
        self.consoleDbgCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Select to start the debugger in a console window (e.g. xterm)"))
        self.consoleDbgCheckBox.setText(_translate("DebuggerGeneralPage", "Start debugger in console window"))
        self.groupBox_5.setTitle(_translate("DebuggerGeneralPage", "Environment for Debug Client"))
        self.debugEnvironReplaceCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Select, if the environment should be replaced."))
        self.debugEnvironReplaceCheckBox.setWhatsThis(_translate("DebuggerGeneralPage", "<b>Replace Environment</b>\n"
"<p>If this entry is checked, the environment of the debugger will be replaced by the entries of the environment variables field. If it is unchecked, the environment will be ammended by these settings.</p>"))
        self.debugEnvironReplaceCheckBox.setText(_translate("DebuggerGeneralPage", "Replace Environment"))
        self.textLabel1_16.setText(_translate("DebuggerGeneralPage", "Environment:"))
        self.debugEnvironEdit.setToolTip(_translate("DebuggerGeneralPage", "Enter the environment variables to be set."))
        self.debugEnvironEdit.setWhatsThis(_translate("DebuggerGeneralPage", "<b>Environment</b>\n"
"<p>Enter the environment variables to be set for the debugger. The individual settings must be separate by whitespace and be given in the form \'var=value\'.</p>\n"
"<p>Example: var1=1 var2=\"hello world\"</p>"))
        self.groupBox.setTitle(_translate("DebuggerGeneralPage", "Start Debugging"))
        self.debugAutoSaveScriptsCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Select, whether changed scripts should be saved upon a debug, run, ... action."))
        self.debugAutoSaveScriptsCheckBox.setText(_translate("DebuggerGeneralPage", "Autosave changed scripts"))
        self.groupBox_7.setTitle(_translate("DebuggerGeneralPage", "Debug Client Exit"))
        self.automaticResetCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Select, whether a reset of the debug client should be performed after a client exit"))
        self.automaticResetCheckBox.setText(_translate("DebuggerGeneralPage", "Automatic Reset after Client Exit"))
        self.dontShowClientExitCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Select to suppress the client exit dialog for a clean exit"))
        self.dontShowClientExitCheckBox.setText(_translate("DebuggerGeneralPage", "Don\'t show client exit dialog for a clean exit"))
        self.groupBox_8.setTitle(_translate("DebuggerGeneralPage", "Breakpoints"))
        self.debugThreeStateBreakPoint.setToolTip(_translate("DebuggerGeneralPage", "Select to change the breakpoint toggle order from Off->On->Off to Off->On (permanent)->On (temporary)->Off"))
        self.debugThreeStateBreakPoint.setText(_translate("DebuggerGeneralPage", "Three state breakpoint"))
        self.groupBox_9.setTitle(_translate("DebuggerGeneralPage", "Exceptions"))
        self.exceptionBreakCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Select to always break at exceptions"))
        self.exceptionBreakCheckBox.setText(_translate("DebuggerGeneralPage", "Always break at exceptions"))
        self.groupBox_10.setTitle(_translate("DebuggerGeneralPage", "Local Variables Viewer"))
        self.autoViewSourcecodeCheckBox.setToolTip(_translate("DebuggerGeneralPage", "Automatically view source code when user changes the callstack frame in the callstack viewer."))
        self.autoViewSourcecodeCheckBox.setText(_translate("DebuggerGeneralPage", "Automatically view source code"))
