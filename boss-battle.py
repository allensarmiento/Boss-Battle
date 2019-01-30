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
input_color = white
input_hover = grey

game_title = "Star Wars: EpSIode 2019"

title_screen_img_path = "starwarslogo.png"

#Team names and images
team1_name = ""
team1_image = ""

team2_name = ""
team2_image = ""

team3_name = ""
team3_image = ""
#############################


# Function: title_image
# Call this function when we wnat to access the title image
def title_image(x, y):
    gameDisplay.blit(title_img, (x, y))

# Function: render_text
# Call this function whene we want to render the text
def render_text(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Function: button
# Call this function when we want to create a button
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


#Function: input_box
#Draw the input box
def input_box(x, y, width, height, hover_color, original_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    active = False

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, hover_color, (x,y,width,height))

        # If left click on the button, then call the action
        if click[0] == 1: #and action != None:
            active = True
    else:
        pygame.draw.rect(gameDisplay, original_color, (x,y,width,height))

# Function: game_intro
# Call this function to display the home screen
def game_intro():
    gameDisplay.fill(background_color)
    title_image(x, y)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play", 250, 600, 150, 50, button_hover_color, button_color, "play")
        button("Quit", 650, 600, 150, 50, button_hover_color, button_color, "quit")

        pygame.display.update()
        clock.tick(60)

# Fuction: game_loop
def game_loop():
    gameDisplay.fill(background_color)

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # NOTE: This is just here to check that we are changing scenes
        input_box(200, 300, 200, 50, input_hover, input_color)#meant to be an input button for points
        input_box(450, 300, 200, 50, input_hover, input_color)
        input_box(700, 300, 200, 50, input_hover, input_color)
        button("In Game Button", 450, 600, 200, 50, button_hover_color, button_color, "game")

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
title_img = pygame.transform.scale(title_img, (display_width-300, display_height-250))

# Location for the image to be placed
# NOTE: Change these values to center the image how you would like.
(x, y) = (150, 50)

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
