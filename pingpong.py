from pygame import *


#IMAGES
img_back = "table.png"

#DATA
finish = False
run = True

# GAME WINDOW -----------
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# GAME LOOPS -----------
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        
        # PRESS KEY TO FIRE ----------
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire = num_fire + 1
                    fire_sound.play()
                    ship.fire()
                
                # FIRE LIMIT -------
                if num_fire  >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True
