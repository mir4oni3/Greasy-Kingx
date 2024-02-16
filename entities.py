import pygame
import config
import utils
import weapons

class Entity(pygame.sprite.Sprite):
    def __init__(self, coords, is_friendly):
        super().__init__()
        self.image = pygame.transform.scale(self.image, config.ENTITY_SIZE)
        self.rect = self.image.get_rect(center = coords)
        self._original_image = self.image.copy()
        self.coords = coords
        self.is_using_item = False
        self.is_friendly = is_friendly

class GreasyKiller(Entity):
    def __init__(self, coords):
        self.image = pygame.image.load(config.GREASY_KILLER_ICON).convert_alpha()
        super().__init__(coords, True)
        self.items = []
        self.current_item = 0
        self.balance = 0

    def use_item(self):
        self.items[self.current_item].sprite.use_item()

    def select_item(self, index):
        self.current_item = index if index >= 0 and index <= 9 else self.current_item 

    def move(self, keys):
        movement_vector = utils.get_mov_vector(keys)

        #move
        self.rect.left += movement_vector[0]
        self.rect.top += movement_vector[1]

        #fix out of bounds
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, config.SCREEN_WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, config.SCREEN_HEIGHT)

        #update coords
        self.coords = self.rect.center

    def aim(self, active_item):
        #translate
        translate_amount = (active_item.sprite.width ** 2 + active_item.sprite.height ** 2) ** 0.5 / 2
        utils.translate(active_item.sprite, self.coords, self.coords, pygame.mouse.get_pos(), translate_amount)

        #attack
        additional_angle = active_item.sprite.use()
        
        #rotate
        utils.rotate(self, self.coords, pygame.mouse.get_pos(), 0)
        utils.rotate(active_item.sprite, self.coords, pygame.mouse.get_pos(), additional_angle)
        active_item.sprite.coords = utils.rotate_around_point(active_item.sprite.coords, self.coords, -additional_angle)
        active_item.sprite.rect = active_item.sprite.image.get_rect(center = active_item.sprite.coords)


class Monster(Entity):
    def __init__(self, coords):
        super().__init__(coords, False)

class SlickbackScoundrel(Monster):
    def __init__(self, coords):
        self.image = pygame.image.load(config.SLICKBACK_SCOUNDREL_ICON).convert_alpha()
        super().__init__(coords)
