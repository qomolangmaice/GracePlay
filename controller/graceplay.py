#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: graceplay.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.05 21:35:27

import os
import random
from datetime import timedelta

from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon

import view
import model

class GracePlayController:
    def __init__(self, model, view): 
        self.model = model
        self.view = view
        self.audio = self.view.audio
        self.media = self.view.media
        self.video = self.view.video
        self.playlist = self.view.playlist
        self.controlbar = self.view.controlbar
        self.playlist.listview.setModel(self.model) 

        self.init_media()

        # Handle button clicked signals
        self.view.btn_open.clicked.connect(self.handle_btn_open)
        self.view.btn_play.clicked.connect(self.handle_btn_play)
        self.view.btn_pause.clicked.connect(self.handle_btn_pause)
        self.view.btn_stop.clicked.connect(self.handle_btn_stop)
        self.view.btn_fullscreen.clicked.connect(self.handle_btn_fullscreen)

        self.video.doubleClicked.connect(self.toggle_fullscreen)
        self.video.mouseTrack.connect(self.animate_controlbar)
        #self.video.keyPressed.connect(self.key_handler)
        
        #self.playlist.listview.doubleClicked.connect(self.play_file)

    def animate_controlbar(self, e):
        if self.video.isFullScreen():
            if self.view.height() - e.y() < 60:
                self.controlbar.show() 
            else:
                self.controlbar.hide()

    #def key_handler(self, e):
    #    if e.key() == QtCore.Qt.Key_Left:
    #        self.media.seek(self.media.currentTime() - 10000)
    #    elif e.key() == QtCore.Qt.Key_Right:
    #        self.media.seek(self.media.currentTime() + 10000)
    #    elif e.key() == QtCore.Qt.Key_Down:
    #        self.media.seek(self.media.currentTime() - 60000)
    #    elif e.key() == QtCore.Qt.Key_Up:
    #        self.media.seek(self.media.currentTime() + 60000)
    #    elif e.key() == QtCore.Qt.Key_F:
    #        self.toggle_fullscreen()
    #    elif e.key() == QtCore.Qt.Key_Space:
    #        self.toggle_play()
        #elif e.key() == QtCore.Qt.Key_Esc:
        #    self.toggle_fullscreen()

    def init_media(self):
        self.path_to_audio = Phonon.createPath(self.media, self.audio)
        self.path_to_video = Phonon.createPath(self.media, self.video)

        self.view.seekslider.setMediaObject(self.media)
        self.view.volumeslider.setAudioOutput(self.audio)

    def clear_files(self):
        self.model.clear()

    def handle_btn_open(self):
        #file_path = QtGui.QFileDialog.getOpenFileName(self.view, self.view.btn_open.text())
        file_dialog = QtGui.QFileDialog(self.view, _('Choose a File'), 
                                      os.path.expanduser('~'),
                                      _('Multimedia File (*.avi *.wmv *.mkv *.rmvb *.mp3 *.mp4)'))
        #if file_path:
        if file_dialog.exec_():
            self.clear_files()
            files = file_dialog.selectedFiles()
            file_name = files[0]
            self.model.append(file_name)
            self.playlist.listview.setCurrentIndex(self.model.index(0))
            #self.media.setCurrentSource(Phonon.MediaSource(file_path))
            self.media.setCurrentSource(Phonon.MediaSource(file_name))
            self.media.play()

    def handle_btn_pause(self):
        self.view.btn_play.setEnabled(True)
        self.media.pause()

    def handle_btn_play(self):
        self.view.btn_play.setEnabled(False)
        self.media.setTickInterval(400)
        self.media.play()

    def handle_btn_stop(self):
        self.view.btn_play.setEnabled(True)
        self.media.stop()

    def handle_btn_fullscreen(self):
        if self.video.isFullScreen():
            self.video.setFullScreen(False)
            self.controlbar.setFloating(False)
            self.controlbar.show()
            self.view.show()
        else:
            self.video.setFullScreen(True)
            self.view.hide()
            self.controlbar.setFloating(True)
            self.controlbar.move_to_bottom()

    def toggle_fullscreen(self):
        if self.video.isFullScreen():
            self.video.setFullScreen(False)
            self.controlbar.setFloating(False)
            self.controlbar.show()
            self.view.show()
        else:
            self.video.setFullScreen(True)
            self.view.hide()
            self.controlbar.setFloating(True)
            self.controlbar.move_to_bottom()

    def toggle_play(self):
        if self.media.state() == Phonon.PlayingState:
            self.pause()
        else:
            self.play()


