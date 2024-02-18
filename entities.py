import pygame
import config
import utils
import random
import items

class Entity(pygame.sprite.Sprite):
    def __init__(self, coords, is_friendly, weapon_code, movement_speed, health):
        super().__init__()
        self.image = pygame.transform.scale(self.image, config.ENTITY_SIZE)
        self.rect = self.image.get_rect(center = coords)
        self._original_image = self.image.copy()
        self.coords = coords
        self.is_using_item = False if is_friendly else True
        self.is_friendly = is_friendly
        self.movement_speed = movement_speed
        self.health = health
        self.max_health = health
        self.projectiles = []
        if not is_friendly:
            self.active_item = items.weapon_factory(self, weapon_code)

    def move(self, movement_vector):
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


    def aim(self, direction):
        #rotate entity
        utils.rotate(self, self.coords, direction, 0)

        if not self.active_item:
            return
        
        #translate active item
        translate_amount = (self.active_item.width ** 2 + self.active_item.height ** 2) ** 0.5 / 2
        self.active_item.coords = utils.translate(self.coords, self.coords, direction, translate_amount)

        #attack with active item
        additional_angle = self.active_item.use(direction)
        
        #rotate active item
        utils.rotate(self.active_item, self.coords, direction, additional_angle)
        self.active_item.coords = utils.rotate_around_point(self.active_item.coords, self.coords, -additional_angle)
        self.active_item.rect = self.active_item.image.get_rect(center = self.active_item.coords)
    

#entity_code = 0
class GreasyKiller(Entity):
    def __init__(self, coords):
        self.image = pygame.image.load(config.GREASY_KILLER_ICON).convert_alpha()
        speed = config.GREASY_KILLER_MOVEMENT_SPEED
        health = config.GREASY_KILLER_HEALTH
        super().__init__(coords, True, None, speed, health)
        self.items = []
        self.current_item = 0
        self.balance = 0

    @property
    def active_item(self):
        return self.items[self.current_item]
    
    def use_item(self):
        self.active_item.use_item()


    def select_item(self, index):
        self.current_item = index if index >= 0 and index < len(self.items) else self.current_item 


    def move(self, keys):
        movement_vector = utils.get_mov_vector(keys)
        super().move(movement_vector)


    def aim(self):
       super().aim(pygame.mouse.get_pos())


class Monster(Entity):
    def __init__(self, coords, movement_speed, weapon_code, body_damage, health):
        super().__init__(coords, False, weapon_code, movement_speed, health)
        self.body_damage = body_damage

    def move(self, target_point):
        mov_vector_end = utils.translate(self.coords, self.coords, target_point, self.movement_speed)
        mov_vector = (mov_vector_end[0] - self.coords[0], mov_vector_end[1] - self.coords[1])
        super().move(mov_vector)


#entity_code = 1
class SlickbackScoundrel(Monster):
    def __init__(self, coords):
        self.image = pygame.image.load(config.SLICKBACK_SCOUNDREL_ICON).convert_alpha()
        speed = config.SLICKBACK_SCOUNDREL_MOVEMENT_SPEED
        damage = config.SLICKBACK_SCOUNDREL_BODY_DAMAGE
        health = config.SLICKBACK_SCOUNDREL_HEALTH
        super().__init__(coords, speed, None, damage, health)

#entity_code = 2
class DaggerMaster(Monster):
    def __init__(self, coords):
        self.image = pygame.image.load(config.DAGGER_MASTER_ICON).convert_alpha()
        speed = config.DAGGER_MASTER_MOVEMENT_SPEED
        damage = config.DAGGER_MASTER_BODY_DAMAGE
        health = config.DAGGER_MASTER_HEALTH
        super().__init__(coords, speed, 1, damage, health)

#entity_code = 3
class FrostwindMarksman(Monster):
    def __init__(self, coords):
        self.image = pygame.image.load(config.FROSTWIND_MARKSMAN_ICON).convert_alpha()
        speed = config.FROSTWIND_MARKSMAN_MOVEMENT_SPEED
        damage = config.FROSTWIND_MARKSMAN_BODY_DAMAGE
        health = config.FROSTWIND_MARKSMAN_HEALTH
        super().__init__(coords, speed, 2, damage, health)

def entity_factory(code):
    #generate the topleft coordinates of the new monster
    match random.randint(1, 4):
        case 1: #left wall
            coords = (0, random.randint(0, config.SCREEN_HEIGHT - int(config.ENTITY_SIZE[1])))
        case 2: #top wall
            coords = (random.randint(0, config.SCREEN_WIDTH - int(config.ENTITY_SIZE[0])), 0)
        case 3: #right wall
            coords = (config.SCREEN_WIDTH - int(config.ENTITY_SIZE[0]),
                      random.randint(0, config.SCREEN_HEIGHT - int(config.ENTITY_SIZE[1])))
        case 4: #bottom wall
            coords = (random.randint(0, config.SCREEN_WIDTH - int(config.ENTITY_SIZE[0])),
                      config.SCREEN_HEIGHT - int(config.ENTITY_SIZE[1]))
    
    #transform topleft coordinates into center coordinates
    coords = (coords[0] + config.ENTITY_SIZE[0] // 2, coords[1] + config.ENTITY_SIZE[1] // 2)

    #spawn enemy with the given code at the generated coordinates
    match code:
        case 1:
            return SlickbackScoundrel(coords)
        case 2:
            return DaggerMaster(coords)
        case 3:
            return FrostwindMarksman(coords)