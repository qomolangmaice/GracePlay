#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# File Name: main.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.05 20:51:41

import sys
import gettext

from PyQt4 import QtGui, QtCore 

import model
import view
import controller

def main():
    gettext.install('main', 'i18n', unicode=True, names = ['ugettext'])
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName(_('GracePlay'))
    playlist_model = model.PlayListModel()
    graceplay = view.GracePlay()
    graceplaycontroller = controller.GracePlayController(playlist_model, graceplay)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
