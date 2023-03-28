# generate the fursona of your dreams
# originally by softhoof - http://www.generatorland.com/usergenerator.aspx?id=7427

import badger2040
import gc
import os
import badger_os
import time
import math
import random
import machine
from badger2040 import WIDTH, HEIGHT

# Content, baby!
adjective = ("eldritch","neon green","angelic","ghostly","scene","emo","hipster","alien","sweaty","OBSCENELY BRIGHT YELLOW","spotted","hairy","glowing","pastel pink","glittering blue","golden","shimmering red","robotic","black","goth","elegant","white","divine","striped","radioactive","red and green","slimy","slime","garbage","albino","skeleton","petite","swamp","aquatic","vampire","bright pink and yellow","mossy","stone","gray","fairy","zombie","pastel","mint green","giant","big pink","tiny pink","big white","tiny white","tiny black","translucent","glistening","glittering black","shimmering white","iridescent","glass","silver","jewel-encrusted","fuschia","purple","tiny purple","lilac","lavender","shimmering lilac","sparkling purple","tiny blue","heavenly","gilded","holy","blue and white striped","black and orange spotted","black and red","black and orange","ancient","green","purple and blue","pink and blue","candy","abyssal","floral","candle","melanistic","punk","ethereal","unholy","celestial","cyan","cream","cream and pink","cream and brown","yellow","black and pink","magenta","speckled","tiger-striped","chocolate","pastel goth","vintage","glossy black","glossy white","glossy gray","glossy blue","glossy pink","shimmery gray","glossy yellow","magma","plastic","leucistic","piebald","wooden")
species = ("kestrel","goat","sheep","dragon","platypus","blobfish","hydra","wolf","fox","sparkledog","cow","bull","cat","tiger","panther","hellhound","spider","beagle","pomeranian","whale","hammerhead shark","snake","hyena","lamb","pony","horse","pup","swan","pigeon","dove","fennec fox","fish","rat","possum","hamster","deer","elk","reindeer","cheetah","ferret","bear","panda","koala","kangaroo","skink","lizard","iguana","cerberus","turtle","raven","cardinal","bluejay","antelope","buffalo","rabbit","bunny","frog","newt","salamander","cobra","coyote","jellyfish","bee","wasp","dinosaur","bat","worm","chicken","eel","tiger","sloth","seal","vulture","barghest","hedgehog","peacock","anglerfish","dolphin","liger","llama","alpaca","walrus","mantis","ladybug","set_penguin","flamingo","civet","pudu","crab","maine coon","fawn","siamese","amoeba","owl","unicorn","crocodile","alligator","chihuahua","great dane","dachshund","corgi","rooster","sparrow","wyrm","slug","snail","seagull","badger","gargoyle","scorpion","boa","axolotl", "kobold", "sergal", "synth", "protogen", "otter", "shiba inu", "fennix", "rexouium", "crux", "pikachu", "renamon", "hobkin", "impim", "red panda", "boar")
description = ("it constantly drips with a tar-like black substance.","it enjoys performing occult rituals with friends.","it is a communist.","a golden halo floats above its head.","it wears a mcdonalds uniform because it works at mcdonalds.","it carries a nail bat.","it wears louboutin heels.","it has two heads.","it has an unknowable amount of eyes.","it drools constantly.","its tongue is bright green.","it has numerous piercings.","it is a cheerleader.","it is a farmhand.","when you see it you are filled with an ancient fear.","it wears a toga.","it is made of jelly.","it has incredibly long and luxurious fur.","it uses reddit but won't admit it.","it glows softly and gently- evidence of a heavenly being.","it is a ghost.","it dresses like a greaser.","crystals grow from its flesh.","it rides motorcycles.","it wears incredibly large and impractical sunglasses.","it instagrams its starbucks drinks.","it is a hired killer.","where its tail should be is just another head.","it dwells in a bog.","it is wet and dripping with algae.","it runs a blog dedicated to different types of planes throughout history.","it worships the moon.","it comes from a long line of royalty.","it frolics in flowery meadows.","it wears a ballerina's outfit.","it wears a neutral milk hotel t-shirt with red fishnets and nothing else.","it wears a lot of eye makeup.","it won't stop sweating.","it has far too many teeth and they are all sharp.","it is a tattoo artist.","it is shaking.","it is a witch.","it wears scarves all the time.","to look into its eyes is to peer into a distant abyss.","mushrooms grow from its skin.","its face is actually an electronic screen.","it loves to wear combat boots with cute stickers all over them.","it comes from space.","it is a knife collector.","it flickers in and out of this plane of reality.","it wishes it were a cloud.","its eyes are red.","it is the most beautiful thing you have ever seen.","it loves strawberry milkshakes.","it cries all the time and can't really do much about it.","it lives alone in a dense forgotten wilderness.","it wears big christmas sweaters year-round.","it floats about a foot off of the ground.","it loves trash.","it has demonic wings.","it has a cutie mark of a bar of soap.","it is melting.","it wears opulent jewelry of gold and gemstones.","it has a hoard of bones.","it has ram horns.","it has a forked tongue.","it wears frilly dresses.","it has antlers.","it is a nature spirit.","its back is covered in candles which flicker ominously.","it wears a leather jacket with lots of patches.","it wears a snapback.","it has a tattoo that says 'yolo'.","electricity flickers through the air surrounding it.","it is a fire elemental.","it consumes only blood.","it works at an adorable tiny bakery.","it is a professional wrestler.","instead of eyes there are just more ears.","it speaks a forgotten and ancient language both disturbing and enchanting to mortal ears.","it works out.","it wishes it were a tree.","it is always blushing.","it uses ancient and powerful magic.","it loves raw meat.","it is always smiling.","it can fire lasers from its eyes.","a small raincloud follows it everywhere.","it is made of glass.","fireflies circle it constantly.","it is always accompanied by glowing orbs of light.","it has human legs.","water drips from it constantly.","it has golden horns.","it loves gore.","it lives in a cave with its parents.","its purse costs more than most people's cars.","it always shivers even when it's not cold.","it has tentacles.","it never blinks.","it only listens to metal.","it wears a golden crown.","it wears a white sundress.","it has green hair pulled up into two buns.","its body is covered in occult sigils and runes which pulse ominously.","it loves to devour the rotting plant matter covering the forest floor.","it wears a plain white mask.","its eyes flash multiple colors rapidly.","it loves to wear nail polish but applies it messily.","it runs a jimmy carter fanblog.","it is a surfer.","it only wears hawaiian shirts.","everything it wears is made out of denim.","it has long braided hair.","it calls everybody comrade.","it lures men to their deaths with its beautiful voice.","it has braces.","it has full sleeve tattoos.","it dresses like a grandpa.","smoke pours from its mouth.","it is a makeup artist.","it dresses like a pinup girl.","it has only one large eye.","it plays the harp.","it has very long hair with many flowers in it.","it has a cyan buzzcut.","it is a garden spirit.","it has fangs capable of injecting venom.","numerous eyeballs float around it. watching. waiting.","it loves to play in the mud.","it wears a surgical mask.","its eyes are pitch black and cause those who look directly into them for too long to slowly grow older.","it wears numerous cute hairclips.","it has a very large tattoo of the 'blockbuster' logo.","it is constantly covered in honey that drips on everything and pools beneath it.","it wears a cherry-themed outfit.","it has heterochromia.","it is heavily scarred.","in place of a head it has a floating cube that glows and pulses softly.","it seems to be glitching.","it does not have organs- instead it is full of flowers.","its insides are glowing.","it is a skateboarder.","it is a superwholock blogger.","it is a skilled glass-blower.","it has a pet of the same species as itself.","it is the leader of an association of villains.","it wears a black leather outfit.","its pupils are slits.","it wears a crop top with the word OATMEAL in all caps.","it only wears crop tops and high waisted shorts.","it is always giving everyone a suspicious look.","it has a septum piercing.","instead of talking it just says numbers.","it is an internet famous scene queen.","its eyes are way too big to be normal.","it has super obvious tan lines.","it wears a maid outfit.","it is an emissary from hell.","its eyes have multiple pupils in them.","it has an impractically large sword.","it is a magical girl.","it has a scorpion tail.","it is a biologist specializing in marine invertebrates.","it runs. everywhere. all the time.","it is an esteemed fashion designer for beings with 6 or more limbs.","it wears short shorts that say CLAM.","it can't stop knitting.","it is always coated in glitter.","it worships powerful dolphin deities.","it has slicked back hair.","it has a thick beard.","it has a long braided beard plaited with ribbons.","it is a viking.","it wears a parka.","its outfit is completely holographic.","it wears an oversized pearl necklace.","it has stubble.","it carries a cellphone with a ridiculous amount of charms and keychains.","it wears crocs.","it has a hoard of gems and gold that was pillaged from innocent villagers.","it robs banks.","its facial features are constantly shifting.","it works as a librarian in hell.","it wears a fedora.","it is made of petrified wood.")
# New content needs to be added. species and adjectives should be merged in to species and colors

badger = badger2040.Badger2040()
display = badger

fursonasavefile = "output files/fursonasfile.txt" # Full path including any directories. The file will be created if it does not exist.

font_size = 2
inverted = False
fursonas = ["BEGINNING OF LIST", "END OF LIST"]
currentFurre = 0
menupage = 0
furdrawspeed = 2
o3ostate = 0

font_sizes = (0.5, 0.7, 0.9)

OVERLAY_BORDER = 40
OVERLAY_SPACING = 20
OVERLAY_TEXT_SIZE = 0.5

# Approximate center lines for buttons A, B and C
centers = (41, 147, 253)
btnlabels = (("MENU", "RE-DRAW", "GENERATE!!"),
             ("MENU", "SAVE", "SPEED"),
             ("MENU", "o3o", "CREDIT"),
             ("YES", "", "NO"))
btnlabelsize = 0.6

button_a = badger2040.BUTTON_A
button_b = badger2040.BUTTON_B
button_c = badger2040.BUTTON_C
button_up = badger2040.BUTTON_UP
button_down = badger2040.BUTTON_DOWN

# Set the global or initial font
display.set_font("sans")

# Renders the initial screen before any stuff happens, like a button press
def render(menuonly=0):
    if menuonly == 1:
        draw_menu()
        display.partial_update(int(WIDTH / 3), 112, WIDTH - int(WIDTH / 3), 16)
    else:
        global currentFurre
        memory = str(gc.mem_free())
        memtextpos = WIDTH - display.measure_text(memory, 0.4)
        badger.led(255)
        display.set_pen(0)
        display.rectangle(0, 0, WIDTH, 16)
        display.set_thickness(1)
        display.set_pen(15)
        display.text("generate the fursona of your dreams", 3, 8, scale=0.4)
        draw_menu()
        display.set_pen(15)
        display.set_thickness(1)
        display.text(memory, memtextpos, 8, scale=0.4)
        if len(fursonas) == 2:
            display.rectangle(0, 16, WIDTH, 93)
        else:
            drawThatFursona()
        display.update()
    badger.led(0)

def draw_menu():
    display.set_pen(15)
    display.rectangle(0, 111, WIDTH, HEIGHT)
    display.set_thickness(2)
    display.set_pen(0)
    display.line(0, 110, WIDTH, 110)
    for x in range(0, 3):
        display.text(btnlabels[menupage][x], centers[x] - int(display.measure_text(btnlabels[menupage][x], btnlabelsize) / 2), 122, scale=btnlabelsize)
    

# Draw an overlay box with a given message within it
def draw_overlay(message, width, height, line_spacing, text_size):
    # Draw a light grey background
    display.set_pen(14)
    display.rectangle((WIDTH - width) // 2, (HEIGHT - height) // 2, width, height)

    # Take the provided message and split it up into
    # lines that fit within the specified width
    words = message.split(" ")

    lines = []
    current_line = ""
    for word in words:
        if display.measure_text(current_line + word + " ", text_size) < width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())

    display.set_pen(0)
    display.set_thickness(2)

    # Display each line of text from the message, centre-aligned
    num_lines = len(lines)
    for i in range(num_lines):
        length = display.measure_text(lines[i], text_size)
        current_line = (i * line_spacing) - ((num_lines - 1) * line_spacing) // 2
        display.text(lines[i], (WIDTH - length) // 2, (HEIGHT // 2) + current_line, scale=text_size)

def drawThatFursona(override=""):
    display.set_pen(15)
    display.rectangle(0, 16, WIDTH, 93)
    if override != "":
        words = override.split(" ")
    else:
        if currentFurre == len(fursonas) - 1:
            words = fursonas[currentFurre].split(" ")
        elif currentFurre == 0:
            words = fursonas[currentFurre].split(" ")
        else:
            words = (str(currentFurre) + ": " + fursonas[currentFurre]).split(" ")
    line_spacing = 20
    lines = []
    current_line = ""
    for word in words:
        if display.measure_text(current_line + word + " ", 0.6) < WIDTH:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())

    display.set_pen(0)
    display.set_thickness(2)

    # Display each line of text from the message, centre-aligned
    num_lines = len(lines)
    for i in range(num_lines):
        length = display.measure_text(lines[i], 0.6)
        current_line = (i * line_spacing) - ((num_lines - 1) * line_spacing) // 2
        display.text(lines[i], (WIDTH - length) // 2, (HEIGHT // 2) + current_line, scale=0.6)

def generateFursona():
    global currentFurre
    fursonas.insert(len(fursonas) - 1, random.choice(adjective) + " " + random.choice(species) + ". " + random.choice(description))
    currentFurre = len(fursonas) - 2

def button(pin):
    global menupage, font_size, inverted, currentFurre, furdrawspeed, o3ostate
    badger.led(255)
    if pin == button_a:     # This button switches between menu options, and ALWAYS says Menu
        o3ostate = 0
        if menupage == 0:   # MENU, RE-DRAW, GENERATE!
            menupage = 1
        elif menupage == 1: # MENU, SAVE, SPEED
            menupage = 2
        else:               # MENU, o3o, CREDIT
            menupage = 0
        display.set_update_speed(3)
        render(1)
    if pin == button_b:
        if menupage == 0:   # RE-DRAW
            display.set_update_speed(3)
            render()
        elif menupage == 1: # SAVE
            if len(fursonas) == 2:                         # Checks that we've even generated one yet.
                drawThatFursona("You have to generate one, first!")
            else:                                          # We've generated at least one fursona already.
                if currentFurre == 0 or currentFurre == len(fursonas) - 1: # Checks against the Beginning/End messages being shown
                    drawThatFursona("That's not a fursona!")
                else:                                      # We're actually viewing a fursona
                    furfile = open(fursonasavefile, "a")   # Opens the existing file in append mode, or creates the file if it doesn't exist.
                    savefurcount = furfile.readlines()     # Checks how many furres are in the file alreadygoo
                    if str(savefurcount).find(str(fursonas[currentFurre])) != -1: #Confirming furre doesn't already exist in the file
                        drawThatFursona("Furre already saved in file!")
                    else:
                        furfile.seek(0, 2)                     # Seeks to the end of the file.
                        furfile.write(fursonas[currentFurre] + '\n')  # Writes the current fursona to the file!
                        drawThatFursona("Done! Fursonas in file: " + str(len(savefurcount) + 1))
                    furfile.close()
            display.set_update_speed(3)
            display.update()                               # After all that, show whatever message is relevant based on what happened.
            time.sleep(1)
            drawThatFursona()
            render()
            display.update()
        else:               # o3o Menu Option
            display.set_update_speed(1)
            currentFurre = len(fursonas) - 1  # This is just so the Save button won't work when a o3o message is on the screen
            if o3ostate == 0:
                drawThatFursona("It looks like a blue fox! o3o")
                o3ostate = 1
            elif o3ostate == 1:
                drawThatFursona("o3o to you too, buddy")
                o3ostate = 2
            elif o3ostate == 2:
                drawThatFursona("Stop pressing that! It doesn't do anything.")
                o3ostate = 3
            else:
                drawThatFursona("Forget this, I'm resetting.")
                o3ostate = 0
            display.update()
    if pin == button_c:
        o3ostate = 0
        if menupage == 0:   # GENERATE!
            generateFursona()
            display.set_update_speed(furdrawspeed)
            render()
        elif menupage == 1: # SPEED
            display.set_pen(15)
            display.rectangle(int(WIDTH /3) * 2, 112, WIDTH - int(WIDTH / 3) * 2, 16)
            display.set_pen(0)
            if furdrawspeed == 0:
                furdrawspeed = 1
                display.text("MEDIUM", centers[2] - int(display.measure_text("MEDIUM", btnlabelsize) / 2), 122, scale=btnlabelsize)
            elif furdrawspeed == 1:
                furdrawspeed = 2
                display.text("FAST", centers[2] - int(display.measure_text("FAST", btnlabelsize) / 2), 122, scale=btnlabelsize)
            elif furdrawspeed == 2:
                furdrawspeed = 3
                display.text("TURBO", centers[2] - int(display.measure_text("TURBO", btnlabelsize) / 2), 122, scale=btnlabelsize)
            else:
                furdrawspeed = 0
                display.text("SLOW", centers[2] - int(display.measure_text("SLOW", btnlabelsize) / 2), 122, scale=btnlabelsize)
            display.set_update_speed(3)
            display.partial_update(int(WIDTH / 3) * 2, 112, WIDTH - int(WIDTH / 3) * 2, 16)
            time.sleep(0.3)
            render(1)
        else:               # CREDIT
            display.set_update_speed(2)
            draw_overlay("Content from an online fursona generator made by softhoof. Migrated to Micropython and content added by Waterfox.", WIDTH - OVERLAY_BORDER, HEIGHT - OVERLAY_BORDER, OVERLAY_SPACING, 0.5)
            display.update()
            time.sleep(3)
            render()

    if pin == button_up:
        pass
        if currentFurre == 0:
            pass
        else:
            currentFurre = currentFurre - 1
        drawThatFursona()
        display.update()
    if pin == button_down:
        pass
        if currentFurre == len(fursonas) - 1:
            pass
        else:
            currentFurre = currentFurre + 1
        drawThatFursona()
        display.update()


# Initial Interface Drawng before the main loop
badger.led(128)
display.set_update_speed(1)
render()

# Main loop!
while True:
    if badger.pressed(button_a):
        button(button_a)
    if badger.pressed(button_b):
        button(button_b)
    if badger.pressed(button_c):
        button(button_c)

    if badger.pressed(button_up):
        button(button_up)
    if badger.pressed(button_down):
        button(button_down)    
    
    time.sleep(0.01)
    