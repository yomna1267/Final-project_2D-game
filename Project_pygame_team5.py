import pygame
import random
import time
pygame.display.init()

# Variables
window = pygame.display.set_mode((700, 700))
   #Colours
blue = (30, 62, 75)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (211, 211, 211)
window.fill(blue)
pygame.draw.rect(window, blue, (0, 0, 100, 100))
pygame.display.update()
pygame.display.set_caption("Welcome to our first game")

#Load Mouse
m = pygame.image.load("mouse.png")
mouse = pygame.transform.scale(m, (50, 50))

# Position Mouse
list_x_mouse = [100, 200, 300, 400, 500]
list_y_mouse = [100, 200, 300, 400, 500]
x_mouse = random.choice(list_x_mouse)
y_mouse = random.choice(list_y_mouse)

#Load Cat
cat_img = pygame.image.load("cat.png")
cat = pygame.transform.scale(cat_img, (50,50))

#Position Cat
list_x_cat = [100, 200, 300, 400, 500]
list_y_cat = [100, 200, 300, 400, 500]
x_cat = random.choice(list_x_cat)
y_cat = random.choice(list_y_cat)


# Start Game
while True:
    #Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Draw rect
    y = 100
    for repeat in range(5):
        for x in range(100, 600, 100):
            pygame.draw.rect(window, white, [x, y, 99, 99])
            pygame.display.update()
        y += 100
    pygame.draw.rect(window, green, [600, 300, 99, 99])
    pygame.display.update()
    # Draw Cat rect
    pygame.draw.rect(window, red, [x_cat, y_cat, 99, 99])
    window.blit(cat, (x_cat + 25,y_cat + 25))
    #Draw Mouse
    pygame.draw.rect(window, grey, [x_mouse, y_mouse, 99, 99])
    window.blit(mouse, (x_mouse+25, y_mouse+25))
    pygame.display.update()
    time.sleep(1)









