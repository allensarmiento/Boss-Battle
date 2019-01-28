import pygame


# RGB Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


###### CUSTOMIZATIONS #######
# variables to edit quickly #
display_width = 800
display_height = 600

background_color = black

game_title = "Star Wars: EpSIode 2019"

title_screen_img_path = "starwarslogo.png"
#############################


# When we want to access the title image, call this function
def title_image(x, y):
    gameDisplay.blit(title_img, (x, y))


# Set the window size and title
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(game_title)

# Set the game clock
clock = pygame.time.Clock()

# Title screen image
# NOTE: Change the value in order to center the image how you would like.
title_img = pygame.image.load(title_screen_img_path)
title_img = pygame.transform.scale(title_img, (display_width-100, display_height-100))

# Location for the image to be placed
# NOTE: Change these values to center the image how you would like.
(x, y) = (50, 50)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameDisplay.fill(background_color)
    title_image(x, y)

    pygame.display.update()
    clock.tick(60)

# If we reach this point, quit the program
pygame.quit()
quit()
