"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from a_threads import SystemInfo
from hw_3.ui.sysinfo import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.verticalSlider.valueChanged.connect(self.onSliderChange)
        self.systemInfo.systemInfoReceived.connect(self.onGettingInfo)

    def onSliderChange(self):
        self.systemInfo.delay = self.ui.verticalSlider.value()
        self.ui.lcdDelay.display(self.ui.verticalSlider.value())

    def onGettingInfo(self, info):
        cpu_value, ram_value = info
        self.ui.lcdCPU.display(cpu_value)
        self.ui.lcdRAM.display(ram_value)

    def initThreads(self):
        self.systemInfo = SystemInfo()
        self.systemInfo.start()

    def closeEvent(self, event):
        self.systemInfo.terminate()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
