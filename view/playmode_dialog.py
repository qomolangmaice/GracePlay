#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: playmode_dialog.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.02.25 20:17:34

import sys
from PyQt4 import QtGui, QtCore

class PlayModeDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(PlayModeDialog, self).__init__(parent)

        grp_playmode = QtGui.QGroupBox()
        combo_playmode = QtGui.QComboBox()
        combo_playmode.addItem(u"自动播放")
        combo_playmode.addItem(u"单个循环")
        combo_playmode.addItem(u"列表循环")
        combo_playmode.addItem(u"随机播放")

        h_layout = QtGui.QVBoxLayout()
        h_layout.addWidget(combo_playmode)

        self.btn_ok = QtGui.QPushButton(u"确定")
        btn_layout = QtGui.QHBoxLayout()
        btn_layout.addStretch(1)
        btn_layout.addWidget(self.btn_ok)

        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(h_layout)
        main_layout.addLayout(btn_layout)

        self.setWindowTitle(u"播放模式")    
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    playmode_dialog = PlayModeDialog()
    sys.exit(playmode_dialog.exec_())
        
        

