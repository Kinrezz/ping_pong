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
    def update(self, player):
        self.rect.y += self.speed
        if self.rect.y > 500 or sprite.spritecollide(player, monsters, False):
            self.rect.y = 0
            self.rect.x = randint(0, 620)
            player.lost += 1
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
#цикл
win = font.Font(None, 60).render('Ура победа', True, (40,240,40))
lose = font.Font(None, 60).render('Поражение', True, (240,40,40))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == False:
        window.fill(wc)
        racket1.update_1()
        racket2.update_2()
        racket1.reset()
        racket2.reset()
    display.update()
    clock.tick(60)
    