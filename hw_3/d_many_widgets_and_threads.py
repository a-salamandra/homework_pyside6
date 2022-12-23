"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFrame, QSizePolicy

from c_weatherapi_widget import Window as WeatherWindow
from b_systeminfo_widget import Window as SysinfoWindow


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        self.weather = WeatherWindow()
        self.sysinfo = SysinfoWindow()

        separador = QFrame()
        separador.setFrameShape(QFrame.VLine)
        separador.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        separador.setLineWidth(1)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.sysinfo)
        layout.addWidget(separador)
        layout.addWidget(self.weather)
        self.setLayout(layout)
        self.setWindowTitle("(´｡• ᵕ •｡`)")

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()