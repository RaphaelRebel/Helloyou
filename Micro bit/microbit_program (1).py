from microbit import *
LOLLY = Image("09990:"
             "09990:"
             "09990:"
             "00900:"
             "00900")


display.scroll("HELLO YOU!")
while True:
    if button_a.is_pressed():
        display.scroll("RAPHAEL REBEL")
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.scroll("LOLLY")
        display.show(LOLLY)