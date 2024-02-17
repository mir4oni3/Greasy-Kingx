import pygame
import config
import utils
from utils import Status
import iteration
import event_handler
import UI
pygame.init()

screen = utils.init_screen()
hero = utils.init_hero()
clock = pygame.time.Clock()
background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

current_wave = 0
remaining_enemies = []
current_enemies = []
objects = {'hero' : hero}
current_status = Status.in_menu
timer = 0

while True: #game loop
    for event in pygame.event.get():
       current_status = event_handler.handle_event(event, current_status, objects)

    if current_status not in (Status.paused, Status.in_shop, Status.dead):
        screen.blit(background, (0, 0))
        
    if current_status is Status.in_shop:
        UI.show_shop(screen, objects)

    elif current_status is Status.in_menu or current_status is Status.paused:
        UI.show_menu(screen, objects, current_status)

    elif current_status is Status.in_game or current_status is Status.resuming:
        result = iteration.process_game_iteration(hero, screen, current_status, current_wave,
                                                  remaining_enemies, current_enemies, timer)
        current_status, current_wave, remaining_enemies, current_enemies, timer = result
        UI.show_ingame_UI(screen, hero, current_wave, timer // 10)
    
    elif current_status is Status.dead:
        UI.show_death_screen(screen, timer // 10, objects)
    
    elif current_status is Status.new_game:
        hero = utils.init_hero()
        current_wave = 0
        remaining_enemies = []
        current_enemies = []
        objects = {'hero' : hero}
        current_status = Status.in_menu
        timer = 0
        
    pygame.display.update()
    clock.tick(config.FRAMERATE)