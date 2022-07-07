import time
import re
import psutil
import requests
from PySide2 import QtCore, QtWidgets
from ui.practice_form_design import Ui_Form


class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QThreadPractice, self).__init__(parent)
        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUi()
        self.systemThread.start()

    def initThreads(self):
        self.timerThread = TimerThread()
        self.timerThread.started.connect(self.timerThreadStarted)
        self.timerThread.finished.connect(self.timerThreadFinished)
        self.timerThread.timerSignal.connect(self.timerThreadTimerSignal)

        self.siteThread = SiteThread()
        self.siteThread.started.connect(self.siteThreadStarted)
        self.siteThread.finished.connect(self.siteThreadFinished)
        self.siteThread.siteSignal.connect(self.siteThreadSiteSignal)

        self.systemThread = SystemThread()
        self.systemThread.started.connect(self.systemThreadStarted)
        self.systemThread.finished.connect(self.systemThreadFinished)


    def initUi(self):
        self.ui.pushButtonStopTimer.setEnabled(False)
        self.ui.pushButtonUrlCheckStop.setEnabled(False)
        self.ui.spinBoxUrlCheckTime.setValue(1)
        self.ui.spinBoxUrlCheckTime.setMinimum(1)
        self.ui.pushButtonStartTimer.clicked.connect(self.onPushButtonStartTimerClicked)
        self.ui.pushButtonStopTimer.clicked.connect(self.onPushButtonStopTimerClicked)
        self.ui.pushButtonUrlCheckStart.clicked.connect(self.onPushButtonUrlCheckStart)
        self.ui.pushButtonUrlCheckStop.clicked.connect(self.onPushButtonUrlCheckStop)

    def onPushButtonStartTimerClicked(self):
        self.timerThread.timerCount = self.ui.spinBoxTimerCount.value()
        self.timerThread.start()

    def onPushButtonStopTimerClicked(self):
        self.timerThread.status = False

    def onPushButtonUrlCheckStart(self):
        if self.ui.lineEditURL.text() == "":
            self.ui.lineEditURL.setText("http://www.google.com")
        self.siteThread.siteName = self.ui.lineEditURL.text()
        self.siteThread.timerCount = self.ui.spinBoxUrlCheckTime.value()
        self.siteThread.start()

    def onPushButtonUrlCheckStop(self):
        self.siteThread.status = False

    def timerThreadStarted(self):
        self.ui.spinBoxTimerCount.setEnabled(False)
        self.ui.pushButtonStartTimer.setEnabled(False)
        self.ui.pushButtonStopTimer.setEnabled(True)

    def timerThreadFinished(self):
        self.ui.spinBoxTimerCount.setEnabled(True)
        self.ui.pushButtonStartTimer.setEnabled(True)
        self.ui.pushButtonStopTimer.setEnabled(False)
        self.ui.lineEditTimerEnd.setText("0")

    def timerThreadTimerSignal(self, emit_value):
        self.ui.lineEditTimerEnd.setText(emit_value)

    def siteThreadStarted(self):
        self.ui.spinBoxUrlCheckTime.setEnabled(False)
        self.ui.pushButtonUrlCheckStart.setEnabled(False)
        self.ui.pushButtonUrlCheckStop.setEnabled(True)

    def siteThreadFinished(self):
        self.ui.spinBoxUrlCheckTime.setEnabled(True)
        self.ui.pushButtonUrlCheckStart.setEnabled(True)
        self.ui.pushButtonUrlCheckStop.setEnabled(False)

    def siteThreadSiteSignal(self, emit_value):
        self.ui.plainTextEditUrlCheckLog.appendPlainText(emit_value)

    def systemThreadStarted(self):
        ...

    def systemThreadFinished(self):
        ...

class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timerCount = None
        self.status = None

    def run(self) -> None:
        self.status = True
        for i in range(self.timerCount, 0, -1):
            if self.status == True:
                self.timerSignal.emit(str(i))
                time.sleep(0.5)

class SiteThread(QtCore.QThread):
    siteSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.siteName = None
        self.status = None
        self.timerCount = None

    def run(self):
        self.status = True
        while self.status == True:
            self.r = requests.get(self.siteName)
            self.siteSignal.emit(f"{time.ctime()}, Статус - {str(self.r.status_code)}")
            for i in range(self.timerCount, 0, -1):
                if self.status == True:
                    time.sleep(1)

class SystemThread(QtCore.QThread):
    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self) -> None:
        while True:
            print(f"{time.ctime()} - Third thread running")
            time.sleep(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()
    myapp.show()

    app.exec_()
