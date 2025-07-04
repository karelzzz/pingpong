from pygame import *

# IMAGES
img_back = "table.png"

# DATA
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

    window.blit(background, (0, 0)) 
    display.update()