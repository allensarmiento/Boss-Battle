import math
import pygame
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

# ----- RGB Colors -----
black = (0, 0, 0)
black = (0, 0, 0)
silver = (211, 211, 211)
darkgrey = (169, 169, 169)
grey = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
darkred = (204, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
springgreen = (51, 255, 51)
blue = (0, 0, 255)
lightblue = (0, 255, 255)
# ----- End of RGB Color -----

# Initialization
pygame.init()

# Scaling Factor
scale = 1.05

# ----- Customizations -----
# Game title
game_title = "Title Goes Here"

# Display settings
display_width = math.floor(1280 * scale)
display_height = math.floor(720 * scale)

# Background color
background_color = black

# Menu button colors
menu_button_color = grey
menu_button_hover_color = yellow 

# Title screen Images
title_screen_img_path = "Images/raceBackground.jpg"
boss_image_path = "Images/clock.png"
game_bg_path = "Images/raceBackground.jpg"

# Team names and images
team_1_name = "TEAM 1"
team_1_icon_path = "Images/rubiks-cube.png"
team_1_image_path = "Images/clock.png"

team_2_name = "TEAM 2"
team_2_icon_path = "Images/penguin.png"
team_2_boss_path = "Images/clock.png"

team_3_name = "TEAM 3"
team_3_icon_path = "Images/music-note.png"
team_3_image_path = "Images/clock.png"

# Textfile
boss_filename = "boss-info.txt"
boss_info = open(boss_filename, 'r')
print(boss_info.read())
# TODO: Close the file

# Fonts
button_text = pygame.font.Font("freesansbold.ttf", 20)
basic_font = pygame.font.Font(None, 32)
bossText = pygame.font.Font("freesansbold.ttf", 20)

# Team icon box colors
team_1_color_inactive = pygame.Color('ghostwhite')
team_1_color_active = pygame.Color('gold1')
team_2_color_inactive = pygame.Color('ghostwhite')
team_2_color_active = pygame.Color('gold1')
team_3_color_inactive = pygame.Color('ghostwhite')
team_3_color_active = pygame.Color('gold1')
# ----- End of Customizations -----

# display_image: Blits an image given the x and y coordinates
def display_image(image_name, x, y):
    gameDisplay.blit(image_name, (x, y))

# render_text: Renders a text given the font style and color
def render_text(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

# menu_button: Creates a menu button with specified colors and actions
def menu_button(text, x, y, width, height, default_color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
        pygame.draw.rect(gameDisplay, hover_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, default_color, (x, y, width, height))
    text_surface, text_rectangle = render_text(text, button_text, black)
    text_rectangle.center = ( (x+(width/2)), (y+(height/2)) )
    gameDisplay.blit(text_surface, text_rectangle)

# game_button: Creates an in-game button with functionality
def game_button(text, x, y, width, height, default_color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
        pygame.draw.rect(gameDisplay, hover_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "attack":
                game_loop()
    else:
        pygame.draw.rect(gameDisplay, default_color, (x, y, width, height))
    text_surface, text_rectangle = render_text(text, button_text, black)
    text_rectangle.center = ( (x + (width / 2)), (y + (height / 2)) )
    gameDisplay.blit(text_surface, text_rectangle)

# TODO
# change_display: Changes the display size
def change_display(): 
    pygame.display.set_mode((1600, 900))

# game_intro: Home screen of the game
def game_intro():
    # --- Button Locations ---
    button_y_coord = math.floor(550 * scale)
    button_width = math.floor(150 * scale)
    button_height = math.floor(50 * scale)

    play_x_coord = math.floor(300 * scale)
    quit_x_coord = math.floor(800 * scale)
    # --- End of Button Locations ---

    # create_button: Creates a menu button
    def create_button(text, x_coord, action):
        menu_button(text, x_coord, button_y_coord, button_width, button_height, menu_button_color, menu_button_hover_color, action)

    gameDisplay.fill(background_color)
    display_image(title_img, 0, 0)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        create_button("Play", play_x_coord, "play")
        create_button("Quit", quit_x_coord, "quit")

        pygame.display.update()
        clock.tick(60)

# Bullet: class for the attack animation
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(springgreen)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += 2

# game_loop: In-game mode
def game_loop():
    game = True
    gameDisplay.fill(background_color)
    display_image(game_bg, 0, 0)

    # --- Team colors and active ---
    team_1_color = team_1_color_inactive
    team_1_text = ''
    team_1_active = False
    team_2_color = team_2_color_inactive
    team_2_text = ''
    team_2_active = False
    team_3_color = team_3_color_inactive
    team_3_text = ''
    team_3_active = False 
    # --- End of team colors and active ---

    bullet_list = pygame.sprite.Group()

    # --- Health and damage dealt ---
    boss_max_health = 300
    boss_1_health = 300
    boss_2_health = 300
    boss_3_health = 300

    team_1_damage = 0
    team_2_damage = 0
    team_3_damage = 0
    # --- End of health and damage dealt

    # --- Game loop ---
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if team_1.collidepoint(event.pos):
                    team_1_active = True
                    team_1_color = team_1_color_active
                else:
                    team_1_active = False
                    team_1_color = team_1_color_inactive

                if team_2.collidepoint(event.pos):
                    team_2_active = True
                    team_2_color = team_2_color_active
                else:
                    team_2_active = False
                    team_2_color = team_2_color_inactive
                
                if team_3.collidepoint(event.pos):
                    team_3_active = True
                    team_3_color = team_3_color_active
                else:
                    team_3_active = False
                    team_3_color = team_3_color_inactive

            if event.type == pygame.KEYDOWN:
                if team_1_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 1: " + team_1_text)
                        try: 
                            team_1_damage = int(team_1_text)
                        except ValueError:
                            print("Only enter a number to deal damage.")
                        team_1_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_1_text = team_1_text[:-1]
                    else:
                        team_1_text += event.unicode
                
                if team_2_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 2: " + team_2_text)
                        try: 
                            team_2_damage = int(team_2_text)
                        except ValueError:
                            print("Only enter a number to deal damage.")
                        team_2_text = '' 
                    elif event.key == pygame.K_BACKSPACE:
                        team_2_text = team_2_text[:-1]
                    else:
                        team_2_text += event.unicode

                if team_3_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 3: " + team_3_text)
                        try: 
                            team_3_damage = int(team_3_text)
                        except ValueError:
                            print("Only enter a number to deal damage.")
                        team_3_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_3_text = team_3_text[:-1]
                    else:
                        team_3_text += event.unicode
        
        display_image(game_bg, 0, 0)

        bullet_x_coord  = math.floor(225 * scale)

        team_1_bullet_y_coord = math.floor(100 * scale)
        if team_1_damage > 0:
            bullet = Bullet()
            bullet.rect.x = bullet_x_coord
            bullet.rect.y = team_1_bullet_y_coord
            bullet_list.add(bullet)
            team_1_damage -= 1
        elif team_1_damage < 0:
            if boss_1_health < boss_max_health:
                boss_1_health += 1
            team_1_damage += 1

        team_2_bullet_y_coord = math.floor(325 * scale)
        if team_2_damage > 0:
            bullet = Bullet()
            bullet.rect.x = bullet_x_coord
            bullet.rect.y = team_2_bullet_y_coord
            bullet_list.add(bullet)
            team_2_damage -= 1
        elif team_2_damage < 0:
            if boss_2_health < boss_max_health:
                boss_2_health += 1
            team_2_damage += 1
        
        team_3_bullet_y_coord = math.floor(550 * scale)
        if team_3_damage > 0:
            bullet = Bullet()
            bullet.rect.x = bullet_x_coord
            bullet.rect.y = team_3_bullet_y_coord
            bullet_list.add(bullet)
            team_3_damage -= 1
        elif team_3_damage < 0:
            if boss_3_health < boss_max_health:
                boss_3_health += 1
            team_3_damage += 1
        
        # Bullet spacing
        for i in range(0, 7):
            bullet_list.update()
        
        bullet_collide_point = math.floor(200 * scale)

        for bullet in bullet_list:
            # Team 1 Boss
            if bullet.rect.x > display_width - bullet_collide_point and bullet.rect.y == team_1_bullet_y_coord:
                bullet_list.remove(bullet)
                boss_1_health -= 1
                if boss_1_health < 0:
                    boss_1_health = 0

            # Team 2 Boss
            if bullet.rect.x > display_width - bullet_collide_point and bullet.rect.y == team_2_bullet_y_coord:
                bullet_list.remove(bullet)
                boss_2_health -= 1
                if boss_2_health < 0:
                    boss_2_health = 0
            
            # Team 3 Boss
            if bullet.rect.x > display_width - bullet_collide_point and bullet.rect.y == team_3_bullet_y_coord:
                bullet_list.remove(bullet)
                boss_3_health -= 1
                if boss_3_health < 0:
                    boss_3_health = 0
            
        bullet_list.draw(gameDisplay)

        # Team items: Icon box, input box
        icon_x_coord = math.floor(100 * scale)
        attack_x_coord = math.floor(315 * scale)
        team_name_x_coord = math.floor( (icon_x_coord + 325) * scale)

        # ----- Team 1 -----
        team_1_icon_y_coord = math.floor(15 * scale)
        team_1_input_y_coord = math.floor(team_1_icon_y_coord + 185 * scale)
        team_1_name_y_coord = math.floor(team_1_icon_y_coord + 15 * scale)

        pygame.draw.rect(gameDisplay, team_1_color, (icon_x_coord, team_1_icon_y_coord, math.floor(200 * scale), math.floor(175 * scale)))
        display_image(team_1_icon_img, icon_x_coord, team_1_icon_y_coord)

        team_1_textSurf, team_1_textRect = render_text("TEAM 1", bossText, white)
        team_1_textRect.center = ( (team_name_x_coord, team_1_name_y_coord) )
        gameDisplay.blit(team_1_textSurf, team_1_textRect)

        team_1 = pygame.Rect(icon_x_coord, team_1_input_y_coord, math.floor(150 * scale), math.floor(25 * scale))
        team_1_txtsurf = basic_font.render(team_1_text, True, team_1_color)
        team_1_width = max(math.floor(200 * scale), team_1_txtsurf.get_width() + 10)
        team_1.w = team_1_width
        gameDisplay.blit(team_1_txtsurf, (team_1.x+5, team_1.y+5))
        pygame.draw.rect(gameDisplay, team_1_color, team_1, 2)
        game_button("Attack", attack_x_coord, team_1_input_y_coord, 80, 25, white, darkred, "attack")
        # ----- End of Team 1 ----- 

        # ----- Team 2 -----
        team_2_icon_y_coord = math.floor(250 * scale)
        team_2_input_y_coord = math.floor(team_2_icon_y_coord + 185 * scale)
        team_2_name_y_coord = math.floor(team_2_icon_y_coord + 15 * scale)

        pygame.draw.rect(gameDisplay, team_2_color, (icon_x_coord, team_2_icon_y_coord, math.floor(200 * scale), math.floor(175 * scale)))
        display_image(team_2_icon_img, icon_x_coord, team_2_icon_y_coord)

        team_2_textSurf, team_2_textRect = render_text("TEAM 2", bossText, white)
        team_2_textRect.center = ( (team_name_x_coord, team_2_name_y_coord) )
        gameDisplay.blit(team_2_textSurf, team_2_textRect)

        team_2 = pygame.Rect(icon_x_coord, team_2_input_y_coord, math.floor(150 * scale), math.floor(25 * scale))
        team_2_txtsurf = basic_font.render(team_2_text, True, team_2_color)
        team_2_width = max(math.floor(200 * scale), team_2_txtsurf.get_width() + 10)
        team_2.w = team_2_width
        gameDisplay.blit(team_2_txtsurf, (team_2.x+5, team_2.y+5))
        pygame.draw.rect(gameDisplay, team_2_color, team_2, 2)
        game_button("Attack", attack_x_coord, team_2_input_y_coord, 80, 25, white, darkred, "attack")
        # ----- End of Team 2 -----

        # ----- Team 3 -----
        team_3_icon_y_coord = math.floor(485 * scale)
        team_3_input_y_coord = math.floor(team_3_icon_y_coord + 185 * scale)
        team_3_name_y_coord = math.floor(team_3_icon_y_coord + 15 * scale)

        pygame.draw.rect(gameDisplay, team_3_color, (icon_x_coord, team_3_icon_y_coord, math.floor(200 * scale), math.floor(175 * scale)))
        display_image(team_3_icon_img, icon_x_coord, team_3_icon_y_coord)

        team_3_textSurf, team_3_textRect = render_text("TEAM 3", bossText, white)
        team_3_textRect.center = ( (team_name_x_coord, team_3_name_y_coord) )
        gameDisplay.blit(team_3_textSurf, team_3_textRect)
        
        team_3 = pygame.Rect(icon_x_coord, team_3_input_y_coord, math.floor(150 * scale), math.floor(25 * scale))
        team_3_txtsurf = basic_font.render(team_3_text, True, team_3_color)
        team_3_width = max(math.floor(200 * scale), team_3_txtsurf.get_width() + 10)
        team_3.w = team_3_width
        gameDisplay.blit(team_3_txtsurf, (team_3.x+5, team_3.y+5))
        pygame.draw.rect(gameDisplay, team_3_color, team_3, 2)
        game_button("Attack", attack_x_coord, team_3_input_y_coord, 80, 25, white, darkred, "attack")
        # ----- End of Team 3 -----

        # Boss items: Boss icon, health text, health bar
        boss_x_coord = math.floor(1000 * scale)

        # --- Team 1 Boss 
        boss_1_icon_y_coord = math.floor(15 * scale)
        boss_1_input_y_coord = math.floor(200 * scale)

        display_image(team_1_boss_img, boss_x_coord, boss_1_icon_y_coord)

        boss_1_textSurf, boss_1_textRect = render_text("Health: " + str(boss_1_health), bossText, white)
        boss_1_textRect.center = ( (boss_x_coord-50-75, boss_1_input_y_coord) )
        gameDisplay.blit(boss_1_textSurf, boss_1_textRect)

        team_1_boss = pygame.Rect(boss_x_coord-50, boss_1_input_y_coord, boss_1_health, 25)
        team_1_boss_max_health = pygame.Rect(boss_x_coord-50, boss_1_input_y_coord, 300, 25)
        pygame.draw.rect(gameDisplay, grey, team_1_boss_max_health)
        pygame.draw.rect(gameDisplay, darkred, team_1_boss)
        
        # --- Team 2 Boss
        boss_2_icon_y_coord = team_2_icon_y_coord
        boss_2_input_y_coord = team_2_input_y_coord

        display_image(team_2_boss_img, boss_x_coord, boss_2_icon_y_coord)

        boss_2_textSurf, boss_2_textRect = render_text("Health: " + str(boss_2_health), bossText, white)
        boss_2_textRect.center = ( (boss_x_coord-50-75, boss_2_input_y_coord) )
        gameDisplay.blit(boss_2_textSurf, boss_2_textRect)

        team_2_boss = pygame.Rect(boss_x_coord-50, boss_2_input_y_coord, boss_2_health, 25)
        team_2_boss_max_health = pygame.Rect(boss_x_coord-50, boss_2_input_y_coord, 300, 25)
        pygame.draw.rect(gameDisplay, darkgrey, team_2_boss_max_health)
        pygame.draw.rect(gameDisplay, darkred, team_2_boss)
        
        # --- Team 3 Boss
        boss_3_icon_y_coord = team_3_icon_y_coord
        boss_3_input_y_coord = team_3_input_y_coord

        display_image(team_3_boss_img, boss_x_coord, boss_3_icon_y_coord)

        boss_3_textSurf, boss_3_textRect = render_text("Health: " + str(boss_3_health), bossText, white)
        boss_3_textRect.center = ( (boss_x_coord-50-75, boss_3_input_y_coord) )
        gameDisplay.blit(boss_3_textSurf, boss_3_textRect)

        team_3_boss = pygame.Rect(boss_x_coord-50, boss_3_input_y_coord, boss_3_health, 25)
        team_3_boss_max_health = pygame.Rect(boss_x_coord-50, boss_3_input_y_coord, 300, 25)
        pygame.draw.rect(gameDisplay, grey, team_3_boss_max_health)
        pygame.draw.rect(gameDisplay, darkred, team_3_boss)

        pygame.display.update()
        clock.tick(60)
    # --- End of game loop ---

# --------------- Main ---------------------------
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(game_title)

clock = pygame.time.Clock()

# Title Image
title_img = pygame.image.load(title_screen_img_path)
title_img = pygame.transform.scale(title_img, (display_width, display_height))
#title_img = pygame.transform.scale(title_img, (display_width - math.floor(370 * scale), display_height - math.floor(222 * scale)))

# Default Boss Image
boss_img = pygame.image.load(boss_image_path).convert()
transColor = boss_img.get_at((0, 0))
boss_img.set_colorkey(transColor)
boss_img = pygame.transform.scale(boss_img, (math.floor(175 * scale), math.floor(175 * scale)))

# Game Background
game_bg = pygame.image.load(game_bg_path).convert()
game_bg = pygame.transform.scale(game_bg, (display_width, display_height))

# --- Team 1 Icon and Box Image ---
team_1_icon_img = pygame.image.load(team_1_icon_path)
team_1_icon_img = pygame.transform.scale(team_1_icon_img, (math.floor(200 * scale), math.floor(175 * scale)))
team_1_boss_img = pygame.image.load(team_1_image_path).convert()
team_1_boss_img = pygame.transform.scale(team_1_boss_img, (math.floor(200 * scale), math.floor(175 * scale)))
#team_1_boss_hit_img = pygame.image.load(team_1_hit_image_path)
#team_1_boss_hit_img = pygame.transform.scale(team_1_hit_image_path, (175, 200))
# --- End of Team 1 Icon and Box Image --- 

# --- Team 2 Icon and Box Image ---
team_2_icon_img = pygame.image.load(team_2_icon_path)
team_2_icon_img = pygame.transform.scale(team_2_icon_img, (math.floor(200 * scale), math.floor(175 * scale)))
team_2_boss_img = pygame.image.load(team_2_boss_path)
team_2_boss_img = pygame.transform.scale(team_2_boss_img, (math.floor(200 * scale), math.floor(175 * scale)))
# --- End of Team 2 Icon and Box Image ---

# --- Team 3 Icon and Box Image ---
team_3_icon_img = pygame.image.load(team_3_icon_path)
team_3_icon_img = pygame.transform.scale(team_3_icon_img, (math.floor(200 * scale), math.floor(175 * scale)))
team_3_boss_img = pygame.image.load(team_3_image_path)
team_3_boss_img = pygame.transform.scale(team_3_boss_img, (math.floor(200 * scale), math.floor(175 * scale)))
# --- End of Team 3 Icon and Box Image ---

# Location for the image to be placed
(x, y) = (display_width//6, display_height//10)

intro = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse = pygame.mouse.get_pos()
    game_intro()

pygame.quit()
quit()
