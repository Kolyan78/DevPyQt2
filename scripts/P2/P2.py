from PySide2 import QtCore, QtWidgets, QtGui
from ui import P2_MyForm
import time


class MyWidgetsForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWidgetsForm, self).__init__(parent)
        self.ui = P2_MyForm.Ui_Form()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems(["BIN", "OCT", "DEC", "HEX"])
        self.ui.lcdNumber.setBinMode()
        self.ui.lcdNumber.setDigitCount(8)

        self.ui.comboBox.currentIndexChanged.connect(self.changeLCD)
        self.ui.dial.valueChanged.connect(self.showLCD)
        self.ui.horizontalSlider.valueChanged.connect(self.showLCD)

        self.ui.pushButtonLT.clicked.connect(self.editPosition)
        self.ui.pushButtonRT.clicked.connect(self.editPosition)
        self.ui.pushButtonLB.clicked.connect(self.editPosition)
        self.ui.pushButtonRB.clicked.connect(self.editPosition)
        self.ui.pushButtonCenter.clicked.connect(self.editPosition)

        self.ui.pushButtonGetData.clicked.connect(self.getScreenInfo)

    def showLCD(self):
        if self.sender().objectName() == 'dial':
            value = self.ui.dial.value()
            self.ui.horizontalSlider.setValue(value)
        if self.sender().objectName() == 'horizontalSlider':
            value = self.ui.horizontalSlider.value()
            self.ui.dial.setValue(value)
        self.ui.lcdNumber.display(value)


    def changeLCD(self):
        # print(self.ui.comboBox.currentText())
        a = {"HEX": self.ui.lcdNumber.setHexMode, "OCT": self.ui.lcdNumber.setOctMode,
             "DEC": self.ui.lcdNumber.setDecMode, "BIN": self.ui.lcdNumber.setBinMode}
        a[self.ui.comboBox.currentText()]()
        print(self.ui.lcdNumber.mode())

    def editPosition(self):
        print(f"Окно перемещено {self.sender().text().lower()}")
        buttonText = self.sender().text()
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        # print(f"Разрешение экрана: {screenWidth} х {screenHeight}")
        print(f"Размер окна: {self.width()} х {self.height()}")

        position = {"Влево вверх": (0, 0),
                    "Влево вниз": (0, screenHeight - self.height() - 70),
                    "В центр": (screenWidth / 2 - self.width() / 2, screenHeight / 2 - self.height() / 2),
                    "Вправо вверх": (screenWidth - self.width(), 0),
                    "Вправо вниз": (screenWidth - self.width(), screenHeight - self.height() - 70)}

        self.move(position.get(buttonText)[0], position.get(buttonText)[1])
        print(f"Позиция окна: {self.pos().x()}, {self.pos().y()}")

    @QtCore.Slot()
    def getScreenInfo(self):
        """Получение параметров экрана"""
        screens_count = QtWidgets.QApplication.screens()
        log = self.ui.plainTextEdit.appendPlainText

        log(time.ctime())
        log(f"{15*'='} SystemInfo {15*'='}")
        log(f"Кол-во экранов: {len(screens_count)}")
        log(f"Основное окно: {QtWidgets.QApplication.primaryScreen().name()}")
        for cur_screen in screens_count:
            log(f"Разрешение экрана {cur_screen.name()}: {cur_screen.size().width()} х {cur_screen.size().height()}")
        log(f"Окно находится на экране {QtWidgets.QApplication.screenAt(self.pos()).name()}")
        log(f"Размеры окна: ширина {self.size().width()} высота {self.size().height()}")
        log(f"Минимальные размеры окна: ширина {self.minimumWidth()} высота {self.minimumHeight()}")
        log(f"Текущее положение: x = {self.pos().x()} y = {self.pos().y()}")
        log(f"Центр приложения: x = {self.pos().x() + self.width()/2} y = {self.pos().y() + self.height()/2}")
        log(f"{38 * '='}\n")

    def printTime(self):
        return time.strftime('%d.%m.%Y %H:%M:%S')

    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                self.ui.plainTextEdit.appendPlainText(f"{self.printTime()} Окно свернуто")
            elif self.isMaximized():
                self.ui.plainTextEdit.appendPlainText(f"{self.printTime()} Окно развернуто")
        if event.type() == QtCore.QEvent.ActivationChange:
            self.ui.plainTextEdit.appendPlainText(f"{self.printTime()} Окно активно")
        QtWidgets.QWidget.changeEvent(self, event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(f"{self.printTime()} Изменение положения окна. Новые координаты: {self.pos().x()}, {self.pos().y()}")

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        print(f"{self.printTime()} Изменение размеров окна. Новый размер: {self.size().width()} x {self.size().height()}")

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        print(f"{self.printTime()} Окно скрыто.")

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        print(f"{self.printTime()} Окно отображено.")

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно",
                                               "Вы хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event:QtGui.QKeyEvent) -> None:
        print(f"Нажата клавиша {event.key()}")

    def event(self, event: QtCore.QEvent) -> bool:
        return QtWidgets.QWidget.event(self, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyWidgetsForm()
    myapp.show()

    app.exec_()
