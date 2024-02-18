import pygame
import config
import time
import utils

def show_rect(screen, width, height, props, color, radius, name = None, objects = None):
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

def show_quick_items(screen, items, dest_rect):
    pass

def show_shop_items(screen, shop_items, hero_items):
    pass

def show_menu_buttons(screen, objects):
    #define button dimensions
    width, height = config.SCREEN_WIDTH / 4, config.SCREEN_HEIGHT / 12

    #show the start button
    show_rect(screen, width, height, (1/6, 4.5/12), config.MAIN_MENU_BUTTON_COLOR,
              config.MAIN_MENU_BUTTON_BORDER_RADIUS, 'start_button', objects)
    
    #show the quit button
    show_rect(screen, width, height, (1/6, 6.5/12), config.MAIN_MENU_BUTTON_COLOR,
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
    utils.render_multi_line(screen, config.GAME_TUTORIAL, coordx, coordy,
                            config.FONT_SIZE, config.MAIN_MENU_TEXT_COLOR)

def show_menu(screen, objects, current_status):
    #main_menu
    show_rect(screen,config.SCREEN_WIDTH / 3, config.SCREEN_HEIGHT / 3, (1/8, 1/3),
              config.MAIN_MENU_COLOR, config.MAIN_MENU_BORDER_RADIUS, 'main_menu', objects)

    #buttons
    show_menu_buttons(screen, objects)
    
    #guide
    show_rect(screen, config.SCREEN_WIDTH / 2.5, 3 * config.SCREEN_HEIGHT // 5, (1/2, 1/5),
              config.MAIN_MENU_COLOR, config.MAIN_MENU_BORDER_RADIUS, 'game_guide_window', objects)

    #text
    show_menu_text(screen, objects, current_status)

def play_resume_animation(screen):
    background_props = (9/25, 4/9)
    bg_width, bg_height = config.SCREEN_WIDTH / 4, config.SCREEN_HEIGHT / 12
    
    for i in range(config.RESUME_DURATION):
        background = show_rect(screen, bg_width, bg_height, background_props, 
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

    #show the close shop button
    show_rect(screen, width, height, (1.1/8, 6.2/8), config.SHOP_BUTTON_COLOR,
              config.SHOP_BUTTON_BORDER_RADIUS, 'close_shop', objects)
    
    #show balance background
    show_rect(screen, width, height, (5.2/8, 6.2/8), config.SHOP_BUTTON_COLOR,
              config.SHOP_BUTTON_BORDER_RADIUS, 'balance', objects)
    
def show_shop(screen, objects):
    #show shop background
    show_rect(screen,3 * config.SCREEN_WIDTH // 4, 5 * config.SCREEN_HEIGHT // 8,
              (1/8, 1/8), config.SHOP_COLOR, config.SHOP_BORDER_RADIUS, 'shop', objects)

    #show shop button background
    show_rect(screen, 3 * config.SCREEN_WIDTH // 4, config.SCREEN_HEIGHT // 8, (1/8, 6.1/8),
              config.SHOP_COLOR, config.SHOP_BORDER_RADIUS, 'shop_button_bg', objects)
    
    show_shop_buttons(screen, objects)
    show_shop_text(screen, objects)
    show_shop_items(screen, config.SHOP_ITEMS, objects['hero'].items)


def show_ingame_UI(screen, hero, current_wave, current_enemies, score):
    #show health bar
    show_rect(screen, config.HEALTHBAR_WIDTH, config.HEALTHBAR_HEIGHT, (0.01, 0.01),
              config.HEALTHBAR_BG_COLOR, config.HEALTHBAR_BORDER_RADIUS)
    show_rect(screen, (max(0, hero.health) / hero.max_health) * config.HEALTHBAR_WIDTH, config.HEALTHBAR_HEIGHT,
              (0.01, 0.01), config.HEALTHBAR_COLOR, config.HEALTHBAR_BORDER_RADIUS)
    
    #show score
    xcoord = config.SCREEN_WIDTH - max(len('Score:'), len(str(score))) * 0.013 * config.SCREEN_WIDTH
    text = 'Score:\n' + str(score) + '\nWave:\n' + str(current_wave)
    utils.render_multi_line(screen, text, xcoord, 5, config.FONT_SIZE, config.SCORE_COLOR)

    #show quick item list
    ycoord = (config.SCREEN_HEIGHT - config.QUICK_ITEMS_HEIGHT - 20) / config.SCREEN_HEIGHT
    quick_item_bg = show_rect(screen, config.QUICK_ITEMS_WIDTH, config.QUICK_ITEMS_HEIGHT, (0.234, ycoord),
                              config.QUICK_ITEMS_COLOR, config.QUICK_ITEMS_BORDER_RADIUS)
    
    #show current hero items
    show_quick_items(screen, hero.items, quick_item_bg)
    hb_width = 0.1 * config.SCREEN_WIDTH
    hb_height = 0.01 * config.SCREEN_HEIGHT

    #show enemy healthbars
    hb_color = config.HEALTHBAR_BG_COLOR
    hb_color1 = config.HEALTHBAR_COLOR
    radius = config.HEALTHBAR_BORDER_RADIUS
    for enemy in current_enemies:
        healthbar = pygame.Surface((hb_width, hb_height))
        coords = utils.translate(enemy.coords, (0, 0), (0, -1), config.ENTITY_SIZE[1] // 2)
        hb_rect = healthbar.get_rect(center = coords)
        pygame.draw.rect(screen, hb_color, hb_rect, border_radius = radius)
        cur_health = pygame.Surface((hb_width * (max(0, enemy.health) / enemy.max_health), hb_height))
        pygame.draw.rect(screen, hb_color1, cur_health.get_rect(midleft = hb_rect.midleft), border_radius = radius)



def show_basic_text(screen, objects, note, button_text_1, button_text_2, theme):
    if theme == 1:
        text_color = config.BASIC_SCREEN_TEXT_COLOR1
        button_text_color = config.BASIC_SCREEN_BUTTON_TEXT_COLOR1
    if theme == 2:
        text_color = config.BASIC_SCREEN_TEXT_COLOR2
        button_text_color = config.BASIC_SCREEN_BUTTON_TEXT_COLOR2

    #note
    death_text = config.TEXT_FONT.render(note, True, text_color)
    coordx = (3.75 * objects['basic_bg'].left + 1.5 * objects['basic_bg'].right) / 5.25
    coordy = objects['basic_bg'].top + 40
    screen.blit(death_text, (coordx, coordy))

    #button text 1
    text1 = config.TEXT_FONT.render(button_text_1, True, button_text_color)
    coordx = (2 * objects['basic_button_1'].left + 1.25 * objects['basic_button_1'].right) / 3.25
    coordy = (2 * objects['basic_button_1'].top + objects['basic_button_1'].bottom) / 3
    screen.blit(text1, (coordx, coordy))

    #button text 2
    text2 = config.TEXT_FONT.render(button_text_2, True, button_text_color)
    coordx = (2.5 * objects['basic_button_2'].left + objects['basic_button_2'].right) / 3.5
    coordy = (2 * objects['basic_button_2'].top + objects['basic_button_2'].bottom) / 3
    screen.blit(text2, (coordx, coordy))


def show_basic_screen(screen, objects, note, button_text1, button_text2, theme):
    if theme == 1:
        screen_color = config.BASIC_SCREEN_COLOR1
        button_color = config.BASIC_SCREEN_BUTTON_COLOR1
    if theme == 2:
        screen_color = config.BASIC_SCREEN_COLOR2
        button_color = config.BASIC_SCREEN_BUTTON_COLOR2

    #background
    show_rect(screen, config.BASIC_SCREEN_WIDTH, config.BASIC_SCREEN_HEIGHT, (1/4, 1/3),
              screen_color, config.BASIC_SCREEN_BORDER_RADIUS, 'basic_bg', objects)

    button_width = objects['basic_bg'].width / 3
    button_height = objects['basic_bg'].height / 5

    #button1
    show_rect(screen, button_width, button_height, (11/36, 11/20), button_color,
              config.BASIC_SCREEN_BUTTON_BORDER_RADIUS, 'basic_button_1', objects)
    
    #button2
    show_rect(screen, button_width, button_height, (19/36, 11/20), button_color,
              config.BASIC_SCREEN_BUTTON_BORDER_RADIUS, 'basic_button_2', objects)
    
    #text
    show_basic_text(screen, objects, note, button_text1, button_text2, theme)