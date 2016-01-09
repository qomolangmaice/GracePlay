#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: title_widget.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.07 21:31:25

#from tool_button import ToolButton
from push_button import PushButton

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

class TitleWidget(QWidget):
    def __init__(self, parent=None):
        super(TitleWidget, self).__init__(parent)

        self.btn_mainmenu = PushButton(self)
        self.btn_min = PushButton(self)
        self.btn_max = PushButton(self)
        self.btn_close = PushButton(self)

        # Set logo picture 
        self.lab_logo = QLabel()
        pixmap = QPixmap("./../icons/video.png")
        self.lab_logo.setPixmap(pixmap)
        self.lab_logo.setFixedSize(pixmap.size())
        #self.lab_logo.setFixedSize(25, 25)
        #self.lab_logo.setIconSize(QSize(25, 25))
        self.lab_logo.setStyleSheet("background:transparent")   # set logo transparent
        self.lab_logo.setCursor(Qt.PointingHandCursor)

        # Set Title color
        self.lab_title = QLabel()
        self.lab_title.setText(u'GracePlay-version 0.1')

        # Set the picture of buttons
        self.btn_mainmenu.loadPixmap('./../icons/main_menu.png')
        self.btn_min.loadPixmap('./../icons/min_button.png')
        self.btn_max.loadPixmap('./../icons/max_button.png')
        self.btn_close.loadPixmap('./../icons/close_button.png')

        self.connect(self.btn_mainmenu, SIGNAL("clicked()"), self, SIGNAL("showMainMenu()"))
        self.connect(self.btn_min, SIGNAL("clicked()"), self, SIGNAL("showMin()"))
        self.connect(self.btn_max, SIGNAL("clicked()"), self, SIGNAL("showMax()"))
        self.connect(self.btn_close, SIGNAL("clicked()"), self, SIGNAL("showClose()"))

        
        title_layout = QHBoxLayout()
        title_layout.addWidget(self.lab_logo, 0, Qt.AlignTop)
        title_layout.addWidget(self.lab_title, 0, Qt.AlignTop)
        title_layout.setSpacing(0)
        title_layout.addStretch()
        title_layout.addWidget(self.btn_mainmenu, 0, Qt.AlignTop)
        title_layout.addWidget(self.btn_min, 0, Qt.AlignTop)
        title_layout.addWidget(self.btn_max, 0, Qt.AlignTop)
        title_layout.addWidget(self.btn_close, 0, Qt.AlignTop)
        title_layout.setContentsMargins(0, 0, 5, 0)

        # Set hints of the buttons
        self.translateLanguage()

        self.setLayout(title_layout)
        self.setFixedHeight(60)
        self.is_move = False 

        #self.translateLanguage()

    def translateLanguage(self):
        self.btn_mainmenu.setToolTip(u"主菜单")
        self.btn_min.setToolTip(u"最小化")
        self.btn_max.setToolTip(u"最大化")
        self.btn_close.setToolTip(u"关闭")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    title = TitleWidget()
    title.show()
    app.exec_()

