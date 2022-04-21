from id import Lamp, Fun, PowerSwitch

l = Lamp()
f = Fun()
switch = PowerSwitch(f)
switch.press()
switch.press()
switch = PowerSwitch(l)
switch.press()
switch.press()
