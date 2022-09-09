let calcul = 0
let calcul2 = 0
let calcul1 = 0
led.enable(false)
I2C_LCD1602.LcdInit(39)
max7219_matrix.setup(
12,
DigitalPin.P16,
DigitalPin.P15,
DigitalPin.P14,
DigitalPin.P13
)
max7219_matrix.brightnessAll(5)
let LED1 = max7219_matrix.getCustomCharacterArray(
"B10000001,B01000010,B00011000,B00111100,B00111100,B00011000,B01000010,B10000001"
)
let LED2 = max7219_matrix.getCustomCharacterArray(
"B00001100,B00001010,B11111010,B10001010,B00001100"
)
pins.servoWritePin(AnalogPin.P8, 55)
pins.servoWritePin(AnalogPin.P9, 140)
basic.forever(function () {
    led.enable(false)
    basic.pause(100)
    calcul1 = pins.analogReadPin(AnalogPin.P0) - 50
    basic.pause(100)
    calcul2 = calcul1 / 9
    calcul = Math.round(calcul2)
    I2C_LCD1602.clear()
    I2C_LCD1602.ShowString("RISQUE DE PLUIE", 0, 0)
    I2C_LCD1602.ShowString("%", 8, 1)
    I2C_LCD1602.ShowNumber(calcul, 5, 1)
    if (pins.analogReadPin(AnalogPin.P0) < 250) {
        max7219_matrix.clearAll()
        max7219_matrix.for_4_in_1_modules(
        rotation_direction.clockwise,
        false
        )
        max7219_matrix.displayText(
        "SOLEIL",
        35,
        true
        )
        max7219_matrix.displayCustomCharacter(
        LED1,
        64,
        false
        )
        max7219_matrix.displayCustomCharacter(
        LED1,
        88,
        false
        )
        pins.servoWritePin(AnalogPin.P8, 55)
        pins.digitalWritePin(DigitalPin.P4, 1)
        pins.digitalWritePin(DigitalPin.P5, 0)
        basic.pause(100)
        pins.servoWritePin(AnalogPin.P9, 140)
        pins.digitalWritePin(DigitalPin.P6, 1)
        pins.digitalWritePin(DigitalPin.P7, 0)
        basic.pause(1000)
    } else if (pins.analogReadPin(AnalogPin.P0) >= 250 && pins.analogReadPin(AnalogPin.P0) < 400) {
        max7219_matrix.clearAll()
        max7219_matrix.for_4_in_1_modules(
        rotation_direction.clockwise,
        false
        )
        max7219_matrix.displayText(
        "TEMPS",
        67,
        true
        )
        max7219_matrix.displayText(
        "TRES",
        37,
        false
        )
        max7219_matrix.displayText(
        "CLAIR",
        5,
        false
        )
        pins.servoWritePin(AnalogPin.P8, 55)
        pins.digitalWritePin(DigitalPin.P6, 1)
        pins.digitalWritePin(DigitalPin.P7, 0)
        basic.pause(100)
        pins.servoWritePin(AnalogPin.P9, 140)
        pins.digitalWritePin(DigitalPin.P4, 1)
        pins.digitalWritePin(DigitalPin.P5, 0)
        basic.pause(1000)
    } else if (pins.analogReadPin(AnalogPin.P0) >= 400 && pins.analogReadPin(AnalogPin.P0) < 600) {
        max7219_matrix.clearAll()
        max7219_matrix.for_4_in_1_modules(
        rotation_direction.clockwise,
        false
        )
        max7219_matrix.displayText(
        "PEU",
        74,
        true
        )
        max7219_matrix.displayText(
        "DE",
        45,
        false
        )
        max7219_matrix.displayText(
        "NUAGES",
        1,
        false
        )
        pins.servoWritePin(AnalogPin.P8, 145)
        pins.digitalWritePin(DigitalPin.P6, 0)
        pins.digitalWritePin(DigitalPin.P7, 1)
        basic.pause(100)
        pins.servoWritePin(AnalogPin.P9, 140)
        pins.digitalWritePin(DigitalPin.P4, 1)
        pins.digitalWritePin(DigitalPin.P5, 0)
        basic.pause(1000)
    } else if (pins.analogReadPin(AnalogPin.P0) >= 600 && pins.analogReadPin(AnalogPin.P0) < 850) {
        max7219_matrix.clearAll()
        max7219_matrix.for_4_in_1_modules(
        rotation_direction.clockwise,
        false
        )
        max7219_matrix.displayText(
        "TRES",
        70,
        true
        )
        max7219_matrix.displayText(
        "LEGERE",
        34,
        false
        )
        max7219_matrix.displayText(
        "PLUIE",
        5,
        false
        )
        pins.servoWritePin(AnalogPin.P8, 145)
        pins.digitalWritePin(DigitalPin.P6, 0)
        pins.digitalWritePin(DigitalPin.P7, 1)
        basic.pause(100)
        pins.servoWritePin(AnalogPin.P9, 35)
        pins.digitalWritePin(DigitalPin.P4, 0)
        pins.digitalWritePin(DigitalPin.P5, 1)
        basic.pause(1000)
    } else if (pins.analogReadPin(AnalogPin.P0) >= 850) {
        max7219_matrix.clearAll()
        max7219_matrix.for_4_in_1_modules(
        rotation_direction.clockwise,
        false
        )
        max7219_matrix.displayText(
        "PLUIE",
        36,
        true
        )
        max7219_matrix.displayCustomCharacter(
        LED2,
        1,
        false
        )
        max7219_matrix.displayCustomCharacter(
        LED2,
        25,
        false
        )
        pins.servoWritePin(AnalogPin.P8, 145)
        pins.digitalWritePin(DigitalPin.P6, 0)
        pins.digitalWritePin(DigitalPin.P7, 1)
        basic.pause(100)
        pins.servoWritePin(AnalogPin.P9, 35)
        pins.digitalWritePin(DigitalPin.P4, 0)
        pins.digitalWritePin(DigitalPin.P5, 1)
        basic.pause(1000)
    }
})
