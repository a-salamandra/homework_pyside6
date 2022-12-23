"""
Модуль в котором содержаться потоки Qt
"""

import time
import psutil
import requests
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list) # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            info = [cpu_value, ram_value]
            self.systemInfoReceived.emit(info)
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay



class WeatherHandler(QtCore.QThread):
    weatherInfoReceived = QtCore.Signal(dict)
    connectionError = QtCore.Signal(str)

    def __init__(self, lat=0, lon=0, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = False
        self.__latitude = lat
        self.__longitude = lon

    def setApiUrl(self, lat, lon):
        self.__latitude = lat
        self.__longitude = lon
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    def setDelay(self, delay) -> None:
        self.__delay = delay

    def stop(self):
        self.__status = False

    def run(self) -> None:
        self.__status = True

        while self.__status:
            try:
                response = requests.get(self.__api_url)
                data = response.json()
                self.weatherInfoReceived.emit(data)
                time.sleep(self.__delay)
                # print(data)
            except requests.exceptions.ConnectionError as e:
                self.stop()
                self.connectionError.emit(str(e.args[0].reason))



