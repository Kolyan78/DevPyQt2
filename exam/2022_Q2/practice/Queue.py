from PyQt5 import QtCore, QtWidgets
import queue


class MyThread(QtCore.QThread):
    task_done = QtCore.pyqtSignal(int, int, name = 'taskdone')
    def __init__(self, id, queue, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id
        self.queue = queue

    def run(self):
        while True:
            task = self.queue.get()
            self.sleep(5)
            self.task_done.emit(task, self.id)
            self.queue.task_done()


class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Раздать задания")
        self.queue = queue.Queue()

