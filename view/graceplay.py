#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: graceplay.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.05 20:58:09

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

class Video(Phonon.VideoWidget):

    doubleClicked = QtCore.pyqtSignal()
    keyPressed = QtCore.pyqtSignal(QtGui.QKeyEvent)
    mouseTrack = QtCore.pyqtSignal(QtGui.QMouseEvent)

    def __init__(self, parent=None):
        Phonon.VideoWidget.__init__(self, parent)
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def focusOutEvent(self, event):
        self.setFocus()

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()

    def mouseMoveEvent(self, event):
        self.mouseTrack.emit(event)

    def keyPresseEvent(self, event):
        self.keyPressed.emit(event)

class ControlBar(QtGui.QDockWidget):
    def __init__(self, title='', parent=None):
        super(ControlBar, self).__init__(title, parent)

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
        hbox.addWidget(self.btn_open)
        hbox.addWidget(self.btn_play)
        hbox.addWidget(self.btn_pause)
        hbox.addWidget(self.btn_stop)
        hbox.addWidget(self.btn_fullscreen)
        hbox.addWidget(self.seekslider, 1)
        hbox.addWidget(self.volumeslider)
        self.setWidget(w_controlbar)
        self.setFixedHeight(50)

    def move_to_bottom(self):
        rect = QtGui.QApplication.desktop().availableGeometry()
        self.move(rect.width()/2 - self.size().width()/2, 
                  rect.bottom() - self.height()) 

class GracePlay(QtGui.QMainWindow):
    ''' The main window of the GracePlay.'''
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.init_media()
        self.init_ui()

        self.setWindowTitle(_('GracePlay'))
        self.setWindowOpacity(0.95)
        # set Frameless window
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.show()

    def init_media(self):
        self.media = Phonon.MediaObject(self)
        self.video = Video(self)
        self.audio = Phonon.AudioOutput(self)

    def init_ui(self):
        self.setCentralWidget(self.video)
        self.video.setMinimumSize(650, 350)

        self.controlbar = ControlBar(_('ControlBar'))
        self.btn_open  = self.controlbar.btn_open
        self.btn_play  = self.controlbar.btn_play
        self.btn_pause = self.controlbar.btn_pause
        self.btn_stop = self.controlbar.btn_stop
        self.btn_fullscreen = self.controlbar.btn_fullscreen
        self.seekslider = self.controlbar.seekslider
        self.volumeslider = self.controlbar.volumeslider
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.controlbar)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

