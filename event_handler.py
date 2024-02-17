import utils
import pygame

def handle_mouse_input(event, current_status, objects):
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
    #close shop button pressed in shop
    elif current_status is utils.Status.in_shop and objects['close_shop'].collidepoint(event.pos):
        return utils.Status.resuming
    #quit button is pressed in the death screen
    elif current_status is utils.Status.dead and objects['death_quit'].collidepoint(event.pos):
        pygame.quit()
        exit()
    #quit button is pressed in the death screen
    elif current_status is utils.Status.dead and objects['death_new_game'].collidepoint(event.pos):
        return utils.Status.new_game
    
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
    elif event.key == pygame.K_SPACE and current_status is utils.Status.in_game:
        objects['hero'].use_item()

    #FOR TESTING
    elif event.key == pygame.K_o and current_status is utils.Status.in_game:
        current_status = utils.Status.in_shop
    elif event.key == pygame.K_o and current_status is utils.Status.in_shop:
        current_status = utils.Status.resuming
    elif event.key == pygame.K_i and current_status is utils.Status.in_game:
        current_status = utils.Status.dead
    elif event.key == pygame.K_i and current_status is utils.Status.dead:
        current_status = utils.Status.in_game
    #^^REMOVE LATER
        
    return current_status

def handle_event(event, current_status, objects):
    if event.type == pygame.KEYDOWN:
        current_status = handle_keyboard_input(event, current_status, objects)
    if event.type == pygame.MOUSEBUTTONDOWN:
        current_status = handle_mouse_input(event, current_status, objects)
    
    return current_status
