from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed,sprite_width, sprite_height):
        super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.rect.width = sprite_width
        self.rect.height = sprite_height
 
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
win = display.set_mode((win_width, win_height))
display.set_caption("pin_pong")
color = (255, 255, 255)
win.fill(color)


game = True

rak1 = GameSprite('racket.png', 10, 10, 3, 40, 10)
rak2 = GameSprite('racket.png', 620, 10, 3, 40, 10)
ball = GameSprite('tenis_ball.png', 320, 200, 3, 20, 20)

FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False

    win.fill(color)
    ball.reset()
    rak1.reset()
    rak2.reset()

    display.update()