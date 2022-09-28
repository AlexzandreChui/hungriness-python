from microbit import*

# Created By: Alex.C
# Created On: 2022/09/28
# This block of code tells the microbit to set the counter to 0 on start.
hungryness = 0
# Created By: Alex.C
# Created On: 2022/09/28
# This block of code tells the microbit to change the counter by 1 when the A button is pressed and set the counter back to 0 when the B button is pressed. 

def on_forever():
    global hungryness
    if input.button_a_is_pressed(True):
        hungryness = hungryness + 1
        basic.show_number(hungryness)
    elif input.button_b_is_pressed(True):
        hungryness = 0
        basic.show_number(hungryness)
basic.forever(on_forever)
