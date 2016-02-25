#!/usr/bin/env python
#-*- coding=utf-8 -*-
# File Name: playlist.py
# Description: 
# Author: iczelion
# Email: qomolangmaice@163.com 
# Created: 2016.01.13 18:40:09

import os

from PyQt4 import QtCore


class PlayListModel(QtCore.QAbstractListModel):
    """
    """

    def __init__(self, playlist=[],parent=None):
        """Construct a playlist model with a given playlist and parent.

        Arguments:

        - playlist: original playlist passed to the model
        """
        QtCore.QAbstractListModel.__init__(self, parent)
        self._playlist = playlist


    def __getitem__(self, i):
        return self._playlist[i]


    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._playlist)


    def data(self, index, role=QtCore.Qt.DisplayRole):
        value = self._playlist[index.row()]
        if role == QtCore.Qt.DisplayRole:
            if type(value) == QtCore.QString:
                return QtCore.QFileInfo(value).baseName()
            elif type(value) == QtCore.QUrl:
                return QtCore.QFileInfo(value.path()).baseName()
        if role == QtCore.Qt.ToolTipRole:
            if type(value) == QtCore.QString:
                return value
            elif type(value) == QtCore.QUrl:
                return value.toString()


    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            self._playlist[row] = value
            self.dataChanged.emit(index, index)
            return True
        return False


    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position+rows-1)
        for i in range(rows):
            self._playlist.insert(position, '')
        self.endInsertRows()
        return True


    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position+rows-1)
        for i in range(rows):
            self._playlist.pop(position)
        self.endRemoveRows()
        return True


    def append(self, value):
        self.insert(self.rowCount(), value)


    def clear(self):
        self.removeRows(0, self.rowCount())


    def extend(self, value_list):
        for value in value_list:
            self.append(value)


    def insert(self, position, value):
        if value not in self._playlist:
            self.insertRows(position, 1)
            index = self.index(position)
            self.setData(index, value)


    def pop(self, position=-1):
        if not self.rowCount():
            return
        elif position == -1:
            position += self.rowCount()
        self.removeRows(position, 1)
