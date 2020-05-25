import pygame

# intialize the pygame
pygame.init()

# creat thae scren
screen = pygame.display.set_mode((800, 600))   # width height
# Titles and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png' )
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('p1.png')
playerX = 370
playerY = 480
playerX_change = 0
def player(X, Y):
    screen.blit(playerimg, (X, Y))  # Here this stape is youed to draw charector and passing two parameter


#  Game   Loop
running = True
while running:
    # RGB - red green blue
    screen.fill((0, 0, 0))  # this code is used to screen colour

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


     # Keybord control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()  #this code is used to update screen