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
x_cat = 0
x_mouse = 0
y_cat = 0
y_mouse = 0
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

# Load Mouse
m = pygame.image.load("mouse.png")
mouse = pygame.transform.scale(m, (50, 50))

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

# Load Move Sound and Win Sound
pygame.mixer.init(44100, -16, 2, 2048)
move_sound = pygame.mixer.Sound("laser.wav")
win_sound = pygame.mixer.Sound("win_sound.mp3")

# load Start image
s = pygame.image.load("startgame.png")
start = pygame.transform.scale(s, (height, width))


# Animals'position
def animal_position():
    global x_cat, x_mouse, y_cat, y_mouse
    list_x_cat = [100, 200, 300, 400, 500]
    list_y_cat = [100, 200, 300, 400, 500]
    while True:
        x_cat = random.choice(list_x_cat)
        y_cat = random.choice(list_y_cat)
        if x_cat != 500 and y_cat != 300:
            break
    list_x_mouse = [100, 200, 300, 400, 500]
    list_x_mouse.remove(x_cat)
    list_y_mouse = [100, 200, 300, 400, 500]
    list_y_mouse.remove(y_cat)
    x_mouse = random.choice(list_x_mouse)
    y_mouse = random.choice(list_y_mouse)


# Exit
def Exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def draw_board():
    y = 100
    for repeat in range(5):
        for x in range(100, 600, 100):
            pygame.draw.rect(window, white, [x, y, 99, 99])
            pygame.display.update()
        y += 100
    pygame.draw.rect(window, green, [600, 300, 99, 99])
    pygame.display.update()


# Draw Cat rect
def draw_cat():
    pygame.draw.rect(window, red, [x_cat, y_cat, 99, 99])
    window.blit(cat, (x_cat + 25, y_cat + 25))
    pygame.display.update()


# Draw Mouse
def draw_mouse():
    pygame.draw.rect(window, grey, [x_mouse, y_mouse, 99, 99])
    window.blit(mouse, (x_mouse + 25, y_mouse + 25))
    pygame.display.update()


# 2 types of mouse movement

def manual_move():
    global x_mouse, y_mouse, step
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        y_mouse -= 100
    if key[pygame.K_DOWN]:
        y_mouse += 100
    if key[pygame.K_RIGHT]:
        x_mouse += 100
    if key[pygame.K_LEFT]:
        x_mouse -= 100
    move_sound.play()

def random_move():
    x_pos, y_pos = random.choice(move)
    global x_mouse, y_mouse, step
    x_mouse += x_pos
    y_mouse += y_pos
    move_sound.play()
    step += 1
    time.sleep(.5)


# start game using 2 ways
def start_random():
    global step
    while True:
        while True:
            window.fill(blue)
            draw_board()
            draw_cat()
            draw_mouse()
            random_move()
            time.sleep(1)
            Exit()
            # Conditions
            # If Mouse out borders
            if (x_mouse > 550 and y_mouse != 300) or (x_mouse < 100) or (y_mouse > 550) or (y_mouse < 100):
                draw_mouse()
                random_move()
                pygame.display.update()
                time.sleep(1)
                break

            if step == 20:
                draw_mouse()
                random_move()
                pygame.display.update()
                time.sleep(1)
                break

            # If  Mouse Set on Cat
            if x_mouse == x_cat and y_mouse == y_cat:
                draw_mouse()
                random_move()
                pygame.display.update()
                time.sleep(1)
                break

            # If Set on Block win
            if x_mouse == 600 and y_mouse == 300:
                pygame.display.update()
                time.sleep(2)
                break

        # If Lost
        while not (x_mouse == 600 and y_mouse == 300):
            if not (pygame.key.get_pressed()[pygame.K_SPACE]):
                pygame.mixer.music.stop()
                window.blit(background, (0, 0))
                pygame.display.update()
            else:
                animal_position()
                window.fill(blue)
                draw_board()
                draw_cat()
                draw_mouse()
                random_move()
                pygame.mixer.music.play(-1)
                step = 0
                break

            # Exit
            Exit()

        # If Win
        while x_mouse == 600 and y_mouse == 300:
            if not (pygame.key.get_pressed()[pygame.K_SPACE]):
                pygame.mixer.music.stop()
                win_sound.play()
                window.blit(win, (0, 0))
                pygame.display.update()
            else:
                animal_position()
                window.fill(blue)
                draw_board()
                draw_cat()
                draw_mouse()
                random_move()
                pygame.mixer.music.play(-1)
                step = 0
                break
            Exit()


def start_manually():
    global step
    while True:
        while True:
            window.fill(blue)
            draw_board()
            draw_cat()
            manual_move()
            draw_mouse()
            time.sleep(.6)
            Exit()
            # Conditions
            # If Mouse out borders
            if (x_mouse > 550 and y_mouse != 300) or (x_mouse < 100) or (y_mouse > 550) or (y_mouse < 100):
                draw_mouse()
                manual_move()
                pygame.display.update()
                time.sleep(.5)
                break
            if step == 20:
                draw_mouse()
                manual_move()
                pygame.display.update()
                time.sleep(.5)
                break
            # If  Mouse Set on Cat
            if x_mouse == x_cat and y_mouse == y_cat:
                draw_mouse()
                manual_move()
                pygame.display.update()
                time.sleep(.5)
                break

            # If Set on Block win
            if x_mouse == 600 and y_mouse == 300:
                pygame.display.update()
                time.sleep(1.5)
                break

        # If Lost
        while not (x_mouse == 600 and y_mouse == 300):
            if not (pygame.key.get_pressed()[pygame.K_SPACE]):
                pygame.mixer.music.stop()
                window.blit(background, (0, 0))
                pygame.display.update()
            else:
                animal_position()
                window.fill(blue)
                draw_board()
                draw_cat()
                draw_mouse()
                manual_move()
                pygame.mixer.music.play(-1)
                step = 0
                break

            # Exit
            Exit()

        # If Win
        while x_mouse == 600 and y_mouse == 300:
            if not (pygame.key.get_pressed()[pygame.K_SPACE]):
                pygame.mixer.music.stop()
                win_sound.play()
                window.blit(win, (0, 0))
                pygame.display.update()
            else:
                animal_position()
                window.fill(blue)
                draw_board()
                draw_cat()
                draw_mouse()
                random_move()
                pygame.mixer.music.play(-1)
                step = 0
                break
            Exit()


# main function
def main():
    animal_position()
    flag = True
    while True:
        Exit()
        window.blit(start, (0, 0))
        pygame.display.update()
        if pygame.key.get_pressed()[pygame.K_r]:
            break
        elif pygame.key.get_pressed()[pygame.K_m]:
            flag = False
            break

    if flag:
        start_random()
    else:
        start_manually()

if __name__ == "__main__":
    main()
