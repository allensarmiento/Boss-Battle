import pygame
try: 
    from Tkinter import *
except ImportError:
    from tkinter import *

pygame.init()

# RGB Colors
black = (0, 0, 0)
silver = (211, 211, 211)
darkgrey = (169, 169, 169)
grey = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


###### CUSTOMIZATIONS #######
# variables to edit quickly #
display_width = 1366
display_height = 768

background_color = black
button_color = grey
button_hover_color = yellow
input_color = white
input_hover = grey

game_title = "Star Wars: EpSIode 2019"

title_screen_img_path = "starwarslogo.png"
boss_image_path = "darth.png"

boss_filename = "boss-info.txt"
boss_info = open(boss_filename, 'r')
print(boss_info.read())

#Team names and images
team1_name = "One"
team1_image = ""

team2_name = "Two"
team2_image = ""

team3_name = "Three"
team3_image = ""
#############################


def render_text(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, width, height, hover_color, original_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, hover_color, (x,y,width,height))
        # If left click on the button, then call the action
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, original_color, (x,y,width,height))

    # Add the button
    buttonText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = render_text(msg, buttonText)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    gameDisplay.blit(textSurf, textRect)


def title_image(x, y):
    gameDisplay.blit(title_img, (x, y))

def game_intro():
    gameDisplay.fill(background_color)
    title_image(x, y)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play", 350, 550, 150, 50, button_hover_color, button_color, "play")
        button("Quit", 800, 550, 150, 50, button_hover_color, button_color, "quit")

        pygame.display.update()
        clock.tick(60)


def boss_image(x, y):
    gameDisplay.blit(boss_img, (x, y))

def game_loop():
    gameDisplay.fill(background_color)

    game = True

    # Handling input boxes
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

    # Boss health
    boss_1_health = 250
    boss_2_health = 250
    boss_3_health = 250

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Check for button clicks in the input boxes
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

            # Read keyboard presses. This only reads one keyboard press at
            # a time.
            if event.type == pygame.KEYDOWN:
                if team_1_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 1: " + team_1_text)
                        damage_amount = int(team_1_text)
                        boss_1_health -= damage_amount
                        if boss_1_health < 0:
                            boss_1_health = 0
                        team_1_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_1_text = team_1_text[:-1]
                    else:
                        team_1_text += event.unicode

                if team_2_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 2: " + team_2_text)
                        damage_amount = int(team_2_text)
                        boss_2_health -= damage_amount
                        if boss_2_health < 0:
                            boss_2_health = 0
                        team_2_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_2_text = team_2_text[:-1]
                    else:
                        team_2_text += event.unicode

                if team_3_active:
                    if event.key == pygame.K_RETURN:
                        print("Team 3: " + team_3_text)
                        damage_amount = int(team_3_text)
                        boss_3_health -= damage_amount
                        if boss_3_health < 0:
                            boss_3_health = 0
                        team_3_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        team_3_text = team_3_text[:-1]
                    else:
                        team_3_text += event.unicode

        gameDisplay.fill((30, 30, 30))

        # Displaying team 1 items
        team_1 = pygame.Rect(100, 225, 150, 25)
        team_1_txtsurf = font.render(team_1_text, True, team_1_color)
        team_1_width = max(200, team_1_txtsurf.get_width() + 10)
        team_1.w = team_1_width
        gameDisplay.blit(team_1_txtsurf, (team_1.x+5, team_1.y+5))
        pygame.draw.rect(gameDisplay, team_1_color, team_1, 2)
        # Team 1 team icon box
        pygame.draw.rect(gameDisplay, team_1_color, (100, 25, 200, 175))

        # Displaying team 2 items
        team_2 = pygame.Rect(100, 475, 150, 25)
        team_2_txtsurf = font.render(team_2_text, True, team_2_color)
        team_2_width = max(200, team_2_txtsurf.get_width() + 10)
        team_2.w = team_2_width
        gameDisplay.blit(team_2_txtsurf, (team_2.x+5, team_2.y+5))
        pygame.draw.rect(gameDisplay, team_2_color, team_2, 2)
        # Team 2 team icon box
        pygame.draw.rect(gameDisplay, team_2_color, (100, 275, 200, 175))

        # Displaying team 3 items
        team_3 = pygame.Rect(100, 725, 150, 25)
        team_3_txtsurf = font.render(team_3_text, True, team_3_color)
        team_3_width = max(200, team_3_txtsurf.get_width() + 10)
        team_3.w = team_3_width
        gameDisplay.blit(team_3_txtsurf, (team_3.x+5, team_3.y+5))
        pygame.draw.rect(gameDisplay, team_3_color, team_3, 2)
        # Team 3 team icon box
        pygame.draw.rect(gameDisplay, team_3_color, (100, 525, 200, 175))

        # Team 1 Boss
        team_1_boss = pygame.Rect(1100, 200, boss_1_health, 25)
        team_1_boss_max_health = pygame.Rect(1100, 200, 250, 25)
        pygame.draw.rect(gameDisplay, grey, team_1_boss_max_health, 2)
        pygame.draw.rect(gameDisplay, red, team_1_boss)
        boss_image(1100, 45)

        # Team 2 Boss
        team_2_boss = pygame.Rect(1100, 425, boss_2_health, 25)
        team_2_boss_max_health = pygame.Rect(1100, 425, 250, 25)
        pygame.draw.rect(gameDisplay, grey, team_2_boss_max_health, 2)
        pygame.draw.rect(gameDisplay, red, team_2_boss)
        boss_image(1100, 270) 

        # Team 3 Boss
        team_3_boss = pygame.Rect(1100, 675, boss_3_health, 25)
        team_3_boss_max_health = pygame.Rect(1100, 675, 250, 25)
        pygame.draw.rect(gameDisplay, grey, team_3_boss_max_health, 2)
        pygame.draw.rect(gameDisplay, red, team_3_boss)
        boss_image(1100, 520)

        pygame.display.update()
        clock.tick(60)


# Set the window size and title
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(game_title)

# Set the game clock
clock = pygame.time.Clock()

# Title screen image
# NOTE: Change the value in order to center the image how you would like.
title_img = pygame.image.load(title_screen_img_path)
title_img = pygame.transform.scale(title_img, (display_width-500, display_height-250))

boss_img = pygame.image.load(boss_image_path)
boss_img = pygame.transform.scale(boss_img, (150, 150))

# Location for the image to be placed
# NOTE: Change these values to center the image how you would like.
(x, y) = (display_width//6, display_height//10)

# Loop for intro screen
intro = True

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keep track of mouse movement
    mouse = pygame.mouse.get_pos()

    # Start the game intro
    game_intro()

# If we reach this point, quit the program
pygame.quit()
quit()
