import pygame
import random
pygame.init()

#change these for diff settings
wide = 1280
tall = 720
size = 40
fps = 60
# how often it moves
f = 10
# Positions
x = int(wide/4)
y = int(tall/2)
print(f"snake starting at {x}, {y}, FPS = {fps} Movement Per second = {fps/f}, canvas = {wide, tall} size = {size} win len = {wide/size * tall/size}")
pastX = [x]
pastY = [y]
apX = random.randrange(0, wide/size, 1) * size
apY = random.randrange(0, tall/size, 1) * size
dir = 4
# Random
fruit = False
done = False
color = (0, 128, 255)
aColor = (255, 0, 0)
frame = 0
screen = pygame.display.set_mode((wide, tall))
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    #Key presses   
    pressed = pygame.key.get_pressed()
        # 1,2,3,4 w,a,s,d
    if pressed[pygame.K_UP] and dir != 3:
        dir = 1
    elif pressed[pygame.K_DOWN] and dir != 1:
        dir = 3
    elif pressed[pygame.K_LEFT] and dir != 4:
        dir = 2
    elif pressed[pygame.K_RIGHT] and dir != 2:
        dir = 4

    # Makes sure snakes doesnt move every frame
    if frame % f == 0:
        #print(frame)
        if dir == 1:
            y -= size
        elif dir == 2:
            x -= size
        elif dir == 3:
            y += size
        elif dir == 4:
            x += size
        pastX.insert(0, x)
        pastY.insert(0, y)
        # Apple collision check
        if x == apX and y == apY :
            fruit = True
        if fruit is False:
            pastX.pop()
            pastY.pop()
        else:
            apX = random.randrange(0, wide/size, 1) * size
            apY = random.randrange(0, tall/size, 1) * size
        fruit = False
    #Draw snake and body collision check
    screen.fill((0, 0, 0))
    if len(pastX) >= 1:
        for i in range(len(pastX)):
            pygame.draw.rect(screen, color, pygame.Rect(pastX[i], pastY[i], size, size))
            if pastX[i] == pastX[0] and pastY[i] == pastY[0] and i != 0:
                done =True
    # wall collide check
    if x >= 1280 or y >= 720:
        done = True
    if x < 0 or y < 0:
        done = True
    # Draw apple and head
    pygame.draw.rect(screen, aColor, pygame.Rect(apX , apY , size, size))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))
    pygame.display.flip()
    clock.tick(fps)
    frame += 1
    if frame == 61:
        frame = 1
    if len(pastX) == wide/size * tall/size:
        done = True