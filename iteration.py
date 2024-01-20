import pygame
import config
import utils
import menu

def get_mov_vector(keys):
    movement_vector = [0, 0]

    if keys[pygame.K_a]:
        movement_vector[0] -= config.hero_movement_speed
    if keys[pygame.K_d]:
        movement_vector[0] += config.hero_movement_speed
    if keys[pygame.K_w]:
        movement_vector[1] -= config.hero_movement_speed
    if keys[pygame.K_s]:
        movement_vector[1] += config.hero_movement_speed

    return movement_vector


def move(hero, keys):
    movement_vector = get_mov_vector(keys)
    
    #move
    hero.sprite.rect.left += movement_vector[0]
    hero.sprite.rect.top += movement_vector[1]

    #fix out of bounds
    hero.sprite.rect.left = max(hero.sprite.rect.left, 0)
    hero.sprite.rect.right = min(hero.sprite.rect.right, config.screen_width)
    hero.sprite.rect.top = max(hero.sprite.rect.top, 0)
    hero.sprite.rect.bottom = min(hero.sprite.rect.bottom, config.screen_height)

def process_game_iteration(hero, screen, current_status):
    keys = pygame.key.get_pressed()
    hero.draw(screen)
    if current_status == utils.Status.resuming:
        menu.play_resume_animation(screen)
        current_status = utils.Status.in_game
    move(hero, keys)
    return current_status

