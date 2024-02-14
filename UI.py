import pygame
import config
import time
import utils

def show_element(screen, width, height, props, color, radius):
    element = pygame.Surface((width, height))
    element_rect = element.get_rect(topleft = (props[0] * config.SCREEN_WIDTH, props[1] * config.SCREEN_HEIGHT))
    pygame.draw.rect(screen, #surface to draw on
                    color, #color of drawn rect
                    element_rect, #which rect to draw
                    border_radius = radius) #border radius
    return element_rect

def show_buttons(screen, objects):
    button_width, button_height = config.SCREEN_WIDTH / 4, config.SCREEN_HEIGHT / 12

    start_button_proportions = (1/6, 4.5/12)
    start_button = show_element(screen, button_width, button_height, start_button_proportions, 
                                config.MAIN_MENU_BUTTON_COLOR, config.MAIN_MENU_BUTTON_BORDER_RADIUS)
    objects['start_button'] = start_button

    quit_button_proportions = (1/6, 6.5/12)
    quit_button = show_element(screen, button_width, button_height, quit_button_proportions,
                               config.MAIN_MENU_BUTTON_COLOR, config.MAIN_MENU_BUTTON_BORDER_RADIUS)
    objects['quit_button'] = quit_button

def show_text(screen, objects, current_status):
    #start button text
    text = 'Continue' if current_status is utils.Status.paused else 'Start game'
    start_text = config.TEXT_FONT.render(text, True, config.MAIN_MENU_TEXT_COLOR)
    coordx = (2 * objects['start_button'].left + objects['start_button'].right) / 3
    coordy = (2 * objects['start_button'].top + objects['start_button'].bottom) / 3
    screen.blit(start_text, (coordx, coordy))

    #quit button text
    quit_text = config.TEXT_FONT.render('Quit', True, config.MAIN_MENU_TEXT_COLOR)
    coordx = (1.25 * objects['quit_button'].left + objects['quit_button'].right) / 2.25
    coordy = (2 * objects['quit_button'].top + objects['quit_button'].bottom) / 3
    screen.blit(quit_text, (coordx, coordy))

    #guide text
    coordx = objects['game_guide_window'].left + 10
    coordy = objects['game_guide_window'].top + 20
    utils.render_multi_line(screen, config.GAME_TUTORIAL, coordx, coordy, config.FONT_SIZE)

def show_menu(screen, objects, current_status):
    #main_menu
    main_menu_proportions = (1/8, 1/3)
    main_menu = show_element(screen,config.SCREEN_WIDTH / 3, config.SCREEN_HEIGHT / 3,
                             main_menu_proportions, config.MAIN_MENU_COLOR, config.MAIN_MENU_BORDER_RADIUS)
    objects['main_menu'] = main_menu 

    #buttons
    show_buttons(screen, objects)
    
    #guide
    game_guide_window_proportions = (1/2, 1/5)
    game_guide_window = show_element(screen, config.SCREEN_WIDTH / 2.5, 3 * config.SCREEN_HEIGHT // 5,
                                     game_guide_window_proportions, config.MAIN_MENU_COLOR, config.MAIN_MENU_BORDER_RADIUS)
    objects['game_guide_window'] = game_guide_window

    #text
    show_text(screen, objects, current_status)

    return current_status

def play_resume_animation(screen):
    background_props = (9/25, 4/9)
    bg_width, bg_height = config.SCREEN_WIDTH / 4, config.SCREEN_HEIGHT / 12
    background = show_element(screen, bg_width, bg_height, background_props, 
                              config.RESUME_BACKGROUND_COLOR, config.MAIN_MENU_BUTTON_BORDER_RADIUS)
    
    #print 3
    start_text = config.RESUME_FONT.render('3', True, config.RESUME_TEXT_COLOR)
    coordx = (background.left + background.right) / 2
    coordy = (2 * background.top + background.bottom) / 3
    screen.blit(start_text, (coordx, coordy))
    pygame.display.update()
    time.sleep(1)

    #print 2
    show_element(screen, bg_width, bg_height, background_props, 
                 config.RESUME_BACKGROUND_COLOR, config.MAIN_MENU_BUTTON_BORDER_RADIUS)
    start_text = config.RESUME_FONT.render('2', True, config.RESUME_TEXT_COLOR)
    screen.blit(start_text, (coordx, coordy))
    pygame.display.update()
    time.sleep(1)

    #print 1
    show_element(screen, bg_width, bg_height, background_props, 
                 config.RESUME_BACKGROUND_COLOR, config.MAIN_MENU_BUTTON_BORDER_RADIUS)
    start_text = config.RESUME_FONT.render('1', True, config.RESUME_TEXT_COLOR)
    screen.blit(start_text, (coordx, coordy))
    pygame.display.update()
    time.sleep(1)