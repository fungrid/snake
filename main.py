def on_button_pressed_a():
    global R, B
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

B = 0
R = 0
HX = -1
HY = 2
X = [-1]
Y = [2]
R = 1
B = 0
led.plot_brightness(HX, HY, 128)

def on_every_interval():
    global R, HX, HY, B
    led.unplot(HX, HY)
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
    HY = HY % 5
    X.append(HX)
    Y.append(HY)
    led.plot_brightness(HX, HY, 128)
    B = 0
loops.every_interval(1000, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
