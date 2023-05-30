# This example reaches out to my server at boop.pw so I can learn how to make web requests

# Imports
import badger2040
from badger2040 import WIDTH, HEIGHT
import urequests
import machine
import badger_os

urlCount = "https://boop.pw/count"
urlBase = "https://boop.pw"

# Display Setup
badger = badger2040.Badger2040()
badger.led(128)


# Setup buttons
btnA = machine.Pin(badger2040.BUTTON_A, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(badger2040.BUTTON_B, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnC = machine.Pin(badger2040.BUTTON_C, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnD = machine.Pin(badger2040.BUTTON_DOWN, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnU = machine.Pin(badger2040.BUTTON_UP, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Approximate center lines for buttons A, B and C - Menu Text - Manu Text Size - change global
centers = (41, 147, 253)
btnlabels = ["EXIT", "", "Boop"]
btnlabelsize = 0.8
change = False

# Connects to the wireless network. Ensure you have entered your details in WIFI_CONFIG.py :)
badger.connect()
badger.set_update_speed(3)

def getBoop(new = False):
    global boopCount
    if new:
        req = urequests.head(urlBase)
    print(f"Requesting URL: {urlCount}")
    req = urequests.get(urlCount)
    # open the response content
    boopCount = req.text
    print(boopCount)

    req.close()

def drawMenu(booping = False):
    badger.set_pen(15)
    badger.rectangle(0, HEIGHT - 25, WIDTH, 25)
    badger.set_pen(0)
    badger.set_font("sans")
    badger.set_thickness(2)
    badger.line(0, HEIGHT - 25, WIDTH, HEIGHT - 25, 2)
    if booping == True:
        btnlabels[2] = "Booping"
    else:
        btnlabels[2] = "Boop"
    for x in range(0, 3):
        if booping == True:
            if x == 2:
                badger.text(btnlabels[x], centers[x] - int(badger.measure_text(btnlabels[x], btnlabelsize) / 2) - 5, HEIGHT - 11, scale=btnlabelsize)
        else:
            badger.text(btnlabels[x], centers[x] - int(badger.measure_text(btnlabels[x], btnlabelsize) / 2), HEIGHT - 11, scale=btnlabelsize)

def drawPage(booping = False):
    # Clear the display
    badger.set_pen(15)
    badger.clear()
    badger.set_pen(0)

    # Draw the page header
    badger.set_font("bitmap6")
    badger.set_pen(0)
    badger.rectangle(0, 0, WIDTH, 20)
    badger.set_pen(15)
    badger.text("Boop Count", 3, 4)
    badger.set_pen(0)
    badger.set_font("bitmap8")
    if booping == False:
        badger.text("Loading Boops", int(WIDTH / 4), 28, WIDTH - 105, 4)
    drawMenu()
    if booping == False:
        badger.update()
    getBoop()
    drawBoop()

def drawBoop():
    badger.set_font("bitmap8")
    badger.set_pen(15)
    badger.rectangle(0, 21, WIDTH, HEIGHT - 50)
    badger.set_pen(0)
    if boopCount is not None:
        badger.text(boopCount, int(WIDTH / 3), 28, WIDTH - 105, 4)
    else:
        badger.rectangle(0, 60, WIDTH, 25)
        badger.set_pen(15)
        badger.text("Unable to get boops! Check your network settings in WIFI_CONFIG.py", 5, 65, WIDTH, 1)
    badger.update()

drawPage()

# Button Loop
while True:
    change = False
    if btnC.value():
        drawMenu(True)
        badger.update()
        getBoop(True)
        drawPage(True)
    if btnA.value(): # This works best on battery. On USB it just exits the script.
        badger_os.state_clear_running()
        badger2040.reset_pressed_to_wake()
        machine.soft_reset()
    #badger.halt()
