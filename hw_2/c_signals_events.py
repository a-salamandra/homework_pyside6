"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QScreen
from ui.c import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.setupXYSpinBoxes()

    def initSignals(self):
        self.ui.pushButtonLT.clicked.connect(self.onButtonMoveTopLeftClicked)
        self.ui.pushButtonRT.clicked.connect(self.onButtonMoveTopRightClicked)
        self.ui.pushButtonLB.clicked.connect(self.onButtonMoveBottomLeftClicked)
        self.ui.pushButtonRB.clicked.connect(self.onButtonMoveBottomRightClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onButtonCenterClicked)

        self.ui.pushButtonMoveCoords.clicked.connect(self.onButtonMoveCoordClicked)
        self.ui.pushButtonGetData.clicked.connect(self.onButtonGetDataClicked)

    def onButtonMoveTopLeftClicked(self):
        self.move(0, 0)

    def onButtonMoveTopRightClicked(self):
        display_width = self.screen().size().width()
        self.move(display_width - self.width(), 0)

    def onButtonMoveBottomLeftClicked(self):
        display_height = self.screen().size().height()
        self.move(0, display_height - self.height())

    def onButtonMoveBottomRightClicked(self):
        display_height = self.screen().size().height()
        display_width = self.screen().size().width()
        self.move(display_width - self.width(), display_height - self.height())

    def onButtonCenterClicked(self):
        display_height = self.screen().size().height()
        display_width = self.screen().size().width()
        self.move((display_width - self.width()) // 2, (display_height - self.height()) // 2)

    def onButtonMoveCoordClicked(self):
        x = int(self.ui.spinBoxX.text())
        y = int(self.ui.spinBoxY.text())
        self.move(x, y)

    def setupXYSpinBoxes(self):
        display_height = QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).height()
        display_width = QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).width()

        self.ui.spinBoxX.setMinimum(0)
        self.ui.spinBoxX.setMaximum(display_width)
        self.ui.spinBoxY.setMinimum(0)
        self.ui.spinBoxY.setMaximum(display_height)

        self.ui.spinBoxX.setMinimumWidth(45)
        self.ui.spinBoxY.setMinimumWidth(45)

    def onButtonGetDataClicked(self):
        self.ui.plainTextEdit.setPlainText(
            f"Текущее время: {QtCore.QDateTime.currentDateTime().toString('HH:mm:ss dd.MM.yy t')}\n"
            f"Кол-во экранов: {len(QtGui.QGuiApplication.screens())}\n"
            f"Текущее основное окно: { QtGui.QGuiApplication.applicationDisplayName()}\n"
            f"Разрешение экрана: {self.screen().size().width()} x"
            f" {self.screen().size().height() }\n"
            f"Окно находится на экране {self.screen().name()}\n"
            f"Размеры окна: {self.width()} x {self.height()}\n"
            f"Минимальные размеры окна: {self.minimumWidth()} x {self.minimumHeight()}\n"
            f"Текущее координаты окна: {self.geometry().getCoords()}\n"
            f"Координаты центра приложения: {self.geometry().center().toTuple()}\n"
            f"Состояние окна: {QtGui.QGuiApplication.applicationState().name}")

    def event(self, event):

        if event.type() == QtCore.QEvent.Type.Move:
            print(f"В {QtCore.QDateTime.currentDateTime().toString('HH:mm:ss dd.MM.yy t')} произошло перемещение окна!\n"
            f"прежняя позиция: {event.oldPos()}\nновая позиция: {event.pos()}")

        if event.type() == QtCore.QEvent.Type.Resize:
            print(f"В {QtCore.QDateTime.currentDateTime().toString('HH:mm:ss dd.MM.yy t')} произошло изменение размера окна!\n"
                  f"новый размер: {event.size().width()} x {event.size().height()}")

        return super(Window, self).event(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
