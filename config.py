import pygame
pygame.init()
screen_width, screen_height = 1920, 1080
framerate = 60

game_icon = 'Greasy Kingx/gameIcon.PNG'
greasy_killer_icon = 'Greasy Kingx/greasyKillerIcon.PNG'
slickback_scoundrel_icon = 'Greasy Kingx/SlickBackScoundrel.PNG'

font_size = screen_width // 40

text_font = pygame.font.Font(None, font_size)

hero_movement_speed = 10

main_menu_color = (97, 102, 201)
main_menu_border_radius = 40

main_menu_button_color = (30, 34, 115)
main_menu_button_border_radius = 10

main_menu_text_color = (255, 255, 255)

game_tutorial = 'How to play:\nW,A,S,D - Movement\nMouse click - Shoot at cursor direction\nPress P at any time to pause\n'

resume_background_color = (156, 40, 201)
resume_font = pygame.font.Font(None, font_size)
resume_text_color = (255, 255, 255)

dagger_icon = 'Greasy Kingx/Dagger.PNG'