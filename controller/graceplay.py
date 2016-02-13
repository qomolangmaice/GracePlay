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
        self.main_menu = self.view.main_menu
        self.setting_dialog = self.view.setting_dialog
        self.title_widget = self.view.title_widget
        self.video = self.view.video
        self.controlbar = self.view.controlbar
        self.playlist = self.view.playlist
        self.playlist.listview.setModel(self.model) 

        self.init_media()

        self.view.btn_mainmenu.clicked.connect(self.handle_mainmenu)
        self.view.btn_min.clicked.connect(self.handle_min)
        self.view.btn_max.clicked.connect(self.handle_max)
        self.view.btn_close.clicked.connect(self.handle_close)

        self.video.doubleClicked.connect(self.toggle_fullscreen)
        self.video.mouseTrack.connect(self.animate_controlbar)
        self.video.keyPressed.connect(self.key_handler)
 
        self.view.btn_open.clicked.connect(self.handle_btn_open)
        self.view.btn_play.clicked.connect(self.handle_btn_play)
        self.view.btn_pause.clicked.connect(self.handle_btn_pause)
        self.view.btn_stop.clicked.connect(self.handle_btn_stop)
        self.view.btn_fullscreen.clicked.connect(self.handle_btn_fullscreen)
       
        #self.playlist.listview.doubleClicked.connect(self.play_file)

    def handle_close(self):
        self.view.close()

    def handle_mainmenu(self):
        p = self.view.rect().topRight()
        p.setX(p.x() - 150)
        p.setY(p.y() + 22)
        self.view.main_menu.exec_(self.view.mapToGlobal(p))

    def handle_min(self):
        self.view.showMinimized()

    def handle_max(self):
        if not self.view.isMaximized():
            self.view.showMaximized()
        else:
            self.view.showNormal()

    def animate_controlbar(self, e):
        if self.video.isFullScreen():
            if self.view.height() - e.y() < 60:
                self.controlbar.show() 
            else:
                self.controlbar.hide()

    def key_handler(self, e):
        i = 0.8 
        if e.key() == QtCore.Qt.Key_Left:
            self.media.seek(self.media.currentTime() - 10000)
        elif e.key() == QtCore.Qt.Key_Right:
            self.media.seek(self.media.currentTime() + 10000)
        elif e.key() == QtCore.Qt.Key_Down: 
            self.audio.setVolume(i - 0.2)
        elif e.key() == QtCore.Qt.Key_Up:
            self.audio.setVolume(i + 0.2)
        elif e.key() == QtCore.Qt.Key_F:
            self.toggle_fullscreen()
        elif e.key() == QtCore.Qt.Key_Space:
            self.toggle_play()

    def init_media(self):
        self.path_to_audio = Phonon.createPath(self.media, self.audio)
        self.path_to_video = Phonon.createPath(self.media, self.video)

        self.view.seekslider.setMediaObject(self.media)
        self.view.volumeslider.setAudioOutput(self.audio)

    def clear_files(self):
        self.model.clear()

    def handle_btn_open(self):
        file_dialog = QtGui.QFileDialog(self.view, _('Choose a File'), 
                                      os.path.expanduser('~'),
                                      _('Multimedia File (*.*)'))
        if file_dialog.exec_():
            self.clear_files()
            files = file_dialog.selectedFiles()
            file_name = files[0]
            self.model.append(file_name)
            self.playlist.listview.setCurrentIndex(self.model.index(0))
            self.view.title_widget.lab_movie_name.setText(file_name)
            self.media.setCurrentSource(Phonon.MediaSource(file_name))
            self.media.play()

        ''' Another version - open file ''' 
        #file_path = QtGui.QFileDialog.getOpenFileName(self.view, self.view.btn_open.text())
        #if file_path:
        #    self.view.title_widget.lab_movie_name.setText(file_path)
        #    self.media.setCurrentSource(Phonon.MediaSource(file_path))
        #    self.media.play()

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
            self.media.pause()
        else:
            self.media.play()

