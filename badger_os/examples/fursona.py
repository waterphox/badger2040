# generate the fursona of your dreams
# originally by softhoof - http://www.generatorland.com/usergenerator.aspx?id=7427
# v2 by spiritechoes (inspired by softhoof's original) http://www.generatorland.com/usergenerator.aspx?id=16342

import badger2040
import gc
import os
import badger_os
import time
import math
import random
import machine
from badger2040 import WIDTH, HEIGHT

# Content, baby! Additional items added by Waterfox or taken from spiritechoes' v2 (when using v1, adjectives and species will be from both versions unless added manually)
adjective = ("eldritch","neon green","angelic","ghostly","scene","emo","hipster","alien","sweaty","OBSCENELY BRIGHT YELLOW","spotted","hairy","glowing","pastel pink","glittering blue","golden","shimmering red","robotic","black","goth","elegant","white","divine","striped","radioactive","red and green","slimy","slime","garbage","albino","skeleton","petite","swamp","aquatic","vampire","bright pink and yellow","mossy","stone","gray","fairy","zombie","pastel","mint green","giant","big pink","tiny pink","big white","tiny white","tiny black","translucent","glistening","glittering black","shimmering white","iridescent","glass","silver","jewel-encrusted","fuschia","purple","tiny purple","lilac","lavender","shimmering lilac","sparkling purple","tiny blue","heavenly","gilded","holy","blue and white striped","black and orange spotted","black and red","black and orange","ancient","green","purple and blue","pink and blue","candy","abyssal","floral","candle","melanistic","punk","ethereal","unholy","celestial","cyan","cream","cream and pink","cream and brown","yellow","black and pink","magenta","speckled","tiger-striped","chocolate","pastel goth","vintage","glossy black","glossy white","glossy gray","glossy blue","glossy pink","shimmery gray","glossy yellow","magma","plastic","leucistic","piebald","wooden","","green and yellow","brown and pink","purple and pink","beige","brown","neutral colored","pastel red","purple and green","black and blue","pastel green","neon","pastel blue","red","pink","blue","neon red","pastel purple","neon purple","neon orange","rainbow","dusty white","pastel yellow","neon pink","black and white","orange","brown and beige","pastel orange","neon yellow","neon blue")
species = ("kestrel","goat","sheep","dragon","platypus","blobfish","hydra","wolf","fox","sparkledog","cow","bull","cat","tiger","panther","hellhound","spider","beagle","pomeranian","whale","hammerhead shark","snake","hyena","lamb","pony","horse","pup","swan","pigeon","dove","fennec fox","fish","rat","possum","hamster","deer","elk","reindeer","cheetah","ferret","bear","panda","koala","kangaroo","skink","lizard","iguana","cerberus","turtle","raven","cardinal","bluejay","antelope","buffalo","rabbit","bunny","frog","newt","salamander","cobra","coyote","jellyfish","bee","wasp","dinosaur","bat","worm","chicken","eel","tiger","sloth","seal","vulture","barghest","hedgehog","peacock","anglerfish","dolphin","liger","llama","alpaca","walrus","mantis","ladybug","penguin","flamingo","civet","pudu","crab","maine coon","fawn","siamese","amoeba","owl","unicorn","crocodile","alligator","chihuahua","great dane","dachshund","corgi","rooster","sparrow","wyrm","slug","snail","seagull","badger","gargoyle","scorpion","boa","axolotl","kobold","sergal","synth","protogen","otter","shiba inu","fennix","rexouium","crux","pikachu","renamon","hobkin","impim","red panda","boar","polar bear","lioness","dutch angel dragon","monster","raptor","arctic wolf","zebra","lion","mountain lion","t-rex","cougar","dog","camel","human. A boring human Just like you :)","tigris","hen","ram","robin","leopard")
description = ("it constantly drips with a tar-like black substance.","it enjoys performing occult rituals with friends.","it is a communist.","a golden halo floats above its head.","it wears a mcdonalds uniform because it works at mcdonalds.","it carries a nail bat.","it wears louboutin heels.","it has two heads.","it has an unknowable amount of eyes.","it drools constantly.","its tongue is bright green.","it has numerous piercings.","it is a cheerleader.","it is a farmhand.","when you see it you are filled with an ancient fear.","it wears a toga.","it is made of jelly.","it has incredibly long and luxurious fur.","it uses reddit but won't admit it.","it glows softly and gently- evidence of a heavenly being.","it is a ghost.","it dresses like a greaser.","crystals grow from its flesh.","it rides motorcycles.","it wears incredibly large and impractical sunglasses.","it instagrams its starbucks drinks.","it is a hired killer.","where its tail should be is just another head.","it dwells in a bog.","it is wet and dripping with algae.","it runs a blog dedicated to different types of planes throughout history.","it worships the moon.","it comes from a long line of royalty.","it frolics in flowery meadows.","it wears a ballerina's outfit.","it wears a neutral milk hotel t-shirt with red fishnets and nothing else.","it wears a lot of eye makeup.","it won't stop sweating.","it has far too many teeth and they are all sharp.","it is a tattoo artist.","it is shaking.","it is a witch.","it wears scarves all the time.","to look into its eyes is to peer into a distant abyss.","mushrooms grow from its skin.","its face is actually an electronic screen.","it loves to wear combat boots with cute stickers all over them.","it comes from space.","it is a knife collector.","it flickers in and out of this plane of reality.","it wishes it were a cloud.","its eyes are red.","it is the most beautiful thing you have ever seen.","it loves strawberry milkshakes.","it cries all the time and can't really do much about it.","it lives alone in a dense forgotten wilderness.","it wears big christmas sweaters year-round.","it floats about a foot off of the ground.","it loves trash.","it has demonic wings.","it has a cutie mark of a bar of soap.","it is melting.","it wears opulent jewelry of gold and gemstones.","it has a hoard of bones.","it has ram horns.","it has a forked tongue.","it wears frilly dresses.","it has antlers.","it is a nature spirit.","its back is covered in candles which flicker ominously.","it wears a leather jacket with lots of patches.","it wears a snapback.","it has a tattoo that says 'yolo'.","electricity flickers through the air surrounding it.","it is a fire elemental.","it consumes only blood.","it works at an adorable tiny bakery.","it is a professional wrestler.","instead of eyes there are just more ears.","it speaks a forgotten and ancient language both disturbing and enchanting to mortal ears.","it works out.","it wishes it were a tree.","it is always blushing.","it uses ancient and powerful magic.","it loves raw meat.","it is always smiling.","it can fire lasers from its eyes.","a small raincloud follows it everywhere.","it is made of glass.","fireflies circle it constantly.","it is always accompanied by glowing orbs of light.","it has human legs.","water drips from it constantly.","it has golden horns.","it loves gore.","it lives in a cave with its parents.","its purse costs more than most people's cars.","it always shivers even when it's not cold.","it has tentacles.","it never blinks.","it only listens to metal.","it wears a golden crown.","it wears a white sundress.","it has green hair pulled up into two buns.","its body is covered in occult sigils and runes which pulse ominously.","it loves to devour the rotting plant matter covering the forest floor.","it wears a plain white mask.","its eyes flash multiple colors rapidly.","it loves to wear nail polish but applies it messily.","it runs a jimmy carter fanblog.","it is a surfer.","it only wears hawaiian shirts.","everything it wears is made out of denim.","it has long braided hair.","it calls everybody comrade.","it lures men to their deaths with its beautiful voice.","it has braces.","it has full sleeve tattoos.","it dresses like a grandpa.","smoke pours from its mouth.","it is a makeup artist.","it dresses like a pinup girl.","it has only one large eye.","it plays the harp.","it has very long hair with many flowers in it.","it has a cyan buzzcut.","it is a garden spirit.","it has fangs capable of injecting venom.","numerous eyeballs float around it. watching. waiting.","it loves to play in the mud.","it wears a surgical mask.","its eyes are pitch black and cause those who look directly into them for too long to slowly grow older.","it wears numerous cute hairclips.","it has a very large tattoo of the 'blockbuster' logo.","it is constantly covered in honey that drips on everything and pools beneath it.","it wears a cherry-themed outfit.","it has heterochromia.","it is heavily scarred.","in place of a head it has a floating cube that glows and pulses softly.","it seems to be glitching.","it does not have organs- instead it is full of flowers.","its insides are glowing.","it is a skateboarder.","it is a superwholock blogger.","it is a skilled glass-blower.","it has a pet of the same species as itself.","it is the leader of an association of villains.","it wears a black leather outfit.","its pupils are slits.","it wears a crop top with the word OATMEAL in all caps.","it only wears crop tops and high waisted shorts.","it is always giving everyone a suspicious look.","it has a septum piercing.","instead of talking it just says numbers.","it is an internet famous scene queen.","its eyes are way too big to be normal.","it has super obvious tan lines.","it wears a maid outfit.","it is an emissary from hell.","its eyes have multiple pupils in them.","it has an impractically large sword.","it is a magical girl.","it has a scorpion tail.","it is a biologist specializing in marine invertebrates.","it runs. everywhere. all the time.","it is an esteemed fashion designer for beings with 6 or more limbs.","it wears short shorts that say CLAM.","it can't stop knitting.","it is always coated in glitter.","it worships powerful dolphin deities.","it has slicked back hair.","it has a thick beard.","it has a long braided beard plaited with ribbons.","it is a viking.","it wears a parka.","its outfit is completely holographic.","it wears an oversized pearl necklace.","it has stubble.","it carries a cellphone with a ridiculous amount of charms and keychains.","it wears crocs.","it has a hoard of gems and gold that was pillaged from innocent villagers.","it robs banks.","its facial features are constantly shifting.","it works as a librarian in hell.","it wears a fedora.","it is made of petrified wood.")

# New v2-only content. New colors were merged in to adjective above, and new species merged in to species above. When using v2, colors and species will be from both versions.
personality = ("Dull","Boring","Dumb","Funny","Weird","Ugly","Popular","Stereotypical","Drooling","Smart","Nerdy","Pretty","Cute","Shining","Shimmering","Glittering","Invisible","Fluffy","Scaly","Awkward","Camouflaged","Lonely","Disgusting","Gross","Emo","Gothic","Pastel Gothic", "Creepy","Bitchy")
reflection = ("It thinks it's funny.","It's very socially awkward.","It's a dj.","It snapchat's it's life.","It always wears headphones, but it's never listening to music.","It's a feminist.","It's extremely sexist.","It's always happy.","It always plays Minecraft.","It's a gamer.","It makes self deprecating jokes.","It's gay.","It's lesbian.","It works out, A LOT!","It looks like it has been living under a rock for the past 2017 years.","It looks like it's from the stoneage.","It's a viking.","It's single and ready to mingle!","It's very social.","It has no eyes.","It has no fur.","It has very long fluffy fur. It loves nature.","It loves music.","It hates technology.","It's very racist.","It's very emotional.","It loves fashion. It's a small youtuber.","It's a youtuber with 2 subscribers, and 0 views.","It's a big youtuber. It's always listening to music.","It's always wearing headphones.")
appearance = ("It's covered in a floral pattern.","It has dots EVERYWHERE!","It looks like it was just outside, rolling in the mud.","It's head is twice as big as it's body.","It has no body.","It has stripes on it's back.","It has spikes on it's back.","It has 2 horns.","It has 5 horns.","It has 4 ears.","It has a heart on it's stomach.","It has a lightning like pattern. It's very tall.","It's gigantic!","It's super tiny.","It has two tails.","It has no ears.","It lost one eye.","It's super old.","It's made of sticks.","It's actually a robot.","It's made of glass.. Literally.","It always carries around it's phone.","It's crosseyed.","It's ALWAYS drooling! Literally ALWAYS! It has an impracticably large sword.","It carries around a bazooka. It hits everything it sees.","IT WON'T STOP BARKING.","IT WON'T STOP MEOWING.","It's head is made of glass.","It keeps slapping you in the face.","It likes to stare creepily at dolls.","It boops everything.","It constantly awoo's.","It's constantly singing the alphabet.","It eats pizza boxes.","It has legs like a human (lol).","It has a super long monkey tail.","It has a ginormous tail feather, instead of it's normal tail.","It won't stop screaming I ATE A BIRD LEAF!","It eats wolf snot for dinner.")
ability = ("","It has the ability to breathe fire.","It can control the way the earth moves.","It has the ability to stop time.","It's the goddess of the moon.","It's the king of the galaxy, and it can control life.","It can control life.","It can switch between alternate worlds and universes.","It lives on a star.","It's the god of cosmos.","It's the god of chaos.","It controls all evil.","It's also a vampire.","It controls time.","It has eternal life.","It's the god of everything. It speaks all languages fluently.","It controls peace.","It's the god of nature.","It has a lot of god like abilities, but refuses to use them.","It controls the ocean.","It's a spirit.","It's a ghost.","","","","","")
clothingcolor = ("red","orange","","yellow","green","blue","nothing, but when it does wear clothes, it wears","purple","pink","neon red","neon orange","neon yellow","neon green","neon blue","neon","pastel","neutral colored","trendy","new","neon purple","neon pink","pastel red","pastel orange","pastel yellow","pastel green","pastel blue","pastel purple","pastel pink","brown","dark brown","gray","black","black and white")
clothingstyle = ("dresses","shirts","t-shirts","jeans","gothic clothes","kawaii clothes","cute clothes","denim clothes","ripped clothes","clothes","hats","earrings","pants","skirts","crop tops","bathing suits","bikinis","tuxedos","cardigans","socks","rings","scarfs","ribbons","spiked collars","collars","necklaces","clown costumes","potato bags")

badger = badger2040.Badger2040()
display = badger

fursonasavedirectory = "output files" # Folder that the resulting save file ends up in.
fursonasavefile = "fursonasfile.txt"  # File name for saving generated fursonas 
fursonafilepath = fursonasavedirectory + "/" + fursonasavefile # Full path including directories. The file will be created if it does not exist.

inverted = False
fursonas = ["BEGINNING OF LIST", "END OF LIST"]
currentFurre = 0
menupage = 0
furdrawspeed = 2
o3ostate = 0
genver = 1

font_sizes = (0.5, 0.6, 0.55)

OVERLAY_BORDER = 40
OVERLAY_SPACING = 20
OVERLAY_TEXT_SIZE = 0.5

# Approximate center lines for buttons A, B and C
centers = (41, 147, 253)
btnlabels = (("MENU", "RE-DRAW", "GENERATE!!"),
             ("MENU", "SAVE THIS", "SPEED"),
             ("MENU", "LOAD FILE", "VERSION"),
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
        display.set_font("bitmap14_outline")
        if genver == 1:
            display.text("generate the fursona of your dreams", 3, 0, scale=0.4)
        else:
            display.text("Fursona Generator 2", 3, 0, scale=0.4)
        display.set_font("sans")
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
    line_spacing = (20, 20)
    lines = []
    current_line = ""
    fontcutoff = 100
    smallfont = 1
    if len(fursonas[currentFurre]) >= fontcutoff and override == "":
#        display.set_font("bitmap6") # Use smaller font for v2
        smallfont = 2
    for word in words:
        if display.measure_text(current_line + word + " ", font_sizes[smallfont]) < WIDTH:
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
        length = display.measure_text(lines[i], font_sizes[smallfont])
        if len(fursonas[currentFurre]) < fontcutoff or override != "":
            current_line = (i * line_spacing[0]) - ((num_lines - 1) * line_spacing[0]) // 2
            display.text(lines[i], (WIDTH - length) // 2, (HEIGHT // 2) + current_line, scale=font_sizes[1])
        else:
            current_line = (i * line_spacing[1]) - ((num_lines - 1) * line_spacing[1]) // 2
            display.text(lines[i], (WIDTH - length) // 2, int((HEIGHT // 2) + current_line // 1.5), scale=font_sizes[2]) # v2 font is bitmap which doesn't vertical center Y align
    
#    display.set_font("sans") # Set back to normal font just in case v2 was used

def generateFursona():
    global currentFurre
    if genver == 1:
        fursonas.insert(len(fursonas) - 1, random.choice(adjective) + " " + random.choice(species) + ". " + random.choice(description))
    else:
        fursonas.insert(len(fursonas) - 1, random.choice(personality) + " " + random.choice(adjective) + " " + random.choice(species) + ". " + random.choice(reflection) + " " + random.choice(appearance) + " " + random.choice(ability) + " It always wears " + random.choice(clothingcolor) + " " + random.choice(clothingstyle) + ".")
    currentFurre = len(fursonas) - 2

def load_fursonas_file(): # Loads the fursona file. ASSUMES FILE EXISTS, FUNCTION SHOULD NOT BE CALLED unless we're already in a position where we know the file's there
    global currentFurre, fursonas, menupage
    furrefile = open(fursonafilepath, "r")
    importedfurres = furrefile.readlines()
    furrefile.close()
    fursonas = ["BEGINNING OF LIST", "END OF LIST"]
    for f in importedfurres:
        if f != "": # Mostly to not load the blank line at the end.
            fursonas.insert(len(fursonas) - 1, str(f).strip())
    currentFurre = len(fursonas) - 2
    menupage = 0
    render()

def button(pin):
    global menupage, font_size, inverted, currentFurre, furdrawspeed, o3ostate, genver
    badger.led(255)
    if pin == button_a:     # This button switches between menu options, unless we're asking YES/NO for file load
        if menupage == 4:   # They clicked YES to LOAD the fursonas file
            load_fursonas_file() # Load as requested!
        else:
            o3ostate = 0
            if menupage == 0:   # MENU, RE-DRAW, GENERATE!
                menupage = 1
            elif menupage == 1: # MENU, SAVE, SPEED
                menupage = 2
            elif menupage == 2: # MENU, LOAD, SAVE
                menupage = 3
            elif menupage == 3: # MENU, o3o, CREDIT
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
                    furfile = open(fursonafilepath, "a")   # Opens the existing file in append mode, or creates the file if it doesn't exist.
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
        elif menupage == 2: # LOAD Menu Option
            if fursonasavefile in os.listdir(fursonasavedirectory): # File already exists
                if len(fursonas) == 2: #We have not generated any yet
                    load_fursonas_file() # Just do it without asking
                else:
                    menupage = 4
                    drawThatFursona("Are you sure? Any furres generated so far will be overwritten if not already saved to the file.")
                    draw_menu()
                    display.set_update_speed(3)
                    display.update()
                    # After this, handled by A or C buttons. A is YES and will load the file. C is NO and bumps us back to menu 2/regular operation
            else:                                                   # File does not exist
                drawThatFursona("File does not exist. Save some fursonas, first?")
                display.set_update_speed(3)
                display.update()                           # After all that, show whatever message is relevant based on what happened.
                time.sleep(1)
                drawThatFursona()
                render()
        else:               # o3o Menu Option
            display.set_update_speed(2)
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
        if menupage == 4: # Pressed NO to LOADing the file
            menupage = 0
            display.set_update_speed(3)
            render()
        else:
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
            elif menupage == 2: # VERSION Menu Option
                display.set_pen(15)
                display.rectangle(int(WIDTH /3) * 2, 112, WIDTH - int(WIDTH / 3) * 2, 16)
                display.set_pen(0)
                if genver == 1:
                    genver = 2
                    display.text("V2 SET", centers[2] - int(display.measure_text("V2 SET", btnlabelsize) / 2), 122, scale=btnlabelsize)
                else:
                    genver = 1
                    display.text("V1 SET", centers[2] - int(display.measure_text("V1 SET", btnlabelsize) / 2), 122, scale=btnlabelsize)
                display.set_update_speed(3)
                display.partial_update(int(WIDTH / 3) * 2, 112, WIDTH - int(WIDTH / 3) * 2, 16)
                time.sleep(0.3)
                render(1)
            else:               # CREDIT Menu Option
                display.set_update_speed(2)
                if genver == 1:
                    draw_overlay("Content from an online fursona generator made by softhoof. Migrated to Micropython and content added by Waterfox.", WIDTH - OVERLAY_BORDER, HEIGHT - OVERLAY_BORDER, OVERLAY_SPACING, 0.5)
                else:
                    draw_overlay("Content from Fursona Generator 2 by spiritechoes, inspired by the first. Ported here with additions by Waterfox.", WIDTH - OVERLAY_BORDER, HEIGHT - OVERLAY_BORDER, OVERLAY_SPACING, 0.5)
                display.update()
                time.sleep(3)
                render()

    if pin == button_up:
        if currentFurre == 0 or menupage == 4: # Reasons for the up button to do nothing. Top of list, or YESNO to load question
            pass
        else:
            currentFurre = currentFurre - 1
        drawThatFursona()
        render()
    if pin == button_down:
        if currentFurre == len(fursonas) - 1 or menupage == 4: # Reasons for the down button to do nothing. Bottom of list, or YESNO to load question
            pass
        else:
            currentFurre = currentFurre + 1
        drawThatFursona()
        render()


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
    