class LightBulb:
    def turn_on(self):
        print('Lamp on')

    def turn_off(self):
        print('Lamp off')

class ElectricPowerSwitch:
    def __init__(self,l: LightBulb):
        self.light_bulb = l
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
