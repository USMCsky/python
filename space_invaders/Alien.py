import random

import pygame
import Settings
from Laser import Laser


class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, atype):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.atype = atype
        self.frame = 0
        self.image = pygame.image.load('images/aliens_sm.png')
        self.sprite_size = 32
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * self.sprite_size + Settings.xoffset,
                             self.y * self.sprite_size + Settings.yoffset)

    def flip_frame(self):
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0

    def draw(self, screen):
        if random.randint(0, 3000) < 1:
            Settings.abullets.append(Laser(self.x * self.sprite_size + Settings.xoffset,
                             self.y * self.sprite_size + Settings.yoffset, 5))
        if Settings.xoffset % 10 == 0:
            self.flip_frame()
        self.rect.topleft = (self.x * self.sprite_size + Settings.xoffset,
                             self.y * self.sprite_size + Settings.yoffset)
        screen.blit(self.image, [self.x * self.sprite_size + Settings.xoffset,
                                 self.y * self.sprite_size + Settings.yoffset,
                                 self.sprite_size, self.sprite_size],
                    [self.frame * self.sprite_size, self.sprite_size * self.atype, self.sprite_size, self.sprite_size])