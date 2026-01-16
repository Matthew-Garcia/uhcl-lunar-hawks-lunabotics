# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network, time

SSID = "Team23"
#"Mr Jiggys"        # ← Change this to your Wi-Fi name
PASSWORD = "uhclgambit"
# "Spaceman466"    # ← Change this to your Wi-Fi password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    time.sleep(1)

print("Connected! IP:", wlan.ifconfig()[0])
