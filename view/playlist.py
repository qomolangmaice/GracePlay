#!/usr/bin/env python
#-*- coding=utf-8 -*-
# File Name: graceplay.py
# Description: Play list GUI 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.05 20:58:09

from PyQt4 import QtGui, QtCore

class PlayList(QtGui.QDockWidget):
    def __init__(self, parent=None):
        super(PlayList, self).__init__()
        self.init_ui()
        self.init_contextmenu()

    def init_ui(self):
        self.listview = QtGui.QListView()
        self.setWidget(self.listview)

        # Hide title bar
        self.setTitleBarWidget(QtGui.QWidget(self))
        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.listview.setFocusPolicy(QtCore.Qt.NoFocus)

    def init_contextmenu(self):
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.action_add_files = QtGui.QAction(_('Add file(s)'), self)
        self.action_add_directory = QtGui.QAction(_('Add directory'), self)
        self.action_add_url = QtGui.QAction(_('Add URL'), self)
        self.action_delete_file = QtGui.QAction(_('Delete'), self)
        self.action_clear_files = QtGui.QAction(_('Clear'), self)
        self.addAction(self.action_add_files)
        self.addAction(self.action_add_directory)
        self.addAction(self.action_add_url)
        self.addAction(self.action_delete_file)
        self.addAction(self.action_clear_files)
