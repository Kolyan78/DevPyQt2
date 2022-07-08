from PyQt5 import QtCore, QtWidgets


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.count = 0

    def run(self) -> None:
        self.running = True
        while self.running:
            self.count += 1
            self.mysignal.emit("count = %s" % self.count)
            self.sleep(1)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Press button for start thread")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnStart = QtWidgets.QPushButton("Start process")
        self.btnStop = QtWidgets.QPushButton("Stop process")
        self.btnStop.setDisabled(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        self.btnStart.clicked.connect(self.on_start)
        self.btnStop.clicked.connect(self.on_stop)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)


    def on_start(self):
        if not self.mythread.isRunning():
            self.mythread.start()
            self.btnStop.setDisabled(False)
            self.btnStart.setDisabled(True)

    def on_stop(self):
        self.mythread.running = False
        self.btnStop.setDisabled(True)
        self.btnStart.setDisabled(False)

    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        self.hide()
        self.mythread.running = False
        self.mythread.wait(5000)
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Start y Stop Thread")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())
