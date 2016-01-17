#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: controlbar.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.17 13:35:24

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

class ControlBar(QtGui.QDockWidget):
    def __init__(self, title='', parent=None):
        super(ControlBar, self).__init__(title, parent)

        #self.combo_open = QtGui.QComboBox()
        #self.combo_open.addItem("Open File")
        #self.combo_open.addItem("Open Directory")

        self.btn_open  = QtGui.QPushButton(QtGui.QIcon('icons/add.png'), '')
        self.btn_play  = QtGui.QPushButton(QtGui.QIcon('icons/play.png'), '')
        self.btn_pause = QtGui.QPushButton(QtGui.QIcon('icons/pause.png'), '')
        self.btn_stop  = QtGui.QPushButton(QtGui.QIcon('icons/stop.png'), '')
        self.btn_fullscreen  = QtGui.QPushButton(QtGui.QIcon('icons/fullscreen.png'), '')
        self.seekslider = Phonon.SeekSlider()
        self.volumeslider = Phonon.VolumeSlider()

        self.setWindowOpacity(0.8)  # Set Controlbar transparent 
        self.setTitleBarWidget(QtGui.QWidget(self))     # Hide title bar
        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.setWindowFlags(QtCore.Qt.Window | 
                            QtCore.Qt.X11BypassWindowManagerHint | 
                            QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.CustomizeWindowHint | 
                            QtCore.Qt.WindowStaysOnTopHint)
        self.setAllowedAreas(QtCore.Qt.TopDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)
        self.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        self.btn_open.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_play.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_pause.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_stop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_fullscreen.setFocusPolicy(QtCore.Qt.NoFocus)
        self.seekslider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.volumeslider.setFocusPolicy(QtCore.Qt.NoFocus)

        # ControlBar Layout management
        w_controlbar = QtGui.QWidget()
        hbox = QtGui.QHBoxLayout()
        w_controlbar.setLayout(hbox)
        #hbox.addWidget(self.combo_open)
        hbox.addWidget(self.btn_open)
        hbox.addWidget(self.btn_play)
        hbox.addWidget(self.btn_pause)
        hbox.addWidget(self.btn_stop)
        hbox.addWidget(self.btn_fullscreen)
        hbox.addWidget(self.seekslider, 1)
        hbox.addWidget(self.volumeslider)
        self.setWidget(w_controlbar)
        #self.setFixedHeight(60)

        self.translateLanguage()
        self.skin_name = QtCore.QString("skin/black.png")
        self.pixmap = QtGui.QPixmap()
        self.pixmap.load(self.skin_name)


    def move_to_bottom(self):
        rect = QtGui.QApplication.desktop().availableGeometry()
        self.move(rect.width()/2 - self.size().width()/2, 
                  rect.bottom() - self.height()) 

    def translateLanguage(self):
        self.btn_open.setToolTip(u"打开")
        self.btn_play.setToolTip(u"播放")
        self.btn_pause.setToolTip(u"暂停")
        self.btn_stop.setToolTip(u"停止")
        self.btn_fullscreen.setToolTip(u"全屏")

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)
        painter.end()


