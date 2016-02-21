# -*- coding: utf-8 -*-
# Author: tiensbakung
# Date: 2013-03-29
'''The playlist GUI.
'''

from PyQt4 import QtGui, QtCore


class PlayList(QtGui.QDockWidget):
    '''The GUI part of the playlist.
    '''
#    def __init__(self, title='', parent=None):
#        super(PlayList, self).__init__(title, parent)
 
    def __init__(self, parent=None):
        super(PlayList, self).__init__()
        self.init_ui()
        self.init_contextmenu()
        #self.setWindowOpacity(1)

    def init_ui(self):
        self.listview = QtGui.QListView()
        self.setWidget(self.listview)

        #self.btn_play_mode = QtGui.QPushButton()
        #self.btn_add_files = QtGui.QPushButton()
        #self.btn_add_directory = QtGui.QPushButton()
        #self.btn_delete_file = QtGui.QPushButton()
        #self.btn_clear_files = QtGui.QPushButton()

        #self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        #self.setWindowFlags(QtCore.Qt.Window | 
        #                    QtCore.Qt.X11BypassWindowManagerHint | 
        #                    QtCore.Qt.FramelessWindowHint |
        #                    QtCore.Qt.CustomizeWindowHint | 
        #                    QtCore.Qt.WindowStaysOnTopHint)
        #self.setAllowedAreas(QtCore.Qt.TopDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)
        #self.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        #self.setFocusPolicy(QtCore.Qt.NoFocus)


        #h_list = QtGui.QVBoxLayout()
        #h_list.addWidget(self.listview)

        #v_list = QtGui.QHBoxLayout()
        #v_list.addWidget(self.btn_play_mode)
        #v_list.addWidget(self.btn_add_files)
        #v_list.addWidget(self.btn_add_directory)
        #v_list.addWidget(self.btn_delete_file)
        #v_list.addWidget(self.btn_clear_files)

        #w_playlist = QtGui.QWidget()
        #playlist = QtGui.QGridLayout()
        #w_playlist.setLayout(playlist) 

        #playlist.addLayout(h_list, 0, 0)
        #playlist.setSpacing(0)
        #playlist.addLayout(v_list, 1, 0)

        #self.setWidget(w_playlist)
        #self.setContentsMargins(0, 0, 0, 0)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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
