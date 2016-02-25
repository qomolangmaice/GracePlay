#!/usr/b#in/env python
#-*- coding=utf-8 -*-
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
from playmode_dialog import PlayModeDialog

class MainMenu(QMenu):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__()
        self.createActions()
        #self.createMenus()
        self.translateActions()
        self.setting_dialog = SettingDialog(self)
        self.playmode_dialog = PlayModeDialog(self)

    def show_setting_dialog(self):
        self.setting_dialog.exec_()

    def show_help(self):
        pass

    def show_about_me(self):
        #QtGui.QMessageBox.about(self, "About Me", 
        #        "Copyright@2015 qomolangmaice") 
        QtGui.QMessageBox.about(self, "About Me",""" 
            <HTML>
            <p><b>This demo shows use of <c>QTableWidget</c> with custom handling for
             individual cells.</b></p>
            <p>Using a customized table item we make it possible to have dynamic
             output in different cells. The content that is implemented for this
             particular demo is:
            <ul>
            <li>Adding two cells.</li>
            <li>Subtracting one cell from another.</li>
            <li>Multiplying two cells.</li>
            <li>Dividing one cell with another.</li>
            <li>Summing the contents of an arbitrary number of cells.</li>
            </HTML>
        """)

    def show_about_qt(self):
        pass

    def show_play_mode(self):
        self.playmode_dialog.exec_() 

    def auto_play_mode(self):
        pass

    def repeat_single_mode(self):
        pass

    def repeat_all_mode(self):
        pass

    def shuffle_mode(self):
        pass

    def createActions(self):
        self.act_setting = QAction("Setting", self, statusTip="", triggered=self.show_setting_dialog)
        self.act_play_mode= QAction("PlayMode", self, statusTip="", triggered=self.show_play_mode)
        self.act_help = QAction(self)
        self.act_about_me= QAction("About me", self, statusTip="", triggered=self.show_about_me)
        self.act_about_qt = QAction("About Qt", self, statusTip="", triggered=self.show_about_qt)
        self.act_about_qt.triggered.connect(QtGui.qApp.aboutQt)

        self.act_setting.setIcon(QIcon(""))
        self.act_help.setIcon(QIcon(""))
        self.act_about_me.setIcon(QIcon(""))
        self.act_about_qt.setIcon(QIcon(""))

        # Add menu item
        self.addAction(self.act_setting)
        self.addAction(self.act_play_mode)
        self.addAction(self.act_help)
        self.addSeparator()
        self.addAction(self.act_about_me)
        self.addAction(self.act_about_qt)

    #def createMenus(self):
    #    self.play_mode = self.menubar_play_mode.addMenu("&PlayMode")
    #    self.play_mode.addAction(self.auto_play_mode)
    #    self.play_mode.addAction(self.repeat_single_mode)
    #    self.play_mode.addAction(self.repeat_all_mode)
    #    self.play_mode.addAction(self.shuffle_mode)

    def translateActions(self):
        self.act_setting.setText(u"设置")
        self.act_play_mode.setText(u"播放模式")
        self.act_help.setText(u"帮助")
        self.act_about_me.setText(u"关于我")
        self.act_about_qt.setText(u"关于Qt")
