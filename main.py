import pygame
import config
import entities
from sys import exit

pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Greasy Kingx")
pygame.display.set_icon(pygame.image.load(config.game_icon).convert_alpha())
clock = pygame.time.Clock()

background = pygame.Surface((config.screen_width, config.screen_height))

hero = pygame.sprite.GroupSingle()
hero.add(entities.GreasyKiller((config.screen_width / 2, config.screen_height / 2)))

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    screen.blit(background, (0, 0))
    hero.draw(screen)

    pygame.display.update()
    clock.tick(config.framerate)
