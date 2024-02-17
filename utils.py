import pygame
import entities
import config
import weapons
import math
from enum import Enum

class Status(Enum):
     in_game = 1
     in_menu = 2
     resuming = 3
     paused = 4
     in_shop = 5
     dead = 6
     new_game = 7
     shop_request = 8

def init_starting_items(hero):
    for item_name in config.STARTING_ITEMS:
        item = None
        if item_name == 'dagger':
            item = weapons.Dagger(hero)
        if item_name == 'bow':
            item = weapons.Bow(hero)
        if not item:
            continue
        hero.items.append(item)

def init_hero():
    hero = entities.GreasyKiller((config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2))
    init_starting_items(hero)
    return hero

def init_screen():
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
    pygame.display.set_caption("Greasy Kingx")
    pygame.display.set_icon(pygame.image.load(config.GAME_ICON).convert_alpha())
    return screen

def render_multi_line(screen, text, x, y, font_size, color):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        current_line = config.TEXT_FONT.render(line, True, color) 
        screen.blit(current_line, (x, y + font_size*i))

def rotate_around_point(target, reference, angle):
    if angle == 0:
        return target
    
    angle_rad = (math.pi / 180) * angle
    new_x = math.cos(angle_rad) * (target[0] - reference[0]) - math.sin(angle_rad) * (target[1] - reference[1]) + reference[0]
    new_y = math.sin(angle_rad) * (target[0] - reference[0]) + math.cos(angle_rad) * (target[1] - reference[1]) + reference[1]
    return (new_x, new_y)

def rotate(target_sprite, point1, point2, additional_angle):
    dir_x = point2[0] - point1[0]
    dir_y = point2[1] - point1[1]

    angle = (180 / math.pi) * -math.atan2(dir_y, dir_x)
    angle += additional_angle

    target_sprite.image = pygame.transform.rotate(target_sprite._original_image, int(angle))
    target_sprite.rect = target_sprite.image.get_rect(center = target_sprite.coords)

def translate(point, vector_start, vector_end, pixel_count):
    '''Translate point in the direction of vector by pixel_count'''
    dir_x = vector_end[0] - vector_start[0]
    dir_y = vector_end[1] - vector_start[1]

    #normalize vector
    vector_length = (dir_x ** 2 + dir_y ** 2) ** 0.5
    dir_x /= vector_length
    dir_y /= vector_length

    #scale vector to target size
    dir_x *= pixel_count
    dir_y *= pixel_count

    #return translated point
    return (point[0] + dir_x, point[1] + dir_y)

def get_mov_vector(keys):
    mov_vector = [0, 0]

    if keys[pygame.K_a]:
        mov_vector[0] -= config.GREASY_KILLER_MOVEMENT_SPEED
    if keys[pygame.K_d]:
        mov_vector[0] += config.GREASY_KILLER_MOVEMENT_SPEED
    if keys[pygame.K_w]:
        mov_vector[1] -= config.GREASY_KILLER_MOVEMENT_SPEED
    if keys[pygame.K_s]:
        mov_vector[1] += config.GREASY_KILLER_MOVEMENT_SPEED

    return mov_vector