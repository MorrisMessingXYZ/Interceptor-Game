import pygame
import random
import math
import time

#initialise pygame
pygame.init()

#Title and Icon
pygame.display.set_caption("Interceptor")
icon = pygame.image.load("jet.png")
pygame.display.set_icon(icon)

#create window
screen = pygame.display.set_mode((600, 400))

#Player
playerImg = pygame.image.load("jet.png")
playerX = 284
playerY = 350
playerX_change = 0
playerY_change = 0

#Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,568)
enemyY = 10
enemyX_change = 0
enemyY_change = 0

#Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 320
bulletY_change = -2
bullet_state = "ready"

#Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

background = pygame.image.load("ocean-top-down.jpg")

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg, (x + 8, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if distance < 20:
        return True
    else:
        return False
def show_score(x,y):
    render_score = font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(render_score, (x, y))
running = True;

#Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #listen for Key
        #push Key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(playerX, playerY)
        #release Key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = -0

    screen.fill((38,38,38))
    screen.blit(background, (0,0))

    playerX += playerX_change
    enemyY += 0.5

    if playerX >= 568:
        playerX = 568
    elif playerX <= 0:
        playerX = 0

    if enemyY >= 400:
        enemyY = 0
        enemyX = random.randint(0,568)
        score += -1
        print(score)

    #Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 320
        bullet_state = "Ready"
        score += 1
        enemyY = 0
        enemyX = random.randint(0, 568)
        print(score)

    planeCollision = isCollision(enemyX, enemyY, playerX, playerY)
    if planeCollision:
        score = 0
        enemyY = 0
        enemyX = random.randint(0, 568)
        print(score)
        playerX = 284

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)

    #bullet movement
    if bullet_state == "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change
        if bulletY <= 0:
            bulletY = 320
            bullet_state = "Ready"

    time.sleep(0.001)
    pygame.display.update()