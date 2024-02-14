import pygame
import config
import utils

class Entity(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.rect = self.image.get_rect(center = coords)
        self.coords = coords
        self.is_attacking = False

class GreasyKiller(Entity):
    def __init__(self, coords):
        self.image = pygame.image.load(config.GREASY_KILLER_ICON).convert_alpha()
        self._original_image = self.image.copy()
        super().__init__(coords)
        self.current_item = 0
        self.items = []

    def use_item(self):
        self.items[self.current_item].sprite.use()

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
        hero_rect.right = min(hero_rect.right, config.SCREEN_WIDTH)
        hero_rect.top = max(hero_rect.top, 0)
        hero_rect.bottom = min(hero_rect.bottom, config.SCREEN_HEIGHT)

        #update coords
        self.coords = hero_rect.center

    def aim(self, active_item):
        #translate
        translate_amount = (active_item.sprite.width ** 2 + active_item.sprite.height ** 2) ** 0.5 / 2
        utils.translate(active_item.sprite, self.coords, self.coords, pygame.mouse.get_pos(), translate_amount)

        #rotate
        additional_angle = active_item.sprite.slash()
        utils.rotate(self, self.coords, pygame.mouse.get_pos(), 0)
        utils.rotate(active_item.sprite, self.coords, pygame.mouse.get_pos(), additional_angle)
        active_item.sprite.coords = utils.rotate_around_point(active_item.sprite.coords, self.coords, -additional_angle)
        active_item.sprite.rect = active_item.sprite.image.get_rect(center = active_item.sprite.coords)


class Monster(Entity):
    def __init__(self, coords):
        super().__init__(coords)

class SlickbackScoundrel(Monster):
    def __init__(self, coords):
        self.image = pygame.image.load(config.SLICKBACK_SCOUNDREL_ICON).convert_alpha()
        super().__init__(coords)
