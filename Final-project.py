import pygame
import random
import time
pygame.display.init()

# Variables
window = pygame.display.set_mode((700, 700))
blue = (30, 62, 75)
white = (255, 255, 255)
green = (0, 255, 0)
window.fill(blue)
pygame.draw.rect(window, blue, (0, 0, 100, 100))
pygame.display.set_caption("Welcome to our first game")
m = pygame.image.load("mouse.png")
mouse = pygame.transform.scale(m, (50, 50))

# mouse position
list_x_mouse = [100, 200, 300, 400, 500]
list_y_mouse = [100, 200, 300, 400, 500]
x_mouse = random.choice(list_x_mouse)
y_mouse = random.choice(list_y_mouse)
while True:
    if x_mouse != x_cat and y_mouse != y_cat:
        break
    else:
        x_mouse = random.choice(list_x_mouse)
        y_mouse = random.choice(list_y_mouse)

# Start Game
while True:
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    y = 100
    for repeat in range(5):
        for x in range(100,600,100):
                pygame.draw.rect(window, white, [x, y, 99, 99])
                pygame.display.update()
        y += 100
        if x > 600:
            break
    pygame.draw.rect(window, green, [600, 300, 99, 99])
    window.blit(mouse, (x_mouse+25, y_mouse+25))
    pygame.display.update()


