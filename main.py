import pygame
pygame.init()
import config
import utils
import iteration

screen = utils.init_screen()
hero = utils.init_hero()
clock = pygame.time.Clock()
background = pygame.Surface((config.screen_width, config.screen_height))

rects = {}
in_menu = True
currentStatus = utils.Status.in_menu

while True: #game loop
    for event in pygame.event.get():
       currentStatus = utils.handle_event(event, currentStatus, rects)

    screen.blit(background, (0, 0))
    
    if currentStatus is utils.Status.in_menu:
        utils.show_menu(screen, rects)
    elif currentStatus is utils.Status.in_game:
        iteration.process_game_iteration(hero, screen)
    elif currentStatus is utils.Status.paused:
        pass#TBI

    pygame.display.update()
    clock.tick(config.framerate)
