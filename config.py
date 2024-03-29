import pygame
pygame.init()

#window
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
FRAMERATE = 60
GAME_ICON = 'Greasy Kingx/resource/GameIcon.PNG'

#entities
ENTITY_SIZE = (max(0.052 * SCREEN_WIDTH, 0.092 * SCREEN_HEIGHT), max(0.052 * SCREEN_WIDTH, 0.092 * SCREEN_HEIGHT))

GREASY_KILLER_ICON = 'Greasy Kingx/resource/GreasyKiller.PNG'
GREASY_KILLER_MOVEMENT_SPEED = 0.005 * SCREEN_WIDTH
GREASY_KILLER_HEALTH = 100

SLICKBACK_SCOUNDREL_ICON = 'Greasy Kingx/resource/SlickBackScoundrel.PNG'
SLICKBACK_SCOUNDREL_MOVEMENT_SPEED = 0.003 * SCREEN_WIDTH
SLICKBACK_SCOUNDREL_BODY_DAMAGE = 30
SLICKBACK_SCOUNDREL_HEALTH = 50
SLICKBACK_SCOUNDREL_GOLD = 20

DAGGER_MASTER_ICON = 'Greasy Kingx/resource/DaggerMaster.PNG'
DAGGER_MASTER_MOVEMENT_SPEED = 0.003 * SCREEN_WIDTH
DAGGER_MASTER_BODY_DAMAGE = 30
DAGGER_MASTER_HEALTH = 75
DAGGER_MASTER_GOLD = 30

FROSTWIND_MARKSMAN_ICON = 'Greasy Kingx/resource/FrostwindMarksman.PNG'
FROSTWIND_MARKSMAN_MOVEMENT_SPEED = 0.001 * SCREEN_WIDTH
FROSTWIND_MARKSMAN_BODY_DAMAGE = 50
FROSTWIND_MARKSMAN_HEALTH = 50
FROSTWIND_MARKSMAN_GOLD = 20

#items

#dagger
DAGGER_ICON = 'Greasy Kingx/resource/Dagger.PNG'
DAGGER_SHOP_ICON = 'Greasy Kingx/resource/DaggerShop.PNG'
DAGGER_SIZE = (0.104 * SCREEN_WIDTH, 0.018 * SCREEN_HEIGHT)
DAGGER_SPAN = 90
DAGGER_SPEED = 2
DAGGER_DAMAGE = 25

#bow
BOW_ICON = 'Greasy Kingx/resource/Bow.PNG'
BOW_SHOP_ICON = 'Greasy Kingx/resource/BowShop.PNG'
BOW_SIZE = (0.028 * SCREEN_WIDTH, 0.092 * SCREEN_HEIGHT)
BOW_COOLDOWN = 1000 #milliseconds
BOW_PROJECTILE_SPEED = 5
BOW_PROJECTILE_SIZE = (0.032 * SCREEN_WIDTH, 0.018 * SCREEN_HEIGHT)
BOW_PROJECTILE_DAMAGE = 20
BOW_PROJECTILE_ICON = 'Greasy Kingx/resource/BowProjectile.PNG'
ENEMY_BOW_PROJECTILE_ICON = 'Greasy Kingx/resource/BowProjectileEnemy.PNG'

#healing potion
POTION_ICON = 'Greasy Kingx/resource/HealingPotion.PNG'
POTION_SHOP_ICON = 'Greasy Kingx/resource/HealingPotionShop.PNG'
POTION_SIZE = (0.052 * SCREEN_WIDTH, 0.092 * SCREEN_HEIGHT)
POTION_HEAL_AMOUNT = GREASY_KILLER_HEALTH * 0.33

#text
FONT_SIZE = SCREEN_WIDTH // 40
TEXT_FONT = pygame.font.Font(None, FONT_SIZE)
GAME_TUTORIAL = 'How to play:\n\nW,A,S,D - Movement\n\nMouse Click\Spacebar - Shoot\Slash at\ncursor direction\n\nP - Pause\n\n0,...,9 - Select Item\n\n'

#score
SCORE_COLOR = (255, 148, 160)

#quick item list
QUICK_ITEMS_WIDTH = 0.6 * SCREEN_WIDTH
QUICK_ITEMS_HEIGHT = 0.150 * SCREEN_HEIGHT
QUICK_ITEMS_COLOR = (255, 138, 138)
QUICK_ITEMS_BORDER_RADIUS = 15

#health bar
HEALTHBAR_WIDTH = 0.234 * SCREEN_WIDTH
HEALTHBAR_HEIGHT = 0.037 * SCREEN_HEIGHT
HEALTHBAR_BG_COLOR = (255, 122, 122)
HEALTHBAR_COLOR = (255, 0, 0)
HEALTHBAR_BORDER_RADIUS = 40

#main menu
MAIN_MENU_COLOR = (97, 102, 201)
MAIN_MENU_BORDER_RADIUS = 40

MAIN_MENU_BUTTON_COLOR = (30, 34, 115)
MAIN_MENU_BUTTON_BORDER_RADIUS = 10

MAIN_MENU_TEXT_COLOR = (255, 255, 255)

#resume screen
RESUME_BACKGROUND_COLOR = (156, 40, 201)
RESUME_FONT = pygame.font.Font(None, FONT_SIZE)
RESUME_TEXT_COLOR = (255, 255, 255)
RESUME_DURATION = 3

#shop screen
SHOP_COLOR = (97, 102, 201)
SHOP_BORDER_RADIUS = 40
SHOP_BUTTON_COLOR = (30, 34, 115)
SHOP_BUTTON_BORDER_RADIUS = 10
SHOP_TEXT_COLOR = (255, 255, 255)
SHOP_ICON_SIZE = (100, 100)
ITEMS_PER_ROW = 10

#basic screen
BASIC_SCREEN_WIDTH = 0.5 * SCREEN_WIDTH
BASIC_SCREEN_HEIGHT = 0.33 * SCREEN_HEIGHT
BASIC_SCREEN_BORDER_RADIUS = 40
BASIC_SCREEN_BUTTON_BORDER_RADIUS = 10

BASIC_SCREEN_COLOR1 = (255, 0, 0)
BASIC_SCREEN_TEXT_COLOR1 = (0, 0, 0)
BASIC_SCREEN_BUTTON_COLOR1 = (0, 0, 0)
BASIC_SCREEN_BUTTON_TEXT_COLOR1 = (255, 255, 255)

BASIC_SCREEN_COLOR2 = (97, 102, 201)
BASIC_SCREEN_TEXT_COLOR2 = (255, 255, 255)
BASIC_SCREEN_BUTTON_COLOR2 = (30, 34, 115)
BASIC_SCREEN_BUTTON_TEXT_COLOR2 = (255, 255, 255)

#items
STARTING_ITEMS = ['dagger', 'bow', 'potion']

SHOP_ITEMS = {'dagger' : 10, 'bow' : 300, 'healing_potion' : 50} #item : price

UPGRADES = {'dagger_size' : 30, 'dagger_speed' : 40, 'dagger_span' : 30, 'dagger_damage' : 40,
            'bow_projectile_speed' : 100, 'bow_projectile_damage' : 100} #item : price


#wave   {wave : list of codes for each enemy in wave} ( Note : codes are in entities.py )
MAX_WAVE = 50
WAVE_ENEMIES = {wave : [3] * wave for wave in range(1, MAX_WAVE + 1)}
ENEMY_SPAWN_RATE = 5 #one enemy spawns every 5 seconds
GOLD_ON_WAVE_COMPLETION = 10