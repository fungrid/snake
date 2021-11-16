function sneka (x: number, y: number) {
    while (indeks <= X.length) {
        if (X[indeks] == x && Y[indeks] == y) {
            return 1
        }
        indeks += 1
    }
    return 0
}
input.onButtonPressed(Button.A, function () {
    if (State == 0) {
        State = 1
        led.stopAnimation()
        led.plotBrightness(HX, HY, 128)
        led.plotBrightness(EX, EY, 255)
    } else {
        if (B == 0) {
            R = R - 1
        }
        B = 1
    }
})
input.onButtonPressed(Button.B, function () {
    if (B == 0) {
        R = R + 1
    }
    B = 1
})
let indeks = 0
let EY = 0
let State = 0
let EX = 0
let B = 0
let R = 0
let Y: number[] = []
let X: number[] = []
let HY = 0
let HX = 0
HX = -1
HY = 1
X = [-1]
Y = [2]
R = 1
B = 0
EX = randint(1, 4)
State = 0
EY = randint(3, 4)
loops.everyInterval(1000, function () {
    if (State == 1) {
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
        X.push(HX)
        Y.push(HY)
        if (EY == HY && EX == HX) {
            while (EY == HY && EX == HX) {
                EX = randint(0, 4)
                EY = randint(0, 4)
                led.plotBrightness(EX, EY, 255)
            }
        } else {
            led.unplot(X.shift(), Y.shift())
        }
        led.plotBrightness(HX, HY, 128)
        B = 0
        HY = HY % 5
    }
})
basic.forever(function () {
    if (State == 0) {
        basic.showString("Sneka")
    }
})
