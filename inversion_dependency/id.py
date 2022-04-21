from abc import ABC, abstractmethod


# abstract class
class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# concrete class inherits from abstract class
class Lamp(Switchable):
    def turn_on(self):
        print("Lamp is on")

    def turn_off(self):
        print("Lamp is off")


# concrete class inherits from abstract class
class Fun(Switchable):
    def turn_on(self):
        print("Fun is on")

    def turn_off(self):
        print("Fun is off")


# concrete class inherits from abstract class
class PowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
