"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
from PySide6 import QtWidgets, QtCore
from a_threads import WeatherHandler
from hw_3.ui.weather import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.error_msg = f"Latitude should always be between -90 and 90.\nLongitude should always be between -180 and 180."

    def initSignals(self):
        self.ui.getWeatherBTN.clicked.connect(self.onBtnPressed)
        self.weatherInfo.finished.connect(self.onWeatherThreadFinished)
        self.weatherInfo.weatherInfoReceived.connect(self.onWeatherInfoReceived)
        self.weatherInfo.connectionError.connect(self.onConnectionError)

    def onBtnPressed(self, status):

        if status:
            try:
                lat = round(float(self.ui.latitude.text()), 2)
                lon = round(float(self.ui.longitude.text()), 2)
                if lat < -90 or lat > 90 or lon < -180 or lon > 180:
                    raise ValueError
            except:
                QtWidgets.QMessageBox.about(self, "ERROR", self.error_msg)
                self.ui.plainTextEditInfo.setPlainText(self.error_msg)
                self.ui.getWeatherBTN.setChecked(False)
                return
            delay = int(self.ui.spinBoxDelay.text())
            self.weatherInfo.setApiUrl(lat, lon)
            self.weatherInfo.setDelay(delay)
            self.weatherInfo.start()
            self.ui.getWeatherBTN.setText("Stop")
            self.ui.spinBoxDelay.setEnabled(False)
            self.ui.longitude.setEnabled(False)
            self.ui.latitude.setEnabled(False)
        else:
            self.ui.getWeatherBTN.setEnabled(False)
            self.weatherInfo.stop()

    def onWeatherThreadFinished(self):
        self.ui.getWeatherBTN.setText("Get Weather Info")
        self.ui.getWeatherBTN.setEnabled(True)
        self.ui.spinBoxDelay.setEnabled(True)
        self.ui.longitude.setEnabled(True)
        self.ui.latitude.setEnabled(True)

    def onWeatherInfoReceived(self, data):
        latitude = str(data['latitude'])
        longitude = str(data['longitude'])
        temperature = str(data['current_weather']['temperature'])
        windspeed = str(data['current_weather']['windspeed'])
        now = QtCore.QDateTime.currentDateTime().toString('HH:mm:ss')

        self.ui.plainTextEditInfo.setPlainText(f"{now}\n\n"
                                               f"latitude: {latitude}, longitude: {longitude}\n\n"
                                               f"temperature: {temperature}\n"
                                               f"windspeed: {windspeed}")

    def initThreads(self):
        self.weatherInfo = WeatherHandler()

    def closeEvent(self, event):
        self.weatherInfo.stop()
        self.weatherInfo.quit()

    def onConnectionError(self, e):
        QtWidgets.QMessageBox.about(self, "Connection ERROR", f"Try again later\n{e}")
        self.ui.getWeatherBTN.setChecked(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
