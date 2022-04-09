from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print('Lamp on')

    def turn_off(self):
        print('Lamp off')

class Fan(Switchable):
    def turn_on(self):
        print('Fan on')

    def turn_off(self):
        print('Fan off')

class ElectricPowerSwitch:
    def __init__(self,c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True

l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
