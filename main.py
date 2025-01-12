import pygame
import sys
import random
from pygame.locals import *

from data import *

# 初始化PyGame
pygame.init()

# 设置屏幕尺寸、屏幕颜色和帧率
screensize = width, height = 800, 600
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("人生模拟器")
bg = 230, 230, 230
clock = pygame.time.Clock()

# 地图数据
me = Me(width, height)
all = pygame.sprite.Group()
road = pygame.sprite.Group()
street = pygame.sprite.Group()

b1 = [
    Building("五一小学", 100, 100),
    Building("五一初中", 100, 190)
]
b2 = [
    Building("心理医院", 100, 100),
    Building("海湾体育场", 350, 100),
    Building("密室逃脱", 600, 100)
]
b3 = [
    Building("河底捞火锅店", 150, 100)
]
r1 = [
    Road("五一路", 100, 160)
]
r2 = [
    Road("中山西路", width//2, 160)
]
r3 = [
    Road("中山东路", 100, 160)
]
s1 = [
    Street("五一街",230, 150)
]
s2 = [
    Street("中街",230, 100)
]
s3 = [
    Street("第三街", 300, 100)
]
while True:
    if me.index == 0:
        for i in all:
            i.kill()
        for i in b2:
            all.add(i)
        for i in road:
            i.kill()
        for i in r2:
            road.add(i)
        for i in street:
            i.kill()
        for i in s2:
            for j in i.image:
                street.add(j)

    if me.index == -1:
        for i in all:
            i.kill()
        for i in b1:
            all.add(i)
        for i in road:
            i.kill()
        for i in r1:
            road.add(i)
        for i in street:
            i.kill()
        for i in s1:
            for j in i.image:
                street.add(j)
    if me.index == 1:
        for i in all:
            i.kill()
        for i in b3:
            all.add(i)
        for i in road:
            i.kill()
        for i in r3:
            road.add(i)
        for i in street:
            i.kill()
        for i in s3:
            for j in i.image:
                street.add(j)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(bg)
    me.update()
    all.draw(screen)
    all.update()
    road.draw(screen)
    road.update()
    street.draw(screen)
    street.update()
    screen.blit(me.image, me.rect)
    pygame.display.update()
    clock.tick(60)
