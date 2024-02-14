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
        
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(midleft = self.owner.rect.center)
        self._original_image = self.image.copy()

        self.attack_progress = 1
        self.weapon_type = weapon_type

    @property
    def width(self):
        return abs(self.rect.right - self.rect.left)
    
    @property
    def height(self):
        return abs(self.rect.top - self.rect.bottom)
    
    def use(self):
        if self.weapon_type is WeaponType.melee:
            self.owner.is_attacking = True
            self.slash()
        elif self.weapon_type is WeaponType.ranged:
            self.shoot()

    def slash(self):
        if not self.owner.is_attacking:
           return 0
        
        if self.attack_progress > self.span:
            self.attack_progress = 1
            self.owner.is_attacking = False
            return 0
        
        self.attack_progress += self.speed
        return self.span / 2 - self.attack_progress
    
    def shoot(self):
        pass

class Dagger(Weapon):
    def __init__(self, owner):
        self.size = config.DAGGER_SIZE
        self.span = config.DAGGER_SPAN
        self.speed = config.DAGGER_SPEED
        self.image = pygame.image.load(config.DAGGER_ICON).convert_alpha()
        super().__init__(owner, WeaponType.melee)
