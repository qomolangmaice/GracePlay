#!/usr/bin/env python
#-*- coding=utf-8 -*-
# File Name: push_button.py
# Description: Set style and special effects of the buttons 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.09 21:59:42

from PyQt4.QtGui import *
from PyQt4.Qt import *

class PushButton(QPushButton):
    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        self.status = 0

    def loadPixmap(self, pic_name):
        self.pixmap = QPixmap(pic_name)
        self.btn_width = self.pixmap.width()/4
        self.btn_height = self.pixmap.height()
        self.setFixedSize(self.btn_width, self.btn_height)

    def enterEvent(self, event):
        self.status = 1
        self.update()

    def mousePressEvent(self, event):
        # If you click left key of mouse
        if(event.button() == Qt.LeftButton):
            self.mouse_press = True
            self.status = 2     # self.PRESS
            self.update()

    def mouseReleaseEvent(self, event):
        # IF you click left key of mouse
        if(self.mouse_press):
            self.mouse_press = False
            self.status = 3     # self.ENTER
            self.update()
            self.clicked.emit(True)

    def leaveEvent(self, event):
        self.status = 0     # self.Normal
        self.update()

    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), self.pixmap.copy(self.btn_width * self.status, 0, self.btn_width, self.btn_height))
        self.painter.end()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    btn = PushButton()
    btn.loadPixmap("./../icons/max_button.png")
    btn.show()
    sys.exit(app.exec_())


