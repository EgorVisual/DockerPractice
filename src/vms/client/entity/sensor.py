import math
import random


class Sensor:
    _value: float
    name: str
    type: str
    step = 1706

    def __init__(self, name):
        self.name = name

    def generate_new_value(self):
        pass

    def get_data(self):
        return self._value

    def __str__(self):
        return str({"type": self.type, "name": self.name, "value": self.get_data()})


class Temperature(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "temperature"

    def generate_new_value(self):
        self._value = random.random() * 10 + self.step/100


class Current(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "current"

    def generate_new_value(self):
        self._value = math.sin(self.step/100) * 10
        self.step = self.step + 100


class Pressure(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "pressure"

    def generate_new_value(self):
        self._value = random.random() * 1000 + self.step


class Voltage(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "voltage"

    def generate_new_value(self):
        self._value = random.random() + self.step/100
