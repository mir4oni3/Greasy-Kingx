import pygame
import entities
import config
from enum import Enum

class Status(Enum):
     in_game = 1
     in_menu = 2
     resuming = 3
     paused = 4

def init_hero():
    hero = pygame.sprite.GroupSingle()
    hero.add(entities.GreasyKiller((config.screen_width / 2, config.screen_height / 2)))
    return hero

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