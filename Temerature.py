# Created by: John Hanekom
# Date: September 26th, 2022
# 
# This program says the temperature every second

current_temperature = 0
def on_forever():
    global current_temperature
    current_temperature = input.temperature()
    basic.show_number(current-temperature)
    basic.pause(1000)
    basic.clear_screen()
basic.forever(on_forever)

