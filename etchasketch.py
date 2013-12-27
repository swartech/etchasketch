import pygame, sys
from pygame.locals import *

x = 200
y = 400


def init():
    window.fill(pygame.Color(0, 0, 0))
    pygame.draw.rect(window, (150, 150, 150),(20, 20, 700, 700))
    pygame.draw.circle(window, (0, 0, 0), (x, y), 0)
    window.blit(border, (0, 0))
    window.blit(border_shadow, (0, 0))
    window.blit(button, (6, 480))
    window.blit(button_shading, (6, 480))
    window.blit(button_shadow, (3, 476))
    window.blit(button_top, (16, 490))
    window.blit(button, (682, 480))
    window.blit(button_shading, (682, 480))
    window.blit(button_shadow, (679, 476))
    window.blit(button_top, (692, 490))


def shake():
    window.fill(pygame.Color(0, 0, 0))
    pygame.draw.rect(window, (150, 150, 150),(20, 20+20, 700, 500))
    window.blit(border, (0, 0+20))
    window.blit(border_shadow, (0, 0+20))
    window.blit(button, (6, 480+20))
    window.blit(button_shading, (6, 480+20))
    window.blit(button_shadow, (3, 476+20))
    window.blit(button_top, (16, 490+20))
    window.blit(button, (682, 480+20))
    window.blit(button_shading, (682, 480+20))
    window.blit(button_shadow, (679, 476+20))
    window.blit(button_top, (692, 490+20))
    pygame.display.update()
    window.fill(pygame.Color(0, 0, 0))
    pygame.draw.rect(window, (150, 150, 150),(20, 20-20, 700, 500))
    window.blit(border, (0, 0-20))
    window.blit(border_shadow, (0, 0-20))
    window.blit(button, (6, 480-20))
    window.blit(button_shading, (6, 480-20))
    window.blit(button_shadow, (3, 476-20))
    window.blit(button_top, (16, 490-20))
    window.blit(button, (682, 480-20))
    window.blit(button_shading, (682, 480-20))
    window.blit(button_shadow, (679, 476-20))
    window.blit(button_top, (692, 490-20))
    pygame.display.update()


def rotate(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    image = rot_image
    return rot_image

pygame.init()
fps_clock = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Etch-A-Sketch')

#load images
border = pygame.image.load('border.png')
border_shadow = pygame.image.load('border_shadow.png')
button = pygame.image.load('button.png')
button_top = pygame.image.load('button_top.png')
button_shading = pygame.image.load('button_shading.png')
button_shadow = pygame.image.load('button_shadow.png')

#initialise
dir_x = 0
dir_y = 0
rot_1 = 0
rot_speed1 = 0
rot_speed2 = 0
rot_2 = 0
init()

#rendering loop
while True:
    #window.fill(pygame.Color(0, 0, 0)) #clear the screen
    pygame.draw.circle(window, (0, 0, 0), (x, y), 0)

    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #if space is pressed swap sides
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pygame.image.save(window, "image.jpg")
            elif event.key == K_LEFT:
                dir_y = 1
                rot_speed2 += 2
            elif event.key == K_RIGHT:
                dir_y = -1
                rot_speed2 -= 2
                window.blit(rotate(button, 2), (682, 480))
            elif event.key == K_a:
                dir_x = -1
                rot_speed1 += 2
            elif event.key == K_d:
                dir_x = 1
                rot_speed1 -= 2
            elif event.key == K_RETURN:
                shake()
                init()

        if event.type == KEYUP:
            if event.key == K_LEFT:
                dir_y -= 1
                rot_speed2 -= 2
            elif event.key == K_RIGHT:
                dir_y += 1
                rot_speed2 += 2
                window.blit(rotate(button, 2), (682, 480))
            elif event.key == K_a:
                dir_x += 1
                rot_speed1 -= 2
            elif event.key == K_d:
                dir_x -= 1
                rot_speed1 += 2

    #update
    x += dir_x
    y += dir_y
    rot_1 += rot_speed1
    rot_2 += rot_speed2

    #bounds checking
    if x >= 700:
        x = 699
    if x <= 100:
        x = 101
    if y >= 500:
        y = 499
    if y <= 100:
        y = 101

    #draw rotated buttons
    window.blit(border, (0, 0))
    window.blit(rotate(button, rot_2), (682, 480))
    window.blit(button_shading, (682, 480))
    window.blit(button_shadow, (679, 476))
    window.blit(button_top, (692, 490))

    window.blit(rotate(button, rot_1), (6, 480))
    window.blit(button_shading, (6, 480))
    window.blit(button_shadow, (3, 476))
    window.blit(button_top, (16, 490))

    pygame.display.update()
    fps_clock.tick(30)