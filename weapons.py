import pygame
import config
from enum import Enum

class WeaponType(Enum):
    melee = 1
    ranged = 2

class Weapon(pygame.sprite.Sprite):
    def __init__(self, owner, weapon_type):
        super().__init__()

        self.owner = owner
        self.coords = self.owner.coords
        
        self.rect = self.image.get_rect(midleft = self.owner.rect.center)
        self._original_image = self.image.copy()

        self.is_attacking = False
        self.weapon_type = weapon_type

    @property
    def width(self):
        return abs(self.rect.right - self.rect.left)
    
    @property
    def height(self):
        return abs(self.rect.top - self.rect.bottom)
    
    def translate(self, point1, point2, pixel_count):
        '''Translate sprite in the direction point1->point2 by pixel_count'''
        dir_x = point2[0] - point1[0]
        dir_y = point2[1] - point1[1]

        #normalize vector
        vector_length = (dir_x ** 2 + dir_y ** 2) ** 0.5
        dir_x /= vector_length
        dir_y /= vector_length

        #scale vector to target size
        dir_x *= pixel_count
        dir_y *= pixel_count

        #update coords
        self.coords = (point1[0] + dir_x, point1[1] + dir_y)
        self.rect = self.image.get_rect(center = self.coords)

    def attack(self, direction):
        pass


class Dagger(Weapon):
    def __init__(self, owner):
        self.image = pygame.image.load(config.dagger_icon).convert_alpha()
        super().__init__(owner, WeaponType.melee)
        self.range = 40
        self.span = 100
        self.speed = 10
    