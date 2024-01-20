import pygame
import config
import time
import utils

def show_element(screen, width, height, props, color, radius):
    element = pygame.Surface((width, height))
    element_rect = element.get_rect(topleft = (props[0] * config.screen_width, props[1] * config.screen_height))
    pygame.draw.rect(screen, #surface to draw on
                    color, #color of drawn rect
                    element_rect, #which rect to draw
                    border_radius = radius) #border radius
    return element_rect

def show_buttons(screen, rects):
    button_width, button_height = config.screen_width / 4, config.screen_height / 12

    start_button_proportions = (1/6, 4.5/12)
    start_button = show_element(screen, button_width, button_height, start_button_proportions, 
                                config.main_menu_button_color, config.main_menu_button_border_radius)
    rects['start_button'] = start_button

    quit_button_proportions = (1/6, 6.5/12)
    quit_button = show_element(screen, button_width, button_height, quit_button_proportions,
                               config.main_menu_button_color, config.main_menu_button_border_radius)
    rects['quit_button'] = quit_button

def show_text(screen, rects, current_status):
    #start button text
    text = 'Continue' if current_status is utils.Status.paused else 'Start game'
    start_text = config.text_font.render(text, True, config.main_menu_text_color)
    coordx = (2 * rects['start_button'].left + rects['start_button'].right) / 3
    coordy = (2 * rects['start_button'].top + rects['start_button'].bottom) / 3
    screen.blit(start_text, (coordx, coordy))

    #quit button text
    quit_text = config.text_font.render('Quit', True, config.main_menu_text_color)
    coordx = (1.25 * rects['quit_button'].left + rects['quit_button'].right) / 2.25
    coordy = (2 * rects['quit_button'].top + rects['quit_button'].bottom) / 3
    screen.blit(quit_text, (coordx, coordy))

    #guide text
    coordx = rects['game_guide_window'].left + 10
    coordy = rects['game_guide_window'].top + 20
    utils.render_multi_line(screen, config.game_tutorial, coordx, coordy, config.font_size)

def show_menu(screen, rects, current_status):
    #main_menu
    main_menu_proportions = (1/8, 1/3)
    main_menu = show_element(screen,config.screen_width / 3, config.screen_height / 3,
                             main_menu_proportions, config.main_menu_color, config.main_menu_border_radius)
    rects['main_menu'] = main_menu 

    #buttons
    show_buttons(screen, rects)
    
    #guide
    game_guide_window_proportions = (1/2, 1/5)
    game_guide_window = show_element(screen, config.screen_width / 2.5, 3 * config.screen_height // 5,
                                     game_guide_window_proportions, config.main_menu_color, config.main_menu_border_radius)
    rects['game_guide_window'] = game_guide_window

    #text
    show_text(screen, rects, current_status)

    return current_status

def play_resume_animation(screen):
    background_props = (9/25, 4/9)
    bg_width, bg_height = config.screen_width / 4, config.screen_height / 12
    background = show_element(screen, bg_width, bg_height, background_props, 
                              config.resume_background_color, config.main_menu_button_border_radius)
    
    #print 3
    start_text = config.resume_font.render('3', True, config.resume_text_color)
    coordx = (background.left + background.right) / 2
    coordy = (2 * background.top + background.bottom) / 3
    screen.blit(start_text, (coordx, coordy))
    pygame.display.update()
    time.sleep(1)

    #print 2
    show_element(screen, bg_width, bg_height, background_props, 
                 config.resume_background_color, config.main_menu_button_border_radius)
    start_text = config.resume_font.render('2', True, config.resume_text_color)
    screen.blit(start_text, (coordx, coordy))
    pygame.display.update()
    time.sleep(1)

    #print 1
    show_element(screen, bg_width, bg_height, background_props, 
                 config.resume_background_color, config.main_menu_button_border_radius)
    start_text = config.resume_font.render('1', True, config.resume_text_color)
    screen.blit(start_text, (coordx, coordy))
    pygame.display.update()
    time.sleep(1)