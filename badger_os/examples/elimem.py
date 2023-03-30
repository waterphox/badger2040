import random
import time
import machine
import badger2040
from badger2040 import WIDTH, HEIGHT

d = badger2040.Badger2040()

#Easier names for reading button states.
btna = machine.Pin(badger2040.BUTTON_A, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnb = machine.Pin(badger2040.BUTTON_B, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnc = machine.Pin(badger2040.BUTTON_C, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnu = machine.Pin(badger2040.BUTTON_UP, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnd = machine.Pin(badger2040.BUTTON_DOWN, machine.Pin.IN, machine.Pin.PULL_DOWN)

try:
    squares = bytearray(open("support files/eliminationsquares.bin", "rb").read())
except (OSError, ImportError):
    machine.reset()
    pass #Reset this with a failure function that just says what the error is and says to reset

roundWinMsgs = ("Nice!",
                "Good job!",
                "You did the thing!",
                "Little faster now!",
                "Excellent!")
roundLoseMsgs = ("Wrong shape, buddy!",
                 "That wasn't it!",
                 "Not that one!",
                 "Oops! Try again!",
                 "Nope! >:C")

oldheartData = bytearray((
        0b00000000,0b00000000,
        0b00011100,0b00111000,
        0b00111110,0b01111100,
        0b01111111,0b11111110,
        0b01111111,0b11111110,
        0b01111111,0b11111110,
        0b01111111,0b11111110,
        0b00111111,0b11111100,
        0b00111111,0b11111100,
        0b00011111,0b11111000,
        0b00011111,0b11111000,
        0b00001111,0b11110000,
        0b00000111,0b11100000,
        0b00000011,0b11000000,
        0b00000001,0b10000000,
        0b00000000,0b00000000))

heartData =[
        "00000000","00000000",
        "00011100","00111000",
        "00111110","01111100",
        "01111111","11111110",
        "01111111","11111110",
        "01111111","11111110",
        "01111111","11111110",
        "00111111","11111100",
        "00111111","11111100",
        "00011111","11111000",
        "00011111","11111000",
        "00001111","11110000",
        "00000111","11100000",
        "00000011","11000000",
        "00000001","10000000",
        "00000000","00000000"]

#Left lines for columns, left to right
columns = (30, 136, 239, 268)

#Top lines for rows, top to bottom
rows = (19, 71, 100)

#Which squares are active. 0 is A, 1 B, 2 C, 3 DOWN, 4 UP
#Each spot has two squares. The first entry in the list is the
#square that is closest to the edge of the screen.
#I think I might mainly need this for the split corner piece but we'll see
activesquares = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
#activesquares = ([1, 1], [1, 1], [1, 1], [1, 1], [1, 1]) #was for testing

#What level are we on? Completing three rounds brings you to the next level.
level = 0
#Remember to add user button cheat to set level
#0 is easiest, 3 blocks
#1, 5 blocks
#2, 7 blocks
#3, 10 blocks

#What round of this level is it? You play each level for three rounds before moving forward.
#Each round gets slightly faster, from 1 second down to 0.1
gmround = 1
roundtimes = (0, 1.0, 0.4, 0.1)

#How many chances are left? You can only get three wrong!
lives = 4

#Just something to manage that pesky corner icon
corner = 0
#0 = both off, 1 = bottom triangle on, 2 = top tri on, 3 = both on
#Nevermind I ended up using the activesquares above for this, keeping here just in case though

#The current pattern, stored as a string of numbers 0 to 9 that represent each square
pattern = ""

#Are we currently listening for user input, should we start the next round
active = False
startround = True

#QuickRefs
#.text(Text, x, y, scale=1, rotation=0)
#.icon(data, index, sheetwidth, iconsizewh, x, y)
#.measure_text(text, scale)
#.image(data, width, height, x, y)
#.partial_update(x, y8, w, h8)
        
def eliminate_square(sq): #used ONLY to update a square to eliminated during gameplay
    #sq is the square to update
    #OLD 0 a1, 1 b1, 2 c1, 3 down1, 4 up1, 5 a2, 6 b2, 7 up2, 8 ctri2, 9 downtri2 THIS WAS PROBLEMATIC SO I REORDERED
    #0 a1, 1 b1, 2 c1, 3 down1, 4 up1, 5 a2, 6 b2, 7 ctri2, 8 downtri2, 9 up2
    d.led(200)
    d.set_update_speed(3)
    global activesquares
    if sq == 0: #a1
        activesquares[0][0] = 0
        d.icon(squares, 1, 144, 24, columns[0], rows[2])
        d.partial_update(columns[0], 96, 24, 32)
    elif sq == 1: #b1
        activesquares[1][0] = 0
        d.icon(squares, 1, 144, 24, columns[1], rows[2])
        d.partial_update(columns[1], 96, 24, 32)
    elif sq == 2: #c1
        activesquares[2][0] = 0
        d.icon(squares, 1, 144, 24, columns[2], rows[2])
        d.partial_update(columns[2], 96, 24, 32)
    elif sq == 3: #down1
        activesquares[3][0] = 0
        d.icon(squares, 1, 144, 24, columns[3], rows[1])
        d.partial_update(columns[3], 72, 24, 32)
    elif sq == 4: #up1
        activesquares[4][0] = 0
        d.icon(squares, 1, 144, 24, columns[3], rows[0])
        d.partial_update(columns[3], 16, 24, 32)
    elif sq == 5: #a2
        activesquares[0][1] = 0
        d.icon(squares, 1, 144, 24, columns[0], rows[1])
        d.partial_update(columns[0], 72, 24, 24)
    elif sq == 6: #b2
        activesquares[1][1] = 0
        d.icon(squares, 1, 144, 24, columns[1], rows[1])
        d.partial_update(columns[1], 72, 24, 24)
    elif sq == 9: #up2
        activesquares[4][1] = 0
        d.icon(squares, 1, 144, 24, columns[2], rows[0])
        d.partial_update(columns[2], 16, 24, 32)
    elif sq == 7: #ctri2
        activesquares[2][1] = 0
        if activesquares[3][1] == 1:
            d.icon(squares, 4, 144, 24, columns[2], rows[1])
        else:
            d.icon(squares, 5, 144, 24, columns[2], rows[1])
        d.partial_update(columns[2], 72, 24, 24)
    elif sq == 8: #downtri2
        activesquares[3][1] = 0
        if activesquares[2][1] == 1:
            d.icon(squares, 3, 144, 24, columns[2], rows[1])
        else:
            d.icon(squares, 5, 144, 24, columns[2], rows[1])
        d.partial_update(columns[2], 72, 24, 24)
    d.led(0)
    pass

def drawIcon(dats, wid, hig, ex, why): # Expects data (dats) to be an array of 8-character strings instead of a byte array IDK it's hackey
    bloop = ""
    for blorp in dats: # Okay I guess technically they don't need to be 8-character strings but that sure makes it easier to visualize
        bloop += blorp
    for row in range(hig):
        for col in range(wid):
            if bloop != "":
                if bloop[0] == "0":
                    d.set_pen(15)
                else:
                    d.set_pen(0)
                d.pixel(ex + col, why + row)
                bloop = bloop[1:]
                #print(bloop)
            

def activate_square(sq): #used ONLY to show a new square during gameplay
    #sq is the square to update
    #0 a1, 1 b1, 2 c1, 3 down1, 4 up1, 5 a2, 6 b2, 7 ctri2, 8 downtri2, 9 up2
    #d.led(220)
    d.set_update_speed(3)
    global activesquares
    if sq == 0: #a1
        activesquares[0][0] = 1
        d.icon(squares, 0, 144, 24, columns[0], rows[2])
        d.partial_update(columns[0], 96, 24, 32)
    elif sq == 1: #b1
        activesquares[1][0] = 1
        d.icon(squares, 0, 144, 24, columns[1], rows[2])
        d.partial_update(columns[1], 96, 24, 32)
    elif sq == 2: #c1
        activesquares[2][0] = 1
        d.icon(squares, 0, 144, 24, columns[2], rows[2])
        d.partial_update(columns[2], 96, 24, 32)
    elif sq == 3: #down1
        activesquares[3][0] = 1
        d.icon(squares, 0, 144, 24, columns[3], rows[1])
        d.partial_update(columns[3], 72, 24, 32)
    elif sq == 4: #up1
        activesquares[4][0] = 1
        d.icon(squares, 0, 144, 24, columns[3], rows[0])
        d.partial_update(columns[3], 16, 24, 32)
    elif sq == 5: #a2
        activesquares[0][1] = 1
        d.icon(squares, 0, 144, 24, columns[0], rows[1])
        d.partial_update(columns[0], 72, 24, 24)
    elif sq == 6: #b2
        activesquares[1][1] = 1
        d.icon(squares, 0, 144, 24, columns[1], rows[1])
        d.partial_update(columns[1], 72, 24, 24)
    elif sq == 9: #up2
        activesquares[4][1] = 1
        d.icon(squares, 0, 144, 24, columns[2], rows[0])
        d.partial_update(columns[2], 16, 24, 32)
    elif sq == 7: #ctri2
        activesquares[2][1] = 1
        if activesquares[3][1] == 1:
            d.icon(squares, 2, 144, 24, columns[2], rows[1])
        else:
            d.icon(squares, 3, 144, 24, columns[2], rows[1])
        d.partial_update(columns[2], 72, 24, 24)
    elif sq == 8: #downtri2
        activesquares[3][1] = 1
        if activesquares[2][1] == 1:
            d.icon(squares, 2, 144, 24, columns[2], rows[1])
        else:
            d.icon(squares, 4, 144, 24, columns[2], rows[1])
        d.partial_update(columns[2], 72, 24, 24)
    d.led(0)
    pass

def countdown(): #Counts down from 3 to WATCH, then triggers whatever function is next to show the pattern
    d.set_update_speed(3)
    d.set_pen(0)
    d.set_thickness(3)
    d.set_font("sans")
    d.text("3..", 10, 55, scale=0.7)
    d.partial_update(10, 40, 30, 24) #Update 3 to dark
    time.sleep(roundtimes[gmround])
    d.text("2..", 40, 55, scale=0.7)
    d.set_pen(8)
    d.text("3..", 10, 55, scale=0.7)
    d.partial_update(10, 40, 60, 24) #Update 3 to light, 2 to dark
    time.sleep(roundtimes[gmround])
    d.text("2..", 40, 55, scale=0.7)
    d.set_pen(0)
    d.text("1..", 70, 55, scale=0.7)
    d.partial_update(40, 40, 60, 24) #Update 2 to light, 1 to dark
    time.sleep(roundtimes[gmround])
    d.text("WATCH", 105, 55, scale=0.7)
    d.set_pen(8)
    d.text("1..", 70, 55, scale=0.7)
    d.partial_update(40, 40, 133, 24) #Update 1 to light, WATCH to dark
    time.sleep(roundtimes[gmround])
    generate_pattern() #Countdown complete. Time to watch the squares
    pass

def generate_pattern(): #Generates the pattern to be remembered, and activates those blocks on screen as it does so
    global pattern, activesquares, active
    activesquares = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
    pattern = ""
    if level == 0:
        total = 3
    elif level == 1:
        total = 5
    elif level == 2:
        total = 7
    elif level == 3:
        total = 10
    for i in range(0, total):
        while True:
            new = random.randint(0, 4)
            if activesquares[new][0] == 1 and level > 1:
                new = new + 5
            newstr = str(new)
            print("Candidate Number: " + newstr)
            if newstr not in pattern:
                print("Number accepted.")
                global pattern
                pattern = pattern + newstr
                activate_square(new)
                #print(activesquares)
                time.sleep(roundtimes[gmround])
                break
            else:
                print("Same number, trying again.")
                continue
    print("Pattern: " + pattern)
    time.sleep(roundtimes[gmround])
    d.set_pen(8)
    d.text("WATCH", 105, 55, scale=0.7)
    d.set_pen(0)
    d.text("GO!", 185, 55, scale=0.7)
    d.partial_update(105, 40, 115, 24) #Update WATCH to light, GO! to dark
    active = True
    pass

def show_result(result):
    d.set_update_speed(3)
    d.set_pen(15) #White pen for the outline
    d.rectangle(0, 0, WIDTH, HEIGHT)
    #display.text(result, int(WIDTH / 2) - int(display.measure_text(result) / 2), int(HEIGHT / 2))
    d.set_thickness(2)
    d.set_pen(0)
    d.text(result, int(WIDTH / 2) - int(d.measure_text(result, 0.5) / 2), int(HEIGHT / 2), scale=0.5)
    d.update()
    pass

def drawstaticui():
    d.set_update_speed(badger2040.UPDATE_FAST)
    d.led(255)
    d.set_pen(15)
    d.rectangle(0, 0, WIDTH, HEIGHT)
    d.set_pen(0) #Black pen
    d.set_thickness(2) #2px line
    d.set_font("sans")
    d.text("eliminate the shapes in", 10, 10, scale=0.6)
    d.text("the order they appear!", 10, 32, scale=0.6)
    d.set_thickness(2) #1px line for the diagonal bar for corner squares
    d.line(231, 63, WIDTH, HEIGHT) #Said bar 231 63 to bottom right corner
    
    #Level Text
    d.set_font("serif")
    d.set_thickness(3)
    levelmid = int((columns[1] + columns[0]) / 2) + 12
    lvlmid = int(levelmid - d.measure_text("LVL", 0.8) / 2)
    lvltmid = int(levelmid - d.measure_text(str(level), 0.8) / 2)
    d.text("LVL", lvlmid, 88, scale=0.8) #66, 84
    d.text(str(level), lvltmid, 110, scale=0.8)
    
    #Draws the hearts/lives/chances
    d.led(220)
    d.set_thickness(2)
    d.set_font("serif")
    d.text("LIVES", 177, 80, scale=0.5)
    for i in range(1, lives + 1):
        drawIcon(heartData, 16, 16, 231 - i * 16, 89)
        pass
    
    #Round Text
    levelmid = int((columns[2] + columns[1]) / 2) + 12
    lvlmid = int(levelmid - d.measure_text("ROUND", 0.5) / 2)
    lvltmid = int(levelmid - d.measure_text(str(gmround), 1) / 2)
    d.text("ROUND", lvlmid, 110, scale=0.5) #66, 84
    d.text(str(gmround), lvltmid, 123, scale=0.5)
    
    #Initial Countdown Text
    d.set_font("sans")
    d.set_thickness(3)
    d.set_pen(8)
    d.text("3..", 10, 55, scale=0.7)
    d.text("2..", 40, 55, scale=0.7)
    d.text("1..", 70, 55, scale=0.7)
    d.text("WATCH", 105, 55, scale=0.7)
    d.text("GO!", 185, 55, scale=0.7)
    
    d.update()
    d.led(0)
    pass
        
def nextround(wl): #Just a quick function to set us up for the next round. (or declare a total win)
    global level, gmround, lives, active, startround
    active = False
    if wl == "win": #We won the round!
        if gmround == 3: #If they are on the last round of the level
            if level == 3: #and it was the last level
                show_result("You won remembering! Bye!")
                time.sleep(3)
                machine.reset() #replace with another prompt?
            else: #This is not the last round of level 3
                show_result("Level up!")
                time.sleep(3)
                level = level + 1
                gmround = 1
        else: #This is not round 3
            show_result(random.choice(roundWinMsgs))
            time.sleep(3)
            gmround = gmround + 1
    else: #We lost the round
        if lives == 1: #This was our last life
            show_result("You died.")
            time.sleep(3)
            machine.reset() #replace with another prompt?
        else: #This was not our last life
            show_result(random.choice(roundLoseMsgs))
            lives = lives - 1
            time.sleep(3)
    #drawstaticui() #Redraw interface with new level/round data
    #countdown() #Start countdown for next round!
    #Removed the above so we'd kick out to the main loop instead
    startround = True
    pass

#Main loop
while True:
    if startround:
        startround = False
        drawstaticui()
        countdown()
    #0 a1, 1 b1, 2 c1, 3 down1, 4 up1, 5 a2, 6 b2, 7 ctri2, 8 downtri2, 9 up2
    if active:
        if btna.value():
            if activesquares[0][1] == 1 and pattern[0] == "5": #If the second A square is active and is the next in the pattern
                pattern = pattern.strip(pattern[0])
                eliminate_square(5)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            elif activesquares[0][0] == 1 and pattern[0] == "0": #If the first A square is active and is the next in the pattern
                pattern = pattern.strip(pattern[0])
                eliminate_square(0)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            else: #Neither of the above was true, so you lose the round
                nextround("lose")
        if btnb.value():
            if activesquares[1][1] == 1 and pattern[0] == "6":
                pattern = pattern.strip(pattern[0])
                eliminate_square(6)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            elif activesquares[1][0] == 1 and pattern[0] == "1": 
                pattern = pattern.strip(pattern[0])
                eliminate_square(1)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            else: #Neither of the above was true, so you lose the round
                nextround("lose")
        if btnc.value():
            if activesquares[2][1] == 1 and pattern[0] == "7":
                pattern = pattern.strip(pattern[0])
                eliminate_square(7)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            elif activesquares[2][0] == 1 and pattern[0] == "2": 
                pattern = pattern.strip(pattern[0])
                eliminate_square(2)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            else: #Neither of the above was true, so you lose the round
                nextround("lose")
        if btnd.value():
            if activesquares[3][1] == 1 and pattern[0] == "8":
                pattern = pattern.strip(pattern[0])
                eliminate_square(8)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            elif activesquares[3][0] == 1 and pattern[0] == "3": 
                pattern = pattern.strip(pattern[0])
                eliminate_square(3)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            else: #Neither of the above was true, so you lose the round
                nextround("lose")
        if btnu.value():
            if activesquares[4][1] == 1 and pattern[0] == "9": 
                pattern = pattern.strip(pattern[0])
                eliminate_square(9)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            elif activesquares[4][0] == 1 and pattern[0] == "4": 
                pattern = pattern.strip(pattern[0])
                eliminate_square(4)
                if pattern == "": #That was the last block and we have no more
                    nextround("win")
            else: #Neither of the above was true, so you lose the round
                nextround("lose")
        pass
    time.sleep(0.01)
    pass