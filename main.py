import pygame

# intialize the pygame
pygame.init()

# creat thae scren
screen = pygame.display.set_mode((800, 600))
# Titles and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png' )
pygame.display.set_icon(icon)

#  Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - red green blue
    screen.fill((0, 0, 0)) # this code is used to screen colour
    pygame.display.update()  #this code is used to update screen