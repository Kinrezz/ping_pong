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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys_pressed[K_SPACE]:
            self.fire()
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
racket = Player('racket.png', 50, 250, 7, 39, 136)
#цикл
win = font.Font(None, 60).render('Ура победа', True, (40,240,40))
lose = font.Font(None, 60).render('Поражение', True, (240,40,40))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == False:
        racket.reset()
    display.update()
    clock.tick(60)
    