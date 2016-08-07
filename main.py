import ugfx
import pyb
import buttons

def displayImage(path):
	ugfx.display_image(0,0, path)

ugfx.area(0, 0, 320, 240, 0x0000)

buttons.init()

while not buttons.is_pressed("BTN_MENU"):
	displayImage('apps/daniellog~jeffgoldblum/jeff-goldblum.gif')
