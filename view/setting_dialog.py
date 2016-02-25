#!/usr/bin/env python
#-*- coding=utf-8 -*-
# File Name: setting_dialog.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.31 13:07:24

import sys
from PyQt4 import QtGui,QtCore


class ConfigurationPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ConfigurationPage, self).__init__(parent)

        configGroup = QtGui.QGroupBox("Server Configuration")

        serverLabel = QtGui.QLabel("Server: ")
        serverCombo = QtGui.QComboBox()
        serverCombo.addItem("Trolltech (Australia)")
        serverCombo.addItem("Trolltech (Germany)")
        serverCombo.addItem("Trolltech (Norway)")
        serverCombo.addItem("Trolltech (People's republic of China)")
        serverCombo.addItem("Trolltech (USA)")

        serverLayout = QtGui.QHBoxLayout()
        serverLayout.addWidget(serverLabel)
        serverLayout.addWidget(serverCombo)

        configLayout = QtGui.QVBoxLayout()
        configLayout.addLayout(serverLayout)
        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

class UpdatePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UpdatePage, self).__init__(parent)

        updateGroup = QtGui.QGroupBox("Package selection")
        systemCheckBox = QtGui.QCheckBox("Update system")
        appsCheckBox = QtGui.QCheckBox("Update applications")
        docsCheckBox = QtGui.QCheckBox("Update documentation")

        packageGroup = QtGui.QGroupBox("Existing packages")

        packageList = QtGui.QListWidget()
        qtItem = QtGui.QListWidgetItem(packageList)
        qtItem.setText("Qt")
        qsaItem = QtGui.QListWidgetItem(packageList)
        qsaItem.setText("QSA")
        teamBuiderItem = QtGui.QListWidgetItem(packageList)
        teamBuiderItem.setText("Teambuilder")

        startUpdateButton = QtGui.QPushButton("Start Update")

        updateLayout = QtGui.QVBoxLayout()
        updateLayout.addWidget(systemCheckBox)
        updateLayout.addWidget(appsCheckBox)
        updateLayout.addWidget(docsCheckBox)
        updateGroup.setLayout(updateLayout)

        packageLayout = QtGui.QVBoxLayout()
        packageLayout.addWidget(packageList)
        packageGroup.setLayout(packageLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(updateGroup)
        mainLayout.addWidget(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startUpdateButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

class QueryPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QueryPage, self).__init__(parent)

        packageGroup = QtGui.QGroupBox("Look fo packages")

        nameLabel = QtGui.QLabel("Name: ")
        nameEdit = QtGui.QLineEdit()

        dataLabel = QtGui.QLabel("Released after: ")
        dateEdit = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        releasesCheckBox = QtGui.QCheckBox("Releases")
        upgradesCheckBox = QtGui.QCheckBox("Upgrades")

        hitsSpinBox = QtGui.QSpinBox()
        hitsSpinBox.setPrefix("Return up to ")
        hitsSpinBox.setSuffix(" results")
        hitsSpinBox.setSpecialValueText("Return only the first result")
        hitsSpinBox.setMinimum(1)
        hitsSpinBox.setMaximum(100)
        hitsSpinBox.setSingleStep(10)

        startQueryButton = QtGui.QPushButton("Start query")
        
        packageLayout = QtGui.QGridLayout()
        packageLayout.addWidget(nameLabel, 0, 0)
        packageLayout.addWidget(nameEdit, 0, 1)
        packageLayout.addWidget(dataLabel, 1, 0)
        packageLayout.addWidget(dateEdit, 1, 1)
        packageLayout.addWidget(releasesCheckBox, 2, 0)
        packageLayout.addWidget(upgradesCheckBox, 3, 0)
        packageLayout.addWidget(hitsSpinBox, 4, 0, 1, 2)
        packageGroup.setLayout(packageLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)
        
        self.setLayout(mainLayout)

class SettingDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(96, 84))
        self.contentsWidget.setMovement(QtGui.QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)
        
        self.pagesWidget = QtGui.QStackedWidget()
        self.pagesWidget.addWidget(ConfigurationPage())
        self.pagesWidget.addWidget(UpdatePage())
        self.pagesWidget.addWidget(QueryPage())

        closeButton = QtGui.QPushButton("close")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.clicked.connect(self.close)

        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(closeButton)
    
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

        self.setWindowTitle("Setting Dialog")

    def chage_page(self, current, previous):
        if not current:
            current = previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    def createIcons(self):
        configButton = QtGui.QListWidgetItem(self.contentsWidget)
        configButton.setIcon(QtGui.QIcon('icons/video.png'))
        configButton.setText(" Config ")
        configButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        configButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        updateButton = QtGui.QListWidgetItem(self.contentsWidget)
        updateButton.setIcon(QtGui.QIcon('icons/video.png'))
        updateButton.setText("Update")
        updateButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        updateButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        queryButton = QtGui.QListWidgetItem(self.contentsWidget)
        queryButton.setIcon(QtGui.QIcon('icons/video.png'))
        queryButton.setText(" Query ")
        queryButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        queryButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.chage_page)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    setting_dialog = SettingDialog()
    sys.exit(setting_dialog.exec_())




