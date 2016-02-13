#!/usr/b#in/env python
#-*- coding: UTF-8 -*-

# File Name: main_menu.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.24 16:29:14

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

from setting_dialog import SettingDialog

class MainMenu(QMenu):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__()
        self.createActions()
        self.translateActions()
        self.setting_dialog = SettingDialog(self)

    def show_setting_dialog(self):
        self.setting_dialog.exec_()

    def show_help(self):
        pass

    def show_documetation(self):
        pass

    def show_about_me(self):
        QtGui.QMessageBox.about(self, "About Me", 
                "Copyright@2015 qomolangmaice") 

    def show_about_qt(self):
        pass

    def createActions(self):
        # Create menu item list
        self.action_setting = QAction("Setting..", self, statusTip="", triggered=self.show_setting_dialog)

        self.action_help = QAction(self)
        self.action_documetation = QAction(self)

        self.action_about_me= QAction("Setting..", self, statusTip="", triggered=self.show_about_me)

        self.action_about_qt = QAction("Setting..", self, statusTip="", triggered=self.show_about_qt)
        self.action_about_qt.triggered.connect(QtGui.qApp.aboutQt)

        self.action_setting.setIcon(QIcon(""))
        self.action_help.setIcon(QIcon(""))
        self.action_documetation.setIcon(QIcon(""))
        self.action_about_me.setIcon(QIcon(""))
        self.action_about_qt.setIcon(QIcon(""))

        # Add menu item
        self.addAction(self.action_setting)
        self.addAction(self.action_help)
        self.addAction(self.action_documetation)
        self.addSeparator()
        self.addAction(self.action_about_me)
        self.addAction(self.action_about_qt)

    def translateActions(self):
        self.action_setting.setText(u"Setting")
        self.action_help.setText(u"Help")
        self.action_documetation.setText(u"Documentation")
        self.action_about_me.setText(u"About Me")
        self.action_about_qt.setText(u"About Qt")
