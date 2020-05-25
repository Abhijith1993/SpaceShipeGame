import pygame
import random
import math

# intialize the pygame
pygame.init()

# baground pic
Background = pygame.image.load("b1.png")

# creat the scren
screen = pygame.display.set_mode((800, 600))  # width height
# Titles and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('p1.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('e1.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(1, 2))
    enemyX_change.append(1)
    enemyY_change.append(40)

# fire
# Ready - tou can't see the bullet
# fire - the bullet is move
bulletimg = pygame.image.load('bul.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

score = 0


def player(X, Y):
    screen.blit(playerimg, (X, Y))  # Here this stape is youed to draw charector and passing two parameter


def enemy(X, Y,i):
    screen.blit(enemyimg[i], (X, Y))  # Here this stape is youed to draw charector and passing two parameter


def fire_Bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# --------------- Game   Loop-----------------------------------
running = True
while running:
    # RGB - red green blue
    screen.fill((0, 0, 0))  # this code is used to screen colour
    # Background image
    screen.blit(Background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keybord control

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_Bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # space ship movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

            # collition
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(1, 2)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"  # bullet is shoot loop
    if bullet_state is "fire":
        fire_Bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)

    pygame.display.update()  # this code is used to update screen
