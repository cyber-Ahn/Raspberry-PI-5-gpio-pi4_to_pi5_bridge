import gpiod

mod = "BOARD"
chip = gpiod.Chip('gpiochip4')

def BCM():
    print("BCM")
def BOARD():
    print("BOARD")
def OUT():
    print("OUT")
def IN():
    print("IN")
def LOW():
    print("LOW")
def HIGH():
    print("HIGH")
def PUD_DOWN():
    print("PUD_DOWN")
def setwarnings(warn):
    print("Warnings: " + str(warn))

def setmode(modus):
    global mod
    mod = str(modus).split(" ")[1]

def gpio_map(num):
    if mod == "BCM":
        return num
    elif mod == "BOARD":
        map_A = ["0","1","3","5","7","29","31","26","24","21","19","23","32","33","8","10","36","11","12","35","38","40","15","16","18","22","37","13"]
        return int(map_A.index(str(num)))

def setup(pin_n, setto, pull_up_down = "x"):
    pin_n = gpio_map(pin_n)
    setto = str(setto).split(" ")[1]
    if setto == "OUT":
        chip.get_line(pin_n).request(consumer="myLed", type=gpiod.LINE_REQ_DIR_OUT)
    elif setto == "IN":
        chip.get_line(pin_n).request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

def output(pin_n, stat):
    pin_n = gpio_map(pin_n)
    stat = str(stat).split(" ")[1]
    if stat == "HIGH":
        chip.get_line(pin_n).set_value(1)
    elif stat == "LOW":
        chip.get_line(pin_n).set_value(0)

def input(pin_n):
    pin_n = gpio_map(pin_n)
    val = chip.get_line(pin_n).get_value()
    if val == 1:
        return HIGH
    else:
        return LOW
