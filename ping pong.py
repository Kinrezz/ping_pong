#Создай собственный Шутер!
from pygame import *
from random import *
font.init()
#класс
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.lost = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 365:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 365:
            self.rect.y += self.speed
class Ball(GameSprite):
    speed_x = 5
    speed_y = 5
    def update(self):
        if ball.rect.y > 450 or ball.rect.y < 0:
            Ball.speed_y *= -1
        self.rect.x += Ball.speed_x
        self.rect.y += Ball.speed_y
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
#задай фон сцены   0
wc = (220,220,240)
window.fill(wc) 
#обработай событие «клик по кнопке "Закрыть окно"»
clock = time.Clock()
run = True
finish = False 
#dfdfd
racket1 = Player('racket.png', 5, 200, 7, 39, 136)
racket2 = Player('racket.png', 650, 200, 7, 39, 136)
ball = Ball('tenis_ball.png', 250, 250, 7, 50, 60)
#цикл
win1 = font.Font(None, 60).render('игрок 2 лошпед)))))))', True, (40,240,40))
win2 = font.Font(None, 60).render('игрок 1 лошпед)))))))', True, (240,40,40))
is_collide_ball = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == False:
        if is_collide_ball == True and not ( sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball)):
            is_collide_ball = False
        if ( sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball)) and is_collide_ball == False:
            Ball.speed_x *= -1
            is_collide_ball = True
        window.fill(wc)
        if ball.rect.x <= -50:
            window.blit(win2, (220, 220))
            finish = True
        if ball.rect.x >= 750:
            window.blit(win1, (220, 220))
            finish = True
        racket1.update_1()
        racket2.update_2()
        racket1.reset()
        racket2.reset()
        ball.update()
        ball.reset()
    display.update()
    clock.tick(60)
    