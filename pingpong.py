from pygame import *

# CLASS FOR ALL GAME OBJECTS --------
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# CLASS TO CREATE PLAYER ----------
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

# IMAGES
img_back = "table.png"
img_ball = "ball.png"
img_racket1 = "batmerah.png"
img_racket2 = "batbiru.png"

# DATA
finish = False
run = True
clock = time.Clock()
FPS = 60

# GAME WINDOW -----------
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# OBJECTS -----------
ball = GameSprite(img_ball, 200, 200, 40, 40, 4)
racket1 = Player(img_racket1, -30, 200, 130, 160, 4)
racket2 = Player(img_racket2, 580, 200, 130, 160, 4)

# LABELS -----------
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

# BALL SPEED -----------
speed_x = 3
speed_y = 3

# GAME LOOPS -----------
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0)) 

        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # COLLISION WITH TOP AND BOTTOM WALLS -----------
        if ball.rect.y > win_height-120 or ball.rect.y < 0:
           speed_y *= -1
        
        # HIT THE BALL WITH RACKET ------
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        # PLAYER 1 LOSE --------
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        # PLAYER 2 LOSE --------
        if ball.rect.x > 660:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

        display.update()
        clock.tick(FPS)