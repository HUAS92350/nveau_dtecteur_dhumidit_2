led.enable(False)
I2C_LCD1602.lcd_init(39)
calcul1 = pins.analog_read_pin(AnalogPin.P0) / 15
calcul1 += 43
calcul = Math.round(calcul1)
pins.digital_write_pin(DigitalPin.P16, 0)
pins.digital_write_pin(DigitalPin.P4, 1)
pins.digital_write_pin(DigitalPin.P5, 0)
pins.digital_write_pin(DigitalPin.P6, 1)
pins.digital_write_pin(DigitalPin.P7, 0)
pins.servo_write_pin(AnalogPin.P8, 55)
pins.servo_write_pin(AnalogPin.P9, 140)
I2C_LCD1602.show_string("IL FAIT BEAU", 0, 0)
I2C_LCD1602.show_string("HUMIDITE %", 0, 1)
I2C_LCD1602.show_number(calcul, 12, 1)
basic.pause(500)

def on_forever():
    global calcul1, calcul
    led.enable(False)
    calcul1 = pins.analog_read_pin(AnalogPin.P0) / 15
    calcul1 += 43
    calcul = Math.round(calcul1)
    if pins.analog_read_pin(AnalogPin.P0) > 500:
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("IL PLEUT", 0, 0)
        I2C_LCD1602.show_string("HUMIDITE %", 0, 1)
        if calcul > 100:
            I2C_LCD1602.show_number(99, 12, 1)
        else:
            I2C_LCD1602.show_number(calcul, 12, 1)
        pins.digital_write_pin(DigitalPin.P4, 0)
        pins.digital_write_pin(DigitalPin.P5, 1)
        pins.digital_write_pin(DigitalPin.P6, 0)
        pins.digital_write_pin(DigitalPin.P7, 1)
        basic.pause(500)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        pins.servo_write_pin(AnalogPin.P8, 145)
        basic.pause(100)
        pins.servo_write_pin(AnalogPin.P9, 35)
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P16, 1)
        music.rest(music.beat(BeatFraction.QUARTER))
        pins.digital_write_pin(DigitalPin.P16, 0)
        basic.pause(100)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P16, 0)
        music.rest(music.beat(BeatFraction.QUARTER))
    else:
        I2C_LCD1602.show_string("IL FAIT BEAU", 0, 0)
        I2C_LCD1602.show_string("HUMIDITE %", 0, 1)
        I2C_LCD1602.show_number(calcul, 12, 1)
        led.enable(False)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P16, 0)
        pins.digital_write_pin(DigitalPin.P4, 1)
        pins.digital_write_pin(DigitalPin.P5, 0)
        pins.digital_write_pin(DigitalPin.P6, 1)
        pins.digital_write_pin(DigitalPin.P7, 0)
        pins.servo_write_pin(AnalogPin.P8, 55)
        pins.servo_write_pin(AnalogPin.P9, 140)
        music.rest(music.beat(BeatFraction.QUARTER))
basic.forever(on_forever)
def Eau_vive_1():
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
def Eau_vive_4():
    music.play_tone(392, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.DOUBLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.WHOLE))
def Eau_vive_3():
    music.play_tone(587, music.beat(BeatFraction.DOUBLE))
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    music.play_tone(659, music.beat(BeatFraction.DOUBLE))
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(587, music.beat(BeatFraction.DOUBLE))
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.DOUBLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.WHOLE))
def Eau_vive_2():
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.WHOLE))
Eau_vive_1()
Eau_vive_2()
Eau_vive_3()
Eau_vive_4()