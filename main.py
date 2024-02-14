import pygame
import config
import utils
import iteration
import event_handler
import UI
pygame.init()

screen = utils.init_screen()
hero = utils.init_hero()
clock = pygame.time.Clock()
background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

objects = {'hero' : hero.sprite}
current_status = utils.Status.in_menu

while True: #game loop
    for event in pygame.event.get():
       current_status = event_handler.handle_event(event, current_status, objects)

    if current_status is not utils.Status.paused:
        screen.blit(background, (0, 0))
        
    if current_status is utils.Status.in_menu or current_status is utils.Status.paused:
        current_status = UI.show_menu(screen, objects, current_status)

    elif current_status is utils.Status.in_game or current_status is utils.Status.resuming:
        current_status = iteration.process_game_iteration(hero, screen, current_status)

    pygame.display.update()
    clock.tick(config.FRAMERATE)