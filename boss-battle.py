import pygame
try: 
    from Tkinter import *
except ImportError:
    from tkinter import *

# RGB Colors
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

pygame.init()


# -------- Customizations ------------
# Display settings
display_width = 1440
display_height = 800

# Background color
background_color = black

# Button colors
button_color = grey
button_hover_color = yellow
input_color = white
input_hover = grey

# Game Title
game_title = "Star Wars: EpSIode 2019"

# Images
title_screen_img_path = "star_wars.png"
boss_image_path = "darth.png"
game_bg_path = "space-collision.jpg"

# Textfile
boss_filename = "boss-info.txt"
boss_info = open(boss_filename, 'r')
print(boss_info.read())

# Team names and images
team1_name = "One"
team1_image = ""

team2_name = "Two"
team2_image = ""

team3_name = "Three"
team3_image = ""
# --------------------------------

def title_image(x, y):
    gameDisplay.blit(title_img, (x, y))

def game_background(x, y):
    gameDisplay.blit(game_bg, (x, y))

def boss_image(x, y):
    gameDisplay.blit(boss_img, (x, y))

def render_text(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, width, height, hover_color, original_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, hover_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, original_color, (x,y,width,height))
    buttonText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = render_text(msg, buttonText, black)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    gameDisplay.fill(background_color)
    title_image(x, y)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play", 425, 550, 150, 50, button_hover_color, button_color, "play")
        button("Quit", 825, 550, 150, 50, button_hover_color, button_color, "quit")
        pygame.display.update()
        clock.tick(60)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(springgreen)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += 2

def game_loop():
    game = True
    gameDisplay.fill(background_color)
    game_background(0, 0)

    # --- Handling input boxes
    font = pygame.font.Font(None, 32)
    team_1_color_inactive = pygame.Color('ghostwhite')
    team_1_color_active = pygame.Color('gold1')
    team_1_color = team_1_color_inactive
    team_1_text = ''
    team_1_active = False
    team_2_color_inactive = pygame.Color('ghostwhite')
    team_2_color_active = pygame.Color('gold1')
    team_2_color = team_2_color_inactive
    team_2_text = ''
    team_2_active = False
    team_3_color_inactive = pygame.Color('ghostwhite')
    team_3_color_active = pygame.Color('gold1')
    team_3_color = team_3_color_inactive
    team_3_text = ''
    team_3_active = False

    # --- Boss health
    boss_1_health = 300
    boss_2_health = 300
    boss_3_health = 300

    # Bullets list
    bullet_list = pygame.sprite.Group()

    team_1_damage = 0
    team_2_damage = 0
    team_3_damage = 0

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
                        team_1_damage = int(team_1_text)
                        team_1_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_1_text = team_1_text[:-1]
                    else:
                        team_1_text += event.unicode
                if team_2_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 2: " + team_2_text)
                        team_2_damage = int(team_2_text)
                        team_2_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_2_text = team_2_text[:-1]
                    else:
                        team_2_text += event.unicode
                if team_3_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 3: " + team_3_text)
                        team_3_damage = int(team_3_text)
                        team_3_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_3_text = team_3_text[:-1]
                    else:
                        team_3_text += event.unicode
        game_background(0, 0)

        if team_1_damage > 0:
            bullet = Bullet()
            bullet.rect.x = 225
            bullet.rect.y = 100
            bullet_list.add(bullet)
            team_1_damage -= 1
        
        if team_2_damage > 0:
            bullet = Bullet()
            bullet.rect.x = 225
            bullet.rect.y = 350
            bullet_list.add(bullet)
            team_2_damage -= 1
        
        if team_3_damage > 0:
            bullet = Bullet()
            bullet.rect.x = 225
            bullet.rect.y = 625
            bullet_list.add(bullet)
            team_3_damage -= 1

        # Bullet spacing
        for i in range(0, 7):
            bullet_list.update()

        for bullet in bullet_list:
            if bullet.rect.x > display_width-375 and bullet.rect.y == 100:
                bullet_list.remove(bullet)
                boss_1_health -= 1
                if boss_1_health < 0:
                    boss_1_health = 0
            if bullet.rect.x > display_width-375 and bullet.rect.y == 350:
                bullet_list.remove(bullet)
                boss_2_health -= 1
                if boss_2_health < 0:
                    boss_2_health = 0
            if bullet.rect.x > display_width-375 and bullet.rect.y == 625:
                bullet_list.remove(bullet)
                boss_3_health -= 1
                if boss_3_health < 0:
                    boss_3_health = 0
        
        bullet_list.draw(gameDisplay)

        # --- Team items
        team_1 = pygame.Rect(150, 230, 150, 25)
        team_1_txtsurf = font.render(team_1_text, True, team_1_color)
        team_1_width = max(200, team_1_txtsurf.get_width() + 10)
        team_1.w = team_1_width
        gameDisplay.blit(team_1_txtsurf, (team_1.x+5, team_1.y+5))
        pygame.draw.rect(gameDisplay, team_1_color, team_1, 2)
        
        pygame.draw.rect(gameDisplay, team_1_color, (150, 30, 200, 175))

        team_2 = pygame.Rect(150, 500, 150, 25)
        team_2_txtsurf = font.render(team_2_text, True, team_2_color)
        team_2_width = max(200, team_2_txtsurf.get_width() + 10)
        team_2.w = team_2_width
        gameDisplay.blit(team_2_txtsurf, (team_2.x+5, team_2.y+5))
        pygame.draw.rect(gameDisplay, team_2_color, team_2, 2)
        
        pygame.draw.rect(gameDisplay, team_2_color, (150, 300, 200, 175))

        team_3 = pygame.Rect(150, 750, 150, 25)
        team_3_txtsurf = font.render(team_3_text, True, team_3_color)
        team_3_width = max(200, team_3_txtsurf.get_width() + 10)
        team_3.w = team_3_width
        gameDisplay.blit(team_3_txtsurf, (team_3.x+5, team_3.y+5))
        pygame.draw.rect(gameDisplay, team_3_color, team_3, 2)
        
        pygame.draw.rect(gameDisplay, team_3_color, (150, 550, 200, 175))

        # --- Boss
        bossText = pygame.font.Font("freesansbold.ttf", 20)

        team_1_boss = pygame.Rect(1000, 230, boss_1_health, 25)
        team_1_boss_max_health = pygame.Rect(1000, 230, 300, 25)
        pygame.draw.rect(gameDisplay, grey, team_1_boss_max_health)
        pygame.draw.rect(gameDisplay, darkred, team_1_boss)
        boss_image(1050, 30)
        boss_1_textSurf, boss_1_textRect = render_text("Health: " + str(boss_1_health), bossText, white)
        boss_1_textRect.center = ( (1000-75, 230+15) )
        gameDisplay.blit(boss_1_textSurf, boss_1_textRect)

        team_2_boss = pygame.Rect(1000, 500, boss_2_health, 25)
        team_2_boss_max_health = pygame.Rect(1000, 500, 300, 25)
        pygame.draw.rect(gameDisplay, darkgrey, team_2_boss_max_health)
        pygame.draw.rect(gameDisplay, darkred, team_2_boss)
        boss_image(1050, 300) 
        boss_2_textSurf, boss_2_textRect = render_text("Health: " + str(boss_2_health), bossText, white)
        boss_2_textRect.center = ( (1000-75, 500+15) )
        gameDisplay.blit(boss_2_textSurf, boss_2_textRect)

        team_3_boss = pygame.Rect(1000, 755, boss_3_health, 25)
        team_3_boss_max_health = pygame.Rect(1000, 755, 300, 25)
        pygame.draw.rect(gameDisplay, grey, team_3_boss_max_health)
        pygame.draw.rect(gameDisplay, darkred, team_3_boss)
        boss_image(1050, 555)
        boss_3_textSurf, boss_3_textRect = render_text("Health: " + str(boss_3_health), bossText, white)
        boss_3_textRect.center = ( (1000-75, 755+15) )
        gameDisplay.blit(boss_3_textSurf, boss_3_textRect)

        pygame.display.update()
        clock.tick(60)

# --------------- Main ---------------------------
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(game_title)

clock = pygame.time.Clock()

title_img = pygame.image.load(title_screen_img_path)
title_img = pygame.transform.scale(title_img, (display_width-500, display_height-300))

boss_img = pygame.image.load(boss_image_path).convert()
transColor = boss_img.get_at((0, 0))
boss_img.set_colorkey(transColor)
boss_img = pygame.transform.scale(boss_img, (175, 175))

game_bg = pygame.image.load(game_bg_path).convert()
game_bg = pygame.transform.scale(game_bg, (display_width, display_height))

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
