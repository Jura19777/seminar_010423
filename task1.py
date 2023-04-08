"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight(object):
    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self.__color = 'Красный'
            print(self.__color)
            time.sleep(7)

            self.__color = 'Желтый'
            print(self.__color)
            time.sleep(2)

            self.__color = 'Зеленый'
            print(self.__color)
            time.sleep(5)


traffic_light = TrafficLight()
traffic_light.running()