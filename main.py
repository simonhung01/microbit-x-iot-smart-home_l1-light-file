microIoT.microIoT_MQTT_Event(microIoT.TOPIC.topic_0, function (message) {
    if (message == "yes") {
        basic.showIcon(IconNames.Yes)
    }
    if (message == "no") {
        basic.showIcon(IconNames.No)
    }
    if (message == "smile") {
        basic.showIcon(IconNames.Happy)
    }
    if (message == "cry") {
        basic.showIcon(IconNames.Sad)
    }
})
input.onButtonPressed(Button.A, function () {
    microIoT.microIoT_SendMessage("helloworld", microIoT.TOPIC.topic_0)
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.AB, function () {
    length = sonar.ping(
    DigitalPin.P14,
    DigitalPin.P13,
    PingUnit.Centimeters
    )
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 4; index++) {
        microIoT.microIoT_ServoRun(microIoT.aServos.S1, 100)
        basic.pause(1000)
        microIoT.microIoT_ServoRun(microIoT.aServos.S1, -90)
        basic.pause(1000)
    }
})
let length = 0
microIoT.microIoT_WIFI("DGINCB_WT6F", "20210601")
microIoT.microIoT_MQTT(
"vkW338gnR",
"DkZq38gnRz",
"8yre3Ugng",
microIoT.SERVERS.English
)
basic.showIcon(IconNames.Heart)
basic.pause(5000)
microIoT.microIoT_SendMessage("hello", microIoT.TOPIC.topic_0)
basic.forever(function () {
    if (0 < 5) {
        for (let index = 0; index < 10; index++) {
            pins.analogWritePin(AnalogPin.P0, 400)
            basic.pause(1000)
            pins.analogWritePin(AnalogPin.P0, 0)
            basic.pause(2000)
        }
    } else if (sonar.ping(
    DigitalPin.P14,
    DigitalPin.P13,
    PingUnit.Centimeters
    ) > 5 && sonar.ping(
    DigitalPin.P14,
    DigitalPin.P13,
    PingUnit.Centimeters
    ) < 20) {
        pins.analogWritePin(AnalogPin.P0, 400)
    } else {
        pins.analogWritePin(AnalogPin.P0, 0)
    }
})
