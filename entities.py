import pygame
import config

class Entity(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.rect = self.image.get_rect(center = coords)

class GreasyKiller(Entity):
    def __init__(self, coords):
        self.image = pygame.image.load(config.greasy_killer_icon).convert_alpha()
        super().__init__(coords)

class Monster(Entity):
    def __init__(self, coords):
        super().__init__(coords)

class SlickbackScoundrel(Monster):
    def __init__(self, coords):
        self.image = pygame.image.load(config.slickback_scoundrel_icon).convert_alpha()
        super().__init__(coords)
