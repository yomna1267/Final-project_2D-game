import pygame
pygame.display.init()

# Variables
window = pygame.display.set_mode((700,700))
blue = (30, 62, 75)
white = (255,255,255)
green = (0, 255, 0)
window.fill(blue)
pygame.draw.rect(window, blue, (0, 0, 100, 100))
pygame.display.update()

# Start Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    y = 100
    for repeat in range(5):
        for x in range(100,600,100):
                pygame.draw.rect(window,white,[x,y,99,99])
                pygame.display.update()
        y += 100
        if x > 600:
            break
    pygame.draw.rect(window, green, [600, 300, 99, 99])
    pygame.display.update()


