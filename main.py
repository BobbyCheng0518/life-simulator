import pygame
import sys
import random
import easygui
from pygame.locals import *

pygame.init()

screensize = width, height = 800, 600
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("人生模拟器")
bg = 230, 230, 230
clock = pygame.time.Clock()
def tti(size, text):
    font = pygame.font.Font("./data/Microsoft YH.ttc", size)
    image = font.render(text, True, (0, 0, 0))
    return image

class Me(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.show_name = "我"
        self.image = tti(30, self.show_name)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.index = 0
        self.speed = 5
        self.speed2 = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[K_UP] and self.rect.top >= 0:
            self.rect.y -= 5
        if key[K_DOWN] and self.rect.bottom <= height:
            self.rect.y += 5
        if key[K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.left <= 0 and self.index == -1:
                self.speed = 0
            else:
                self.speed = 5
            if self.rect.right <= 0 and self.index > -1:
                self.index -= 1
                self.rect.right = width - 1
        if key[K_RIGHT]:
            self.rect.x += self.speed2
            if self.rect.right >= width and self.index == 1:
                self.speed2 = 0
            else:
                self.speed2 = 5
            if self.rect.left >= width and self.index < 1:
                self.index += 1
                self.rect.left = 1

class Building(pygame.sprite.Sprite):
    def __init__(self, name, x, y, color=(255, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = tti(50, name)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.name = name

me = Me()
b1 = [Building("五一小学", 100, 100)]
b2 = [Building("心理医院", 100, 100)]
b3 = [Building("河底捞火锅店", 150, 100)]
all = pygame.sprite.Group()
while True:
    if me.index == 0:
        for i in all:
            i.kill()
        for i in b2:
            all.add(i)
    if me.index == -1:
        for i in all:
            i.kill()
        for i in b1:
            all.add(i)
    if me.index == 1:
        for i in all:
            i.kill()
        for i in b3:
            all.add(i)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(bg)
    screen.blit(me.image, me.rect)
    me.update()
    all.draw(screen)
    all.update()
    pygame.display.update()
    clock.tick(60)
