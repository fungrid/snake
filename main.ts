input.onButtonPressed(Button.A, function () {
    if (B == 0) {
        R = R - 1
    }
    B = 1
})
input.onButtonPressed(Button.B, function () {
    if (B == 0) {
        R = R + 1
    }
    B = 1
})
let B = 0
let R = 0
let HX = -1
let HY = 1
let X = [-1]
let Y = [2]
R = 1
B = 0
led.plotBrightness(HX, HY, 128)
led.plotBrightness(3, 3, 255)
loops.everyInterval(1000, function () {
    led.unplot(HX, HY)
    if (R < 0) {
        R = 3
    }
    R = R % 4
    if (R == 1) {
        HX = HX + 1
    } else if (R == 2) {
        HY = HY + 1
    } else if (R == 3) {
        HX = HX - 1
    } else {
        HY = HY - 1
    }
    if (HX < 0) {
        HX = 4
    }
    HX = HX % 5
    if (HY < 0) {
        HY = 4
    }
    HY = HY % 5
    X.push(HX)
    Y.push(HY)
    led.plotBrightness(HX, HY, 128)
    B = 0
})
basic.forever(function () {
	
})
