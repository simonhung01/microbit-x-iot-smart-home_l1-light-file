let light_intensity = 0
basic.forever(function () {
    light_intensity = pins.analogReadPin(AnalogPin.P2)
    pins.analogWritePin(AnalogPin.P0, light_intensity)
})
