import pygame
import config
import time
import utils

def show_element(screen, width, height, props, color, radius, name = None, objects = None):
    element = pygame.Surface((width, height))
    element_rect = element.get_rect(topleft = (props[0] * config.SCREEN_WIDTH, props[1] * config.SCREEN_HEIGHT))
    pygame.draw.rect(screen, #surface to draw on
                     color, #color of drawn rect
                     element_rect, #which rect to draw
                     border_radius = radius) #border radius
    if name and objects:
        objects[name] = element_rect
    else:
        return element_rect

def show_menu_buttons(screen, objects):
    #define button dimensions
    width, height = config.SCREEN_WIDTH / 4, config.SCREEN_HEIGHT / 12

    #show the start button
    show_element(screen, width, height, (1/6, 4.5/12), config.MAIN_MENU_BUTTON_COLOR,
                 config.MAIN_MENU_BUTTON_BORDER_RADIUS, 'start_button', objects)
    
    #show the quit button
    show_element(screen, width, height, (1/6, 6.5/12), config.MAIN_MENU_BUTTON_COLOR,
                 config.MAIN_MENU_BUTTON_BORDER_RADIUS, 'quit_button', objects)

def show_menu_text(screen, objects, current_status):
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
    show_element(screen,config.SCREEN_WIDTH / 3, config.SCREEN_HEIGHT / 3, (1/8, 1/3),
                 config.MAIN_MENU_COLOR, config.MAIN_MENU_BORDER_RADIUS, 'main_menu', objects)

    #buttons
    show_menu_buttons(screen, objects)
    
    #guide
    show_element(screen, config.SCREEN_WIDTH / 2.5, 3 * config.SCREEN_HEIGHT // 5, (1/2, 1/5),
                 config.MAIN_MENU_COLOR, config.MAIN_MENU_BORDER_RADIUS, 'game_guide_window', objects)

    #text
    show_menu_text(screen, objects, current_status)

def play_resume_animation(screen):
    background_props = (9/25, 4/9)
    bg_width, bg_height = config.SCREEN_WIDTH / 4, config.SCREEN_HEIGHT / 12
    
    for i in range(config.RESUME_DURATION):
        background = show_element(screen, bg_width, bg_height, background_props, 
                                  config.RESUME_BACKGROUND_COLOR, config.MAIN_MENU_BUTTON_BORDER_RADIUS)
        
        start_text = config.RESUME_FONT.render(str(config.RESUME_DURATION - i), True, config.RESUME_TEXT_COLOR)
        coordx = (background.left + background.right) / 2
        coordy = (2 * background.top + background.bottom) / 3
        screen.blit(start_text, (coordx, coordy))
        
        pygame.display.update()
        time.sleep(1)


def show_shop_text(screen, objects):
    close_button_text = config.TEXT_FONT.render('Close Shop', True, config.SHOP_TEXT_COLOR)
    coordx = (3 * objects['close_shop'].left + objects['close_shop'].right) / 4
    coordy = (2 * objects['close_shop'].top + objects['close_shop'].bottom) / 3
    screen.blit(close_button_text, (coordx, coordy))

    balance = config.TEXT_FONT.render('Balance:', True, config.SHOP_TEXT_COLOR)
    coordx = (2 * objects['balance'].left + objects['balance'].right) / 3
    coordy = (6 * objects['balance'].top + objects['balance'].bottom) / 7
    screen.blit(balance, (coordx, coordy))

    current_balance = config.TEXT_FONT.render(str(objects['hero'].balance), True, config.SHOP_TEXT_COLOR)
    coordx = (2 * objects['balance'].left + objects['balance'].right) / 3
    coordy = (objects['balance'].top + objects['balance'].bottom) / 2
    screen.blit(current_balance, (coordx, coordy))

def show_shop_buttons(screen, objects):
    #define button dimensions
    width, height = config.SCREEN_WIDTH / 5, config.SCREEN_HEIGHT / 10

    #show the start button
    show_element(screen, width, height, (1.1/8, 6.2/8), config.SHOP_BUTTON_COLOR,
                 config.SHOP_BUTTON_BORDER_RADIUS, 'close_shop', objects)
    
    #show balance background
    show_element(screen, width, height, (5.2/8, 6.2/8), config.SHOP_BUTTON_COLOR,
                 config.SHOP_BUTTON_BORDER_RADIUS, 'balance', objects)
    
def show_shop(screen, objects):
    #show shop background
    show_element(screen,3 * config.SCREEN_WIDTH // 4, 5 * config.SCREEN_HEIGHT // 8,
                 (1/8, 1/8), config.SHOP_COLOR, config.SHOP_BORDER_RADIUS, 'shop', objects)

    #show shop button background
    show_element(screen, 3 * config.SCREEN_WIDTH // 4, config.SCREEN_HEIGHT // 8, (1/8, 6.1/8),
                 config.SHOP_COLOR, config.SHOP_BORDER_RADIUS, 'shop_button_bg', objects)
    
    show_shop_buttons(screen, objects)
    show_shop_text(screen, objects)