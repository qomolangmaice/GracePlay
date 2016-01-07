#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: title_widget.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.07 21:31:25

#from tool_button import ToolButton
#from push_button import PushButton

from PyQt4 import QtGui, QtCore

class TitleWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TitleWidget, self).__init__(parent)
        #QtGui.QWidget.__init__(self, parent)

        self.btn_min = QtGui.QPushButton(QtGui.QIcon('icons/remove-circular.png'), '')
        self.btn_max = QtGui.QPushButton(QtGui.QIcon('icons/add-circular.png'), '')
        self.btn_close = QtGui.QPushButton(QtGui.QIcon('icons/delete.png'), '')

        self.lab_title = QtGui.QLabel()
        self.lab_title.setStyleSheet("color:white")

        # Set the picture of buttons
        #self.btn_min.loadPixmap('./icons/remov-circular.png')
        #self.btn_max.loadPixmap('./icons/add-circular.png')
        #self.btn_close.loadPixmap('./icons/delete.png')

        self.connect(self.btn_min, SIGNAL("clicked()"), self, SIGNAL("showMin()"))
        self.connect(self.btn_max, SIGNAL("clicked()"), self, SIGNAL("showMax()"))
        self.connect(self.btn_close, SIGNAL("clicked()"), self, SIGNAL("showClose()"))

        title_layout = QtGui.QHBoxLayout()
        title_layout.addWidget(self.lab_title, 0, QtAlignVCenter)
        title_layout.addStretch()
        title_layout.addWidget(self.btn_min, 0, Qt.AlignTop)
        title_layout.addWidget(self.btn_max, 0, Qt.AlignTop)
        title_layout.addWidget(self.btn_close, 0, Qt.AlignTop)

        lab_logo = QtGui.QLabel()
        pixmap = QtGui.QPixmap("./icons/video.png")
        lab_logo.setPixmap(pixmap)
        lab_logo.setFixedSize(pixmap.size())
        lab_logo.setCursor(Qt.PointingHandCursor)

        self.translateLanguage()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    title = TitleWidget()
    title.show()
    app.exec_()

