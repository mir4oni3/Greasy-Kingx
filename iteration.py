import pygame
import utils
import UI
import config
import random
import entities
import items

def fix_wave(current_wave, remaining_enemies, current_enemies, current_status, timer):
    if not remaining_enemies and not current_enemies:
        current_wave = min(current_wave + 1, config.MAX_WAVE)
        remaining_enemies = config.WAVE_ENEMIES[current_wave].copy()
        current_enemies = []
        random.shuffle(remaining_enemies)
        current_status = utils.Status.shop_request if current_wave > 1 else current_status

    if remaining_enemies and timer % (config.FRAMERATE * config.ENEMY_SPAWN_RATE) == 0:
        new_enemy = entities.entity_factory(remaining_enemies[0])
        current_enemies.append(new_enemy)
        remaining_enemies = remaining_enemies[1:]

    return (current_wave, remaining_enemies, current_enemies, current_status)

def manage_enemy_actions(current_enemies, hero, screen):
    for enemy in current_enemies:
        for cur_proj in enemy.projectiles:
            manage_projectile(screen, cur_proj)
        enemy.aim(hero.coords)
        enemy.move(hero.coords)
        screen.blit(enemy.image, enemy.rect)
        if enemy.active_item is None:
            continue

        screen.blit(enemy.active_item.image, enemy.active_item.rect)
        enemy.active_item.use_item()
        enemy.aim(hero.coords)

def manage_projectile(screen, projectile):
    utils.rotate(projectile, (0, 0), projectile.direction, 0)
    projectile.coords = utils.translate(projectile.coords, (0, 0),
                                        projectile.direction, projectile.speed)
    projectile.rect = projectile.image.get_rect(center = projectile.coords)
    screen.blit(projectile.image, projectile.rect)

def manage_hero_actions(screen, hero):
    keys = pygame.key.get_pressed()
    hero.aim()
    hero.move(keys)
    for cur_proj in hero.projectiles:
        manage_projectile(screen, cur_proj)
    screen.blit(hero.active_item.image, hero.active_item.rect)
    screen.blit(hero.image, hero.rect)

def manage_body_colision(hero, enemy, current_enemies):
    if pygame.Rect.colliderect(hero.rect, enemy.rect):
            hero.health -= enemy.body_damage
            current_enemies.remove(enemy)
            if hero.health <= 0:
                return True
    return False

def manage_melee_colision(attacker, target, current_enemies):
    if not attacker.is_using_item or not attacker.is_using_item:
        return False
    if not isinstance(attacker.active_item, items.MeleeWeapon):
        return False
    if attacker.active_item.hit:
        return False
    if pygame.Rect.colliderect(attacker.active_item.rect, target.rect):
            if not attacker.active_item.hit:
                target.health -= attacker.active_item.damage
                attacker.active_item.hit = True
            if target.health <= 0 and not target.is_friendly:
                current_enemies.remove(target)
            if target.health <= 0 and target.is_friendly:
                return True
    return False

def manage_projectile_colision(attacker, targets):
    for current_target in targets:
        for projectile in attacker.projectiles:
            if pygame.Rect.colliderect(projectile.rect, current_target.rect):
                attacker.projectiles.remove(projectile)
                current_target.health -= projectile.damage
                if current_target.health <= 0 and current_target.is_friendly:
                    return True
                if current_target.health <= 0 and not current_target.is_friendly:
                    targets.remove(current_target)
    return False

def manage_collisions(hero, current_enemies):
    ''''Return True if Greasy Killer dies'''
    manage_projectile_colision(hero, current_enemies)
    for enemy in current_enemies:
        manage_melee_colision(hero, enemy, current_enemies)
        if manage_body_colision(hero, enemy, current_enemies):
            return True
        if manage_melee_colision(enemy, hero, None):
            return True
        if manage_projectile_colision(enemy, [hero]):
            return True
    return False

def process_game_iteration(hero, screen, current_status, current_wave,
                           remaining_enemies, current_enemies, timer):
    UI.show_ingame_UI(screen, hero, current_wave, current_enemies, timer // 10)

    temp_result = fix_wave(current_wave, remaining_enemies, current_enemies, current_status, timer)
    current_wave, remaining_enemies, current_enemies, current_status = temp_result
    
    manage_enemy_actions(current_enemies, hero, screen)
    manage_hero_actions(screen, hero)
    if manage_collisions(hero, current_enemies):
        current_status = utils.Status.dead

    if current_status is utils.Status.resuming:
        UI.play_resume_animation(screen)
        current_status = utils.Status.in_game
    else:
        timer += 1

    return current_status, current_wave, remaining_enemies, current_enemies, timer