import pygame
import utils
import UI
import config
import random
import entities

def fix_wave(current_wave, remaining_enemies, current_enemies, timer):
    if not remaining_enemies and not current_enemies:
        current_wave = min(current_wave + 1, config.MAX_WAVE)
        remaining_enemies = config.WAVE_ENEMIES[current_wave].copy()
        current_enemies = [] #list of tuples: (enemy, spawn time)
        random.shuffle(remaining_enemies)

    if remaining_enemies and timer % (config.FRAMERATE * config.ENEMY_SPAWN_RATE) == 0:
        current_enemies.append((entities.entity_factory(remaining_enemies[0]), timer))
        remaining_enemies = remaining_enemies[1:]

    return (current_wave, remaining_enemies, current_enemies)

def manage_enemy_actions(current_enemies, hero, screen, timer):
    for enemy in current_enemies:
        enemy[0].aim(hero.coords)
        enemy[0].move(hero.coords)
        screen.blit(enemy[0].image, enemy[0].rect)
        if enemy[0].active_item is None:
            continue

        screen.blit(enemy[0].active_item.image, enemy.active_item.rect)
        if (timer - enemy[1]) % enemy[0].attack_speed == 0:
            enemy.active_item.use_item()
        enemy.aim(hero.coords)

def manage_hero_actions(screen, hero):
    keys = pygame.key.get_pressed()
    hero.aim()
    hero.move(keys)
    screen.blit(hero.active_item.image, hero.active_item.rect)
    screen.blit(hero.image, hero.rect)

def manage_collisions(hero, current_enemies):
    for enemy in current_enemies:
        if pygame.Rect.colliderect(hero.rect, enemy[0].rect):
            hero.health -= enemy[0].body_damage
            current_enemies.remove(enemy)
            if hero.health <= 0:
                return True
            

def process_game_iteration(hero, screen, current_status,
                           current_wave, remaining_enemies, current_enemies, timer):
    timer += 1
    if current_status is utils.Status.resuming:
        UI.play_resume_animation(screen)
        current_status = utils.Status.in_game

    UI.show_ingame_UI(screen, hero, current_wave, timer // 10)

    temp_result = fix_wave(current_wave, remaining_enemies, current_enemies, timer)
    current_wave, remaining_enemies, current_enemies = temp_result
    
    manage_enemy_actions(current_enemies, hero, screen, timer)
    manage_hero_actions(screen, hero)
    if manage_collisions(hero, current_enemies):
        current_status = utils.Status.dead

    return current_status, current_wave, remaining_enemies, current_enemies, timer

