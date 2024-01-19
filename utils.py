import pygame
import entities
import config
from enum import Enum

class Status(Enum):
     in_game = 1
     in_menu = 2
     paused = 3

def handle_button_press(event, currentStatus, rects):
     #start game button is pressed in the menu
    if currentStatus is Status.in_menu and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and rects['start_button'].collidepoint(event.pos):
            currentStatus = Status.in_game
    #quit is pressed in the menu
    if currentStatus is Status.in_menu and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and rects['quit_button'].collidepoint(event.pos):
            pygame.quit()
            exit()
    return currentStatus

def handle_event(event, currentStatus, rects):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    currentStatus = handle_button_press(event, currentStatus, rects)
    
    return currentStatus

def init_hero():
    hero = pygame.sprite.GroupSingle()
    hero.add(entities.GreasyKiller((config.screen_width / 2, config.screen_height / 2)))
    return hero

def init_screen():
    screen = pygame.display.set_mode((config.screen_width, config.screen_height), pygame.FULLSCREEN | pygame.SCALED)
    pygame.display.set_caption("Greasy Kingx")
    pygame.display.set_icon(pygame.image.load(config.game_icon).convert_alpha())
    return screen

def show_element(screen, width, height, props, color, radius):
    element = pygame.Surface((width, height))
    element_rect = element.get_rect(topleft = (props[0] * config.screen_width, props[1] * config.screen_height))
    pygame.draw.rect(screen, #surface to draw on
                    color, #color of drawn rect
                    element_rect, #which rect to draw
                    border_radius = radius) #border radius
    return element_rect

def show_menu(screen, rects):
    #main_menu
    main_menu_proportions = (1/3, 1/3)
    main_menu = show_element(screen,config.screen_width / 3, config.screen_height / 3,
                             main_menu_proportions, config.main_menu_color, config.main_menu_border_radius)
    rects['main_menu'] = main_menu 

    #buttons
    button_width, button_height = config.screen_width / 4, config.screen_height / 12

    start_button_proportions = (9/24, 4.5/12)
    start_button = show_element(screen, button_width, button_height, start_button_proportions, 
                                config.main_menu_button_color, config.main_menu_button_border_radius)
    rects['start_button'] = start_button

    quit_button_proportions = (9/24, 6.5/12)
    quit_button = show_element(screen, button_width, button_height, quit_button_proportions,
                               config.main_menu_button_color, config.main_menu_button_border_radius)
    rects['quit_button'] = quit_button

    #start button text
    start_text = config.text_font.render('Start game', True, config.main_menu_text_color)
    coordx = (2 * start_button.left + start_button.right) / 3
    coordy = (2 * start_button.top + start_button.bottom) / 3
    screen.blit(start_text, (coordx, coordy))

    #quit button text
    quit_text = config.text_font.render('Quit', True, config.main_menu_text_color)
    coordx = (1.25 * quit_button.left + quit_button.right) / 2.25
    coordy = (2 * quit_button.top + quit_button.bottom) / 3
    screen.blit(quit_text, (coordx, coordy))
    

   