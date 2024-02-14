import utils
import pygame

def handle_button_press(event, current_status, objects):
    if event.button != 1:
        return current_status
    #use current item
    if current_status is utils.Status.in_game:
        objects['hero'].use_item()
    #start game button is pressed in the menu
    if current_status is utils.Status.in_menu and objects['start_button'].collidepoint(event.pos):
        return utils.Status.in_game
    #continue button is pressed in the pause menu
    elif current_status is utils.Status.paused and objects['start_button'].collidepoint(event.pos):
        return utils.Status.resuming
    #quit is pressed in the menu
    elif current_status in (utils.Status.in_menu, utils.Status.paused) and objects['quit_button'].collidepoint(event.pos):
        pygame.quit()
        exit()
    return current_status

def handle_keyboard_input(event, current_status, objects):
    #FOR TESTING 
    if event.key == pygame.K_ESCAPE:
        exit()
    #^^REMOVE LATER
        
    if event.key == pygame.K_p and current_status is utils.Status.in_game:
        current_status = utils.Status.paused
    elif event.key == pygame.K_p and current_status is utils.Status.paused:
        current_status = utils.Status.resuming
    return current_status

def handle_event(event, current_status, objects):
    if event.type == pygame.KEYDOWN:
        current_status = handle_keyboard_input(event, current_status, objects)
    if event.type == pygame.MOUSEBUTTONDOWN:
        current_status = handle_button_press(event, current_status, objects)
    
    return current_status
