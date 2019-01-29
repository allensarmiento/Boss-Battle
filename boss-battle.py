import pygame


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
display_width = 1024
display_height = 768

background_color = black
button_color = grey
button_hover_color = yellow

game_title = "Star Wars: EpSIode 2019"

title_screen_img_path = "starwarslogo.png"
#############################


# When we want to access the title image, call this function
def title_image(x, y):
    gameDisplay.blit(title_img, (x, y))

# Render the text 
def render_text(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Set the window size and title
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(game_title)

# Set the game clock
clock = pygame.time.Clock()

# Title screen image
# NOTE: Change the value in order to center the image how you would like.
title_img = pygame.image.load(title_screen_img_path)
title_img = pygame.transform.scale(title_img, (display_width-300, display_height-250))

# Location for the image to be placed
# NOTE: Change these values to center the image how you would like.
(x, y) = (150, 50)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameDisplay.fill(background_color)
    title_image(x, y)

    # Keep track of mouse movement
    mouse = pygame.mouse.get_pos()

    # Play button
    if 250+150 > mouse[0] > 250 and 600+50 > mouse[1] > 600:
        pygame.draw.rect(gameDisplay, button_hover_color, (250, 600, 150, 50))
    else:
        pygame.draw.rect(gameDisplay, button_color, (250, 600, 150, 50))

    # Set the button text defaults
    buttonText = pygame.font.Font("freesansbold.ttf", 20)

    # Play button text
    textSurf, textRect = render_text("Play", buttonText)
    textRect.center = ( (250+(150/2)), (600+(50/2)) )
    gameDisplay.blit(textSurf, textRect)

    # Quit button
    if 650+150 > mouse[0] > 650 and 600+50 > mouse[1] > 600:
        pygame.draw.rect(gameDisplay, button_hover_color, (650, 600, 150, 50))
    else:
        pygame.draw.rect(gameDisplay, button_color, (650, 600, 150, 50))

    # Quit button text
    textSurf, textRect = render_text("Quit", buttonText)
    textRect.center = ( (650+(150/2)), (600+(50/2)) )
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()
    clock.tick(60)

# If we reach this point, quit the program
pygame.quit()
quit()
