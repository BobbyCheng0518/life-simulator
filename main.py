import pygame
import sys
import random
import easygui
from pygame.locals import *

from data import *

pygame.init()

screensize = width, height = 800, 600
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("人生模拟器")
bg = 230, 230, 230
clock = pygame.time.Clock()


me = Me(width, height)
b1 = [Building("五一小学", 100, 100)]
b2 = [Building("心理医院", 100, 100), Building("海湾体育场", 350, 100)]
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
