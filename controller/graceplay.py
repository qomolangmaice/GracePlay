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

        # Auto play model by default
        self.play_mode = 'ap'

        self.init_media()

        self.view.btn_mainmenu.clicked.connect(self.handle_mainmenu)
        self.view.btn_min.clicked.connect(self.handle_min)
        self.view.btn_max.clicked.connect(self.handle_max)
        self.view.btn_close.clicked.connect(self.handle_close)

        #self.view.action_play_mode.triggered.connect(self.set_play_mode)

        self.video.doubleClicked.connect(self.toggle_fullscreen)
        self.video.mouseTrack.connect(self.animate_controlbar)
        self.video.keyPressed.connect(self.key_handler)
        
        self.media.tick.connect(self.show_time_info)
        self.media.aboutToFinish.connect(self.prepare_next)
        self.media.currentSourceChanged.connect(self.new_file)
        self.media.finished.connect(self.finish)
 
        self.view.btn_open.clicked.connect(self.handle_btn_open)
        self.view.btn_play.clicked.connect(self.handle_btn_play)
        self.view.btn_pause.clicked.connect(self.handle_btn_pause)
        self.view.btn_stop.clicked.connect(self.handle_btn_stop)
        self.view.btn_fullscreen.clicked.connect(self.handle_btn_fullscreen)
        self.view.btn_playlist.clicked.connect(self.handle_btn_playlist)
       
        self.playlist.listview.doubleClicked.connect(self.handle_play_file)

        self.playlist.action_add_files.triggered.connect(self.handle_add_files)
        self.playlist.action_add_directory.triggered.connect(self.handle_add_directory)
        self.playlist.action_add_url.triggered.connect(self.handle_add_url)
        self.playlist.action_delete_file.triggered.connect(self.handle_delete_file)
        self.playlist.action_clear_files.triggered.connect(self.handle_clear_files)

    def set_play_mode(self):
        self.play_mode = str(action.data().toString())

    def show_time_info(self):
        #state = [_('Loading'),
        #         _('Stopped'),
        #         _('Playing'),
        #         _('Buffering'),
        #         _('Paused'),
        #         _('Error')][self.media.state()]
        cur_time   = str(timedelta(seconds = self.media.currentTime() / 1000))
        total_time = str(timedelta(seconds = self.media.totalTime() / 1000))
        time = cur_time + '/' + total_time
        self.view.lab_time.setText(time)

    def prepare_next(self):
        row = self.playlist.listview.currentIndex().row() 
        print 'cur: %d, total: %d' % (row, self.model.rowCount())
        source = Phonon.MediaSource('')
        
        if self.model.rowCount() == 0:
            return 
        elif self.play_mode == 'ap' and (row + 1 < self.model.rowCount()): # autp play mode
            row += 1
            source = Phonon.MediaSource(self.model[row])
        elif self.play_mode == 'rs':  # repeat single play model
            source = Phonon.MediaSource(self.model[row])
        elif self.play_mode == 'ra':  # repeat all play model
            row = (row + 1) % self.model.rowCount()
            source = Phonon.MediaSource(self.model[row])
        elif self.play_mode == 'shuffle':
            row = random.randRange(0, self.model.rowCount())
            source = Phonon.MediaSource(self.model[row])

        self.media.enqueue(source)
        self.playlist.listview.setCurrentIndex(self.model.index(row))

    def new_file(self):
        pass

    def finish(self):
        pass
                
    def handle_add_files(self):
        file_dialog = QtGui.QFileDialog(self.view, _('Choose File(s)'),
                                        os.path.expanduser('~'),
                                        ('Multimedia File (*.avi *.wmv *.mp4 *.rmvb *.mkv *mp3)'))
        if file_dialog.exec_():
            files = file_dialog.selectedFiles()
            self.model.extend(files)

    def handle_add_directory(self):
        file_dialog = QtGui.QFileDialog(self.view, _('Choose a directory'))
        file_dialog.setFileMode(QtGui.QFileDialog.Directory)
        if file_dialog.exec_():
            directory = file_dialog.selectedFiles()[0]
            qdir = QtCore.QDir(directory)
            for f in qdir.entryInfoList(['*.avi','*.wmv', '*.mp4', '*.rmvb','*.mkv', '*.mp3'], QtCore.QDir.Files):
                self.model.append(f.absoluteFilePath())

    def handle_add_url(self):
        pass

    def handle_delete_file(self):
       index = self.playlist.listview.currentIndex() 
       self.model.pop(index.row())
       #self.media.stop()

    def handle_clear_files(self):
       self.model.clear() 
       self.media.stop()
       self.view.lab_time.setText('')
       self.view.title_widget.lab_movie_name.setText('')

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

    def handle_close(self):
        self.view.close()

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

    def handle_btn_open(self):
        file_dialog = QtGui.QFileDialog(self.view, _('Choose a File'), 
                                      os.path.expanduser('~'),
                                      _('Multimedia File (*.*)'))

        if file_dialog.exec_():
            self.handle_clear_files()
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

    def handle_play_file(self, index):
        f = self.model[index.row()]
        self.media.setCurrentSource(Phonon.MediaSource(f))
        self.view.title_widget.lab_movie_name.setText(f)
        self.media.play()

    def handle_btn_stop(self):
        self.view.btn_play.setEnabled(True)
        self.media.stop()
        self.view.lab_time.setText('')
        self.view.title_widget.lab_movie_name.setText('')

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

    def handle_btn_playlist(self):
        if self.view.playlist.isVisible():
            self.view.playlist.hide()
        else:
            self.view.playlist.show()

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
            #self.view.btn_play.setIcon(QtGui.QIcon('icons/stop_normal_24px.png'))
        else:
            self.media.play()

