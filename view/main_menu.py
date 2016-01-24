#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: main_menu.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.24 16:29:14

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

class MainMenu(QMenu):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__()
        self.createActions()
        self.translateActions()

    def createActions(self):
        # Create menu item list
        self.action_setting = QAction(self)
        self.action_help = QAction(self)
        self.action_documetation = QAction(self)
        self.action_about_us = QAction(self)
        self.action_about_qt = QAction(self)

        self.action_setting.setIcon(QIcon(""))
        self.action_help.setIcon(QIcon(""))
        self.action_documetation.setIcon(QIcon(""))
        self.action_about_us.setIcon(QIcon(""))
        self.action_about_qt.setIcon(QIcon(""))

        # Add menu item
        self.addAction(self.action_setting)
        self.addAction(self.action_help)
        self.addAction(self.action_documetation)
        self.addSeparator()
        self.addAction(self.action_about_us)
        self.addAction(self.action_about_qt)

        # Set signal link
        #self.connect(self.action_setting, SIGNAL("triggered()"), SIGNAL("showSettingDialog()"))
        #self.connect(self.action_help, SIGNAL("triggered()"), SIGNAL("showHelpDialog()"))
        #self.connect(self.action_documetation, SIGNAL("triggered()"), SIGNAL("showDocDialog()"))
        #self.connect(self.action_about_us, SIGNAL("triggered()"), SIGNAL("showAboutUs()"))
        #self.connect(self.action_about_qt, SIGNAL("triggered()"), SIGNAL("showAboutQt()"))

    def translateActions(self):
        self.action_setting.setText(u"Setting")
        self.action_help.setText(u"Help")
        self.action_documetation.setText(u"Documentation")
        self.action_about_us.setText(u"About us")
        self.action_about_qt.setText(u"About Qt")
