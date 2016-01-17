#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: graceplay.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.05 20:58:09

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

from title_widget import TitleWidget 
from playlist import PlayList
from controlbar import ControlBar
from video import Video

#class GracePlay(QtGui.QMainWindow):
class GracePlay(QtGui.QWidget):
    ''' The main window of the GracePlay.'''
    def __init__(self, parent=None):
        #QtGui.QMainWindow.__init__(self, parent)
        QtGui.QWidget.__init__(self, parent)

        self.init_media()
        self.init_ui()

        self.setWindowIcon(QtGui.QIcon("icons/video.png"))

        # Set transparent window
        self.setWindowOpacity(0.95)
        self.setMinimumSize(700, 450)

        # set Frameless window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set background color
        #widget_style = ''' 
        #    QWidget{
        #        border-radius: 4px;
        #        background-image: url('skin/17_big.png');
        #    }
        #    VideoWidget{
        #        background-color: #000000;
        #    } 
        #'''
        #self.setStyleSheet(widget_style)
        self.show()

    def init_media(self):
        self.media = Phonon.MediaObject(self)
        self.video = Video(self)
        self.audio = Phonon.AudioOutput(self)

    def init_ui(self):
        self.title_widget = TitleWidget(self)
        self.btn_mainmenu = self.title_widget.btn_mainmenu
        self.btn_min = self.title_widget.btn_min
        self.btn_max = self.title_widget.btn_max
        self.btn_close = self.title_widget.btn_close

        self.controlbar = ControlBar(_('ControlBar'))
        self.controlbar.setFixedHeight(55)
        self.btn_open  = self.controlbar.btn_open
        self.btn_play  = self.controlbar.btn_play
        self.btn_pause = self.controlbar.btn_pause
        self.btn_stop = self.controlbar.btn_stop
        self.btn_fullscreen = self.controlbar.btn_fullscreen
        self.seekslider = self.controlbar.seekslider
        self.volumeslider = self.controlbar.volumeslider

        self.playlist = PlayList(_('PlayList'))

        main_layout = QtGui.QVBoxLayout()
        main_layout.addWidget(self.title_widget)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.video)
        #self.setCentralWidget(self.video)
        #self.video.setMinimumSize(700, 350)

        main_layout.setSpacing(0)
        main_layout.addWidget(self.controlbar)

        #main_layout.addWidget(self.playlist)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(main_layout)
        #self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.controlbar)

        #self.playlist = PlayList(_('PlayList'))
        #self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.playlist)
    
    # Set the drag property of the window -- For press event 
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    # Set the drag property of the window move -- For drag move event 
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

