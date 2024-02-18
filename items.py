import pygame
import config
import abc

class Item(pygame.sprite.Sprite):
    def __init__(self, price, owner, size):
        super().__init__()
        self.price = price
        self.owner = owner
        self.coords = self.owner.coords
        self.size = size if owner.is_friendly else (size[0] * 0.75, size[1])
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(midleft = self.owner.rect.center)
        self._original_image = self.image.copy()


    def use_item(self):
        self.owner.is_using_item = True

    
    @property
    def width(self):
        return abs(self.rect.right - self.rect.left)
    

    @property
    def height(self):
        return abs(self.rect.top - self.rect.bottom)


class HealingPotion(Item):
    def __init__(self, owner):
        self.image = pygame.image.load(config.POTION_ICON).convert_alpha()
        pygame.Surface.set_colorkey(self.image, (255, 255, 255))
        size = config.POTION_SIZE
        self.heal_amount = config.POTION_HEAL_AMOUNT
        price = -1 if 'potion' in config.STARTING_ITEMS else config.SHOP_ITEMS['potion']
        super().__init__(price, owner, size)
    
    #apply potion
    def use(self, direction):
        if not self.owner.is_using_item:
            return 0
        self.owner.is_using_item = False
        self.owner.items.remove(self)
        self.owner.current_item = 0
        self.owner.health = min(self.owner.max_health, self.owner.health + self.heal_amount)
        return 0
    

class Weapon(Item, abc.ABC):
    def __init__(self, owner, price, damage, size, speed):
        super().__init__(price, owner, size)
        self.damage = damage
        self.speed = speed


class MeleeWeapon(Weapon, abc.ABC):
    def __init__(self, owner, price, damage, size, span, speed):
        super().__init__(owner, price, damage, size, speed)
        self.attack_progress = 1
        self.span = span
        self.hit = False
        self.speed = self.speed if owner.is_friendly else self.speed // 2

    #slash
    def use(self, direction):
        if not self.owner.is_using_item:
           return 0
        if self.attack_progress > self.span:
            self.attack_progress = 1
            self.hit = False
            if self.owner.is_friendly:
                self.owner.is_using_item = False
            return 0
        
        self.attack_progress += self.speed
        return self.span / 2 - self.attack_progress


#weapon_code = 1
class Dagger(MeleeWeapon):
    def __init__(self, owner):
        self.image = pygame.image.load(config.DAGGER_ICON).convert_alpha()
        pygame.Surface.set_colorkey(self.image, (255, 255, 255))
    
        price = -1 if 'dagger' in config.STARTING_ITEMS else config.SHOP_ITEMS['dagger']
        super().__init__(owner, price, config.DAGGER_DAMAGE, config.DAGGER_SIZE, config.DAGGER_SPAN, config.DAGGER_SPEED)



class RangedWeapon(Weapon, abc.ABC):
    @abc.abstractmethod
    def get_new_projectile(self):
        pass


    def __init__(self, owner, price, damage, size, speed, cooldown):
        self.projectiles = []
        self.cooldown = cooldown
        self.last_shoot = -1
        super().__init__(owner, price, damage, size, speed)


    #shoot
    def use(self, direction):
        if not self.owner.is_using_item:
            return 0
        if self.owner.is_friendly:
            self.owner.is_using_item = False

        if self.last_shoot == -1:
            self.last_shoot = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.last_shoot < self.cooldown:
            return 0
        self.owner.projectiles.append(self.get_new_projectile(direction))
        self.last_shoot = pygame.time.get_ticks()
        return 0
        
#weapon_code = 2
class Bow(RangedWeapon):
    def __init__(self, owner):
        self.image = pygame.image.load(config.BOW_ICON).convert_alpha()
        pygame.Surface.set_colorkey(self.image, (255, 255, 255))

        price = -1 if 'bow' in config.STARTING_ITEMS else config.SHOP_ITEMS['bow']
        super().__init__(owner, price, config.BOW_PROJECTILE_DAMAGE, config.BOW_SIZE,
                         config.BOW_PROJECTILE_SPEED, config.BOW_COOLDOWN)


    def get_new_projectile(self, direction):
        start = self.owner.rect.center
        direction_vector = (direction[0] - start[0], direction[1] - start[1])
        return BowProjectile(direction_vector, self.owner)


class Projectile(pygame.sprite.Sprite, abc.ABC):
    def __init__(self, damage, direction, speed, owner):
        super().__init__()
        self.damage = damage
        self.direction = direction
        self.speed = speed
        self.owner = owner
        self.coords = owner.coords
        self._original_image = self.image.copy()

        pygame.Surface.set_colorkey(self.image, (255, 255, 255))
        self.rect = self.image.get_rect(center = self.coords)
    

class BowProjectile(Projectile):
    def __init__(self, direction, owner):
        icon = config.BOW_PROJECTILE_ICON if owner.is_friendly else config.ENEMY_BOW_PROJECTILE_ICON
        self.image = pygame.image.load(icon).convert_alpha()
        self.image = pygame.transform.scale(self.image, config.BOW_PROJECTILE_SIZE)
        pygame.Surface.set_colorkey(self.image, (255, 255, 255))
        super().__init__(config.BOW_PROJECTILE_DAMAGE, direction,
                         config.BOW_PROJECTILE_SPEED, owner)
        

def weapon_factory(owner, code):
    if code is None:
        return None
    
    match code:
        case 1:
            return Dagger(owner)
        case 2:
            return Bow(owner)