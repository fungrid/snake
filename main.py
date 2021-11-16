def sneka(x: number, y: number):
    indeks = 0
    while indeks <= len(X):
        if X[indeks] == x and Y[indeks] == y:
            return 1
        indeks += 1
    return 0

def on_button_pressed_a():
    global State, R, B
    if State == 0:
        State = 1
        led.stop_animation()
        led.plot_brightness(HX, HY, 128)
        led.plot_brightness(EX, EY, 255)
    else:
        if B == 0:
            R = R - 1
        B = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global R, B
    if B == 0:
        R = R + 1
    B = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

EY = 0
State = 0
EX = 0
B = 0
R = 0
Y: List[number] = []
X: List[number] = []
HY = 0
HX = 0
HX = -1
HY = 1
X = [-1]
Y = [2]
R = 1
B = 0
EX = randint(1, 4)
State = 0
EY = randint(3, 4)

def on_every_interval():
    global R, HX, HY, EX, EY, B
    if State == 1:
        if R < 0:
            R = 3
        R = R % 4
        if R == 1:
            HX = HX + 1
        elif R == 2:
            HY = HY + 1
        elif R == 3:
            HX = HX - 1
        else:
            HY = HY - 1
        if HX < 0:
            HX = 4
        HX = HX % 5
        if HY < 0:
            HY = 4
        X.append(HX)
        Y.append(HY)
        if EY == HY and EX == HX:
            while EY == HY and EX == HX:
                EX = randint(0, 4)
                EY = randint(0, 4)
                led.plot_brightness(EX, EY, 255)
        else:
            led.unplot(X.shift(), Y.shift())
        led.plot_brightness(HX, HY, 128)
        B = 0
        HY = HY % 5
loops.every_interval(1000, on_every_interval)

def on_forever():
    if State == 0:
        basic.show_string("Sneka")
basic.forever(on_forever)
