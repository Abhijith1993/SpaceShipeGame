import pygame

# intialize the pygame
pygame.init()

# creat thae scren
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ship game")

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
