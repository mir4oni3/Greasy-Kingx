import pygame
import utils
import UI

def process_game_iteration(hero, screen, current_status):
    keys = pygame.key.get_pressed()
    active_item = hero.sprite.items[hero.sprite.current_item]

    hero.sprite.aim(active_item)
    hero.sprite.move(keys)

    active_item.draw(screen)
    hero.draw(screen)

    if current_status is utils.Status.resuming:
        UI.play_resume_animation(screen)
        current_status = utils.Status.in_game

    return current_status

