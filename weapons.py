import pygame
import config
import abc

class Item(pygame.sprite.Sprite):
    def __init__(self, price):
        super().__init__()
        self.price = price


class Weapon(Item, abc.ABC):
    @abc.abstractmethod
    def attack(self):
        pass


    def __init__(self, owner, price, damage, size, speed):
        super().__init__(price)

        self.damage = damage
        self.size = size
        self.speed = speed

        self.owner = owner
        self.coords = self.owner.coords
        
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(midleft = self.owner.rect.center)
        self._original_image = self.image.copy()


    @property
    def width(self):
        return abs(self.rect.right - self.rect.left)
    

    @property
    def height(self):
        return abs(self.rect.top - self.rect.bottom)
    

    def use_item(self):
        self.owner.is_using_item = True


class MeleeWeapon(Weapon, abc.ABC):
    def __init__(self, owner, price, damage, size, span, speed):
        super().__init__(owner, price, damage, size, speed)
        self.attack_progress = 1
        self.span = span

    #slash
    def use(self):
        if not self.owner.is_using_item:
           return 0
        
        if self.attack_progress > self.span:
            self.attack_progress = 1
            self.owner.is_using_item = False
            return 0
        
        self.attack_progress += self.speed
        return self.span / 2 - self.attack_progress
    

class Projectile(pygame.sprite.Sprite, abc.ABC):
    def __init__(self, is_friendly, damage, direction, speed, coords):
        super().__init__()
        self.is_friendly = is_friendly #did greasy killer launch this projectile
        self.damage = damage
        self.direction = direction
        self.speed = speed
        self.coords = coords

        pygame.Surface.set_colorkey(self.image, (255, 255, 255))
        self.rect = self.image.get_rect(center = self.coords)


class BowProjectile(Projectile):
    def __init__(self, is_friendly, direction):
        self.image = pygame.image.load(config.BOW_PROJECTILE_ICON).convert_alpha()
        self.image = pygame.transform.scale(self.image, config.BOW_PROJECTILE_SIZE)
        super().__init__(is_friendly, config.BOW_PROJECTILE_DAMAGE, direction,
                         config.BOW_PROJECTILE_SPEED, self.owner.rect.center)


class RangedWeapon(Weapon, abc.ABC):
    @abc.abstractmethod
    def get_new_projectile(self):
        pass


    def __init__(self, owner, price, damage, size, speed):
        super().__init__(owner, price, damage, size, speed)
        
    #shoot
    def use(self):
        if not self.owner.is_using_item:
           return 0
        self.owner.is_using_item = False
        new_projectile = self.get_new_projectile()
        #
        #
        #
        return 0
        

class Bow(RangedWeapon):
    def __init__(self, owner):
        self.image = pygame.image.load(config.BOW_ICON).convert_alpha()
        pygame.Surface.set_colorkey(self.image, (255, 255, 255))

        price = -1 if 'bow' in config.STARTING_ITEMS else config.SHOP_ITEMS['bow']
        super().__init__(owner, price, config.BOW_PROJECTILE_DAMAGE, config.BOW_PROJECTILE_SIZE, config.BOW_PROJECTILE_SPEED)


    def get_new_projectile(self):
        direction_vector = tuple(a - b for a, b in zip(pygame.mouse.get_pos(), self.owner.rect.center))
        return BowProjectile(self.owner.is_friendly, direction_vector)


class Dagger(MeleeWeapon):
    def __init__(self, owner):
        self.image = pygame.image.load(config.DAGGER_ICON).convert_alpha()
        pygame.Surface.set_colorkey(self.image, (255, 255, 255))
    
        price = -1 if 'dagger' in config.STARTING_ITEMS else config.SHOP_ITEMS['dagger']
        super().__init__(owner, price, config.DAGGER_DAMAGE, config.DAGGER_SIZE, config.DAGGER_SPAN, config.DAGGER_SPEED)