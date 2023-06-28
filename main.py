import time
from yeelight import Bulb

bulb = Bulb("192.168.0.238")

for x in range(10):
    bulb.turn_on(effect="sudden")
    time.sleep(0.3)
    bulb.turn_off()
    time.sleep(0.3)

