from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
from datetime import timedelta

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

    def mouseDoublClickEvent(self, event):
        self.doubleClicked.emit()

    def mouseMoveEvent(self, event):
        self.mouseTrack.emit(event)

    def keyPresseEvent(self, event):
        self.keyPressed.emit(event)

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.media = Phonon.MediaObject(self)
        #self.media.stateChanged.connect(self.handleStateChanged)

        self.video = Video(self)

        self.video.setMinimumSize(800, 600)
        self.video.doubleClicked.connect(self.toggle_fullscreen)
        self.video.keyPressed.connect(self.handle_key)

        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)

        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)

        self.btn_open = QtGui.QPushButton(QtGui.QIcon('icons/video.png'), '')
        self.btn_open.clicked.connect(self.handle_btn_open)

        self.btn_play = QtGui.QPushButton(QtGui.QIcon('icons/play.png'), '')
        self.btn_play.clicked.connect(self.handle_btn_play)        

        self.btn_pause = QtGui.QPushButton(QtGui.QIcon('icons/pause.png'), '')
        self.btn_pause.clicked.connect(self.handle_btn_pause)
    
        self.btn_stop = QtGui.QPushButton(QtGui.QIcon('icons/stop.png'), '')
        self.btn_stop.clicked.connect(self.handle_btn_stop)

        self.btn_fullscreen = QtGui.QPushButton(QtGui.QIcon('icons/expand.png'), '')
        self.btn_fullscreen.clicked.connect(self.handle_btn_fullscreen)

        cur_time = str(timedelta(seconds = self.media.currentTime() / 1000))
        total_time = str(timedelta(seconds = self.media.totalTime() / 1000))
        self.lab_cur_time = QtGui.QLabel(cur_time)
        self.lab_total_time = QtGui.QLabel(total_time)

        #self.list = QtGui.QListWidget(self)
        #self.list.addItems(Phonon.BackendCapabilities.availableMimeTypes())

        self.slider = Phonon.SeekSlider(self)
        self.slider.setMediaObject(self.media)

        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory)
        Phonon.createPath(self.media, self.audio_output) 
        self.volumeSlider = Phonon.VolumeSlider()
        #self.volumeSlider.setAudioOuput(self.audio_output)
        self.volumeSlider.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)

        control_layout = QtGui.QHBoxLayout()
        control_layout.addWidget(self.btn_open)
        control_layout.addWidget(self.btn_play)
        control_layout.addWidget(self.btn_pause)
        control_layout.addWidget(self.btn_stop)
        control_layout.addWidget(self.lab_cur_time)
        control_layout.addWidget(self.slider)
        control_layout.addWidget(self.lab_total_time)
        control_layout.addWidget(self.btn_fullscreen)
        control_layout.addWidget(self.volumeSlider)

        video_layout = QtGui.QVBoxLayout()
        video_layout.addWidget(self.video)

        mainlayout = QtGui.QVBoxLayout(self)
        mainlayout.addLayout(video_layout)
        mainlayout.addLayout(control_layout)

        self.setLayout(mainlayout)
        #layout.addWidget(self.list)


    def handle_btn_open(self):
        #if self.media.state() == Phonon.PlayingState:
        #    self.media.stop()
        #else:
        #    path = QtGui.QFileDialog.getOpenFileName(self, self.btn_open.text())
        #    if path:
        #        self.media.setCurrentSource(Phonon.MediaSource(path))
        #        self.media.play()
        path = QtGui.QFileDialog.getOpenFileName(self, self.btn_open.text())
        if path:
            self.media.setCurrentSource(Phonon.MediaSource(path))
            self.media.play()

    def handle_btn_play(self):
        self.btn_play.setEnabled(False)
        self.media.setTickInterval(400)
        self.media.play()

    def handle_btn_pause(self):
        self.btn_play.setEnabled(True)
        self.media.pause()

    def handle_btn_stop(self):
        self.btn_play.setEnabled(True)
        self.media.stop()

    def handle_btn_fullscreen(self):
        if self.video.isFullScreen():
            self.video.setFullScreen(False) 
        else:
            self.video.setFullScreen(True)
    
    def toggle_fullscreen(self):
        if self.video.isFullScreen():
            self.video.setFullScreen(False)
        else:
            self.video.setFullScreen(True)

    def handle_key(self, e): 
        if e.key() == QtCore.Qt.Key_Esc:
            self.video.exitFullScreen(True)

    #def handleStateChanged(self, newstate, oldstate):
    #    if newstate == Phonon.PlayingState:
    #        self.btn_open.setText('Stop')
    #    elif (newstate != Phonon.LoadingState and
    #          newstate != Phonon.BufferingState):
    #        self.btn_open.setText('Choose File')
    #        if newstate == Phonon.ErrorState:
    #            source = self.media.currentSource().fileName()
    #            print ('ERROR: could not play:', source.toLocal8Bit().data())
    #            print ('  %s' % self.media.errorString().toLocal8Bit().data())

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('GracePlay')
    window = Window()
    window.show()
    sys.exit(app.exec_())
