import pygame
import random
import time
pygame.display.init()

# Variables
height = 700
width = 700
window = pygame.display.set_mode((height, width))
move = [[100, 0], [0, 100], [-100, 0], [0, -100]]
step = 0
# Colours
blue = (30, 62, 75)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
window.fill(blue)
pygame.draw.rect(window, blue, (0, 0, 100, 100))
pygame.display.update()
pygame.display.set_caption("Welcome to our first game")


# Load Cat
cat_img = pygame.image.load("cat.png")
cat = pygame.transform.scale(cat_img, (50, 50))

# Position Cat
list_x_cat = [100, 200, 300, 400, 500]
list_y_cat = [100, 200, 300, 400, 500]
while True:
    x_cat = random.choice(list_x_cat)
    y_cat = random.choice(list_y_cat)
    if x_cat != 500 and y_cat != 300:
        break

# Load Mouse
m = pygame.image.load("mouse.png")
mouse = pygame.transform.scale(m, (50, 50))

# Position Mouse
list_x_mouse = [100, 200, 300, 400, 500]
list_x_mouse.remove(x_cat)
list_y_mouse = [100, 200, 300, 400, 500]
list_y_mouse.remove(y_cat)
global x_mouse, y_mouse
x_mouse: int = random.choice(list_x_mouse)
y_mouse: int = random.choice(list_y_mouse)

# Load Background Music
pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
# Load background image
background_image = pygame.image.load("background.png")
background = pygame.transform.scale(background_image, (height, width))

# Load win img
win_image = pygame.image.load("win.jpg")
win = pygame.transform.scale(win_image, (height, width))

#Load Move Sound and Win Sound
pygame.mixer.init(44100, -16, 2, 2048)
move_sound = pygame.mixer.Sound("laser.wav")
win_sound = pygame.mixer.Sound("win_sound.mp3")
# Start Game
while True:
    while True:
        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Draw rect
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
        window.blit(cat, (x_cat + 25, y_cat + 25))

        # Draw Mouse
        pygame.draw.rect(window, grey, [x_mouse, y_mouse, 99, 99])
        window.blit(mouse, (x_mouse+25, y_mouse+25))
        pygame.display.update()

        # Control the mouse movement
        x_pos, y_pos = random.choice(move)
        x_mouse += x_pos
        y_mouse += y_pos
        move_sound.play()
        step += 1
        time.sleep(.5)

    #Conditions
        # If Mouse out borders
        if (x_mouse > 550 and y_mouse != 300) or (x_mouse < 100) or (y_mouse > 550) or (y_mouse < 100):
            pygame.display.update()
            time.sleep(3)
            break

        if step == 20:
            pygame.display.update()
            time.sleep(3)
            break

        # If  Mouse Set on Cat
        if (x_mouse == x_cat and y_mouse == y_cat):
            pygame.display.update()
            time.sleep(3)
            break
        time.sleep(1)

        # If Set on Block win
        if x_mouse == 600 and y_mouse == 300:
            pygame.display.update()
            time.sleep(3)
            break

    # If Lost
    while not(x_mouse == 600 and y_mouse == 300):
        if not(pygame.key.get_pressed()[pygame.K_SPACE]):
            pygame.mixer.music.stop()
            window.blit(background, (0, 0))
            pygame.display.update()
        else:
            x_mouse: int = random.choice(list_x_mouse)
            y_mouse: int = random.choice(list_y_mouse)
            while True:
                x_cat = random.choice(list_x_cat)
                y_cat = random.choice(list_y_cat)
                if x_cat != 500 and y_cat != 300:
                    break
            window.fill(blue)
            pygame.draw.rect(window, grey, [x_mouse, y_mouse, 99, 99])
            window.blit(mouse, (x_mouse + 25, y_mouse + 25))
            pygame.draw.rect(window, red, [x_cat, y_cat, 99, 99])
            window.blit(cat, (x_cat + 25, y_cat + 25))
            pygame.mixer.music.play(-1)
            pygame.display.update()
            step = 0
            break

        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # If Win
    while x_mouse == 600 and y_mouse == 300:
        if not(pygame.key.get_pressed()[pygame.K_SPACE]):
            pygame.mixer.music.stop()
            win_sound.play()
            window.blit(win, (0, 0))
            pygame.display.update()
        else:
            pygame.mixer.music.stop()
            x_mouse: int = random.choice(list_x_mouse)
            y_mouse: int = random.choice(list_y_mouse)
            while True:
                x_cat = random.choice(list_x_cat)
                y_cat = random.choice(list_y_cat)
                if x_cat != 500 and y_cat != 300:
                    break
            window.fill(blue)
            pygame.draw.rect(window, grey, [x_mouse, y_mouse, 99, 99])
            window.blit(mouse, (x_mouse + 25, y_mouse + 25))
            pygame.draw.rect(window, red, [x_cat, y_cat, 99, 99])
            window.blit(cat, (x_cat + 25, y_cat + 25))
            pygame.mixer.music.play(-1)
            pygame.display.update()
            step = 0
            break

        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()