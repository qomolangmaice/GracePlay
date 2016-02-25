#!/usr/bin/env python
#-*- coding=utf-8 -*-
# File Name: video.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.17 13:30:09

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

from title_widget import TitleWidget 
from playlist import PlayList

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

    def keyPressEvent(self, event):
        self.keyPressed.emit(event)


