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

def init_hero():
    hero_group = pygame.sprite.GroupSingle()
    hero = entities.GreasyKiller((config.screen_width / 2, config.screen_height / 2))
    dagger_group = pygame.sprite.GroupSingle()
    dagger = weapons.Dagger(hero)
    dagger_group.add(dagger)
    hero.items.append(dagger_group)
    hero_group.add(hero)
    return hero_group

def init_screen():
    screen = pygame.display.set_mode((config.screen_width, config.screen_height), pygame.FULLSCREEN | pygame.SCALED)
    pygame.display.set_caption("Greasy Kingx")
    pygame.display.set_icon(pygame.image.load(config.game_icon).convert_alpha())
    return screen

def render_multi_line(screen, text, x, y, font_size):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        current_line = config.text_font.render(line, True, config.main_menu_text_color) 
        screen.blit(current_line, (x, y + font_size*i))

def rotate(reference_sprite, target_sprite, reference_point):
    dir_x = reference_point[0] - reference_sprite.coords[0]
    dir_y = reference_point[1] - reference_sprite.coords[1]

    angle = (180 / math.pi) * -math.atan2(dir_y, dir_x)

    target_sprite.image = pygame.transform.rotate(target_sprite._original_image, int(angle))
    target_sprite.rect = target_sprite.image.get_rect(center = target_sprite.coords)

def get_mov_vector(keys):
    mov_vector = [0, 0]

    if keys[pygame.K_a]:
        mov_vector[0] -= config.hero_movement_speed
    if keys[pygame.K_d]:
        mov_vector[0] += config.hero_movement_speed
    if keys[pygame.K_w]:
        mov_vector[1] -= config.hero_movement_speed
    if keys[pygame.K_s]:
        mov_vector[1] += config.hero_movement_speed

    return mov_vector