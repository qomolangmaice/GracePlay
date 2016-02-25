#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: controlbar.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.17 13:35:24

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

from push_button import PushButton

class ControlBar(QtGui.QDockWidget):
    def __init__(self, parent=None):
        super(ControlBar, self).__init__(parent)

        self.btn_open  = QtGui.QPushButton()
        self.btn_open.setStyleSheet("""
                                    QPushButton{
                                        background-image:url(icons/open_file_normal.svg);
                                        width:16px; 
                                        height:16px; 
                                        padding-top:0px; 
                                        border:0px;}
                                       
                                    QPushButton:hover{
                                        background-image:url(icons/open_file_hover_press.svg);}
                                    """)

        self.btn_play  = QtGui.QPushButton()
        self.btn_play.setStyleSheet("""
                                    QPushButton{
                                        background-image:url(icons/play_normal_24px.png);
                                        width:24px; 
                                        height:24px; 
                                        padding-top:0px; 
                                        border:0px;}
                                       
                                    QPushButton:hover{
                                        background-image:url(icons/play_hover_press_24px.png);}
                                    """)

        self.btn_pause  = QtGui.QPushButton()
        self.btn_pause.setStyleSheet("""
                                    QPushButton{
                                        background-image:url(icons/pause_normal_24px.png);
                                        width:24px; 
                                        height:24px; 
                                        padding-top:0px; 
                                        border:0px;}
                                       
                                    QPushButton:hover{
                                        background-image:url(icons/pause_hover_press_24px.png);}
                                    """)

        self.btn_stop  = QtGui.QPushButton()
        self.btn_stop.setStyleSheet("""
                                    QPushButton{
                                        background-image:url(icons/stop_normal_20px.png);
                                        width:20px; 
                                        height:20px; 
                                        padding-top:0px; 
                                        border:0px;}
                                       
                                    QPushButton:hover{
                                        background-image:url(icons/stop_hover_press_20px.png);}
                                    """)

        self.btn_fullscreen  = QtGui.QPushButton()
        self.btn_fullscreen.setStyleSheet("""
                                    QPushButton{
                                        background-image:url(icons/fullscreen_normal.svg);
                                        width:16px; 
                                        height:16px; 
                                        padding-top:0px; 
                                        border:0px;}
                                       
                                    QPushButton:hover{
                                        background-image:url(icons/cancel_fullscreen_normal.svg);}
                                    """)

        self.btn_playlist = QtGui.QPushButton()
        self.btn_playlist.setStyleSheet("""
                                    QPushButton{
                                        background-image:url(icons/playlist_open_normal.svg);
                                        width:16px; 
                                        height:16px; 
                                        padding-top:0px; 
                                        border:0px;}
                                       
                                    QPushButton:hover{
                                        background-image:url(icons/playlist_open_hover_press.svg);}
                                    """)

        self.lab_time = QtGui.QLabel()   
        #self.lab_time.setText('00:00:00/00:00:00')
        self.lab_time.setText('')
        self.lab_time.setStyleSheet("color:white")   # set logo transparent
        self.lab_time.setFont(QtGui.QFont("Roman times", 11, QtGui.QFont.Normal))

        self.seekslider = Phonon.SeekSlider()
        self.volumeslider = Phonon.VolumeSlider()

        self.setWindowOpacity(0.5)  # Set Controlbar transparent 
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
        self.btn_playlist.setFocusPolicy(QtCore.Qt.NoFocus)
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
        hbox.addWidget(self.lab_time)
        hbox.addWidget(self.seekslider, 1)
        hbox.addWidget(self.volumeslider)
        hbox.addWidget(self.btn_fullscreen)
        hbox.addWidget(self.btn_playlist)
        self.setWidget(w_controlbar)
        self.setFixedHeight(45)

        self.translateLanguage()
        self.skin_name = QtCore.QString("skin/3-Blue-controlbar.png")
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

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    controlbar = ControlBar()
    controlbar.show()
    app.exec_()


