import pygame
import config
import utils

class Entity(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.rect = self.image.get_rect(center = coords)
        self.coords = coords

class GreasyKiller(Entity):
    def __init__(self, coords):
        self.image = pygame.image.load(config.greasy_killer_icon).convert_alpha()
        self._original_image = self.image.copy()
        super().__init__(coords)
        self.current_item = 0
        self.items = []

    def use_item(self):
        self.items[self.current_item].use()

    def select_item(self, index):
        self.current_item = index if index >= 0 and index <= 9 else self.current_item 

    def move(self, keys):
        movement_vector = utils.get_mov_vector(keys)
        hero_rect = self.rect

        #move
        hero_rect.left += movement_vector[0]
        hero_rect.top += movement_vector[1]

        #fix out of bounds
        hero_rect.left = max(hero_rect.left, 0)
        hero_rect.right = min(hero_rect.right, config.screen_width)
        hero_rect.top = max(hero_rect.top, 0)
        hero_rect.bottom = min(hero_rect.bottom, config.screen_height)

        #update coords
        self.coords = hero_rect.center

    def aim(self, active_item):
        #rotate
        utils.rotate(self, self, pygame.mouse.get_pos())
        utils.rotate(self, active_item.sprite, pygame.mouse.get_pos())

        #translate
        translate_amount = max(active_item.sprite.width, active_item.sprite.height) / 2
        active_item.sprite.translate(self.coords, pygame.mouse.get_pos(), translate_amount)
    


class Monster(Entity):
    def __init__(self, coords):
        super().__init__(coords)

class SlickbackScoundrel(Monster):
    def __init__(self, coords):
        self.image = pygame.image.load(config.slickback_scoundrel_icon).convert_alpha()
        super().__init__(coords)
