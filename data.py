import pygame
from pygame.locals import *

def tti(size, text, color=(0, 0, 0)):
    font = pygame.font.Font("./data/Microsoft YH.ttc", size)
    image = font.render(text, True, color)
    return image

class Me(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = width, height
        self.show_name = "我"
        self.image = tti(30, self.show_name)
        self.rect = self.image.get_rect()
        self.rect.center = (self.width // 2, self.height // 2)
        self.index = 0
        self.speed = 5
        self.speed2 = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[K_UP] and self.rect.top >= 0:
            self.rect.y -= 5
        if key[K_DOWN] and self.rect.bottom <= self.height:
            self.rect.y += 5
        if key[K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.left <= 0 and self.index == -1:
                self.speed = 0
            else:
                self.speed = 5
            if self.rect.right <= 0 and self.index > -1:
                self.index -= 1
                self.rect.right = self.width - 1
        if key[K_RIGHT]:
            self.rect.x += self.speed2
            if self.rect.right >= self.width and self.index == 1:
                self.speed2 = 0
            else:
                self.speed2 = 5
            if self.rect.left >= self.width and self.index < 1:
                self.index += 1
                self.rect.left = 1

class Building(pygame.sprite.Sprite):
    def __init__(self, name, x, y, color=(255, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = tti(40, name)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.name = name

class Road(Building):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self.image = tti(20, name, (255, 0, 0))