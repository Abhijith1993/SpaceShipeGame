import pygame
import random
import math
from pygame import mixer

# intialize the pygame
pygame.init()

# baground pic
Background = pygame.image.load("b1.png")

# Baground sound
mixer.music.load("bg.wav")
mixer.music.play(-1)

# creat the scren
screen = pygame.display.set_mode((800, 600))  # width height
# Titles and icon
pygame.display.set_caption("Space Ship    By Abhijith")
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
num_of_enemies = 10
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('e1.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(1, 2))
    enemyX_change.append(2)
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

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

testX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
re_font = pygame.font.Font('freesansbold.ttf', 34)



def game_over_text():
    over_text = over_font.render("GAME OVER ", True, (255, 0, 0))
    re_text = re_font.render("Press Esc For New Game", True, (255, 0, 0))
    screen.blit(over_text,(200, 250))
    screen.blit(re_text, (200, 320))

def show_score(X, Y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (X, Y))


def player(X, Y):
    screen.blit(playerimg, (X, Y))  # Here this stape is youed to draw charector and passing two parameter


def enemy(X, Y, i):
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
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_ESCAPE:
                score_value = 0
                for i in range(num_of_enemies):
                    enemyX[i] = random.randint(0, 735)
                    enemyY[i] = random.randint(1, 2)



            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('sh.wav')
                    bullet_sound.play()
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

        # Gamer Over
        if  enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

            # collition
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1

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
    show_score(testX, testY)
    pygame.display.update()  # this code is used to update screen
