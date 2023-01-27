import pygame
import time
from pygame.locals import *

def screen_engine():
    pygame.init()
    pygame.font.init()

    pygame.mixer.music.fadeout(3)
    pygame.mixer.music.load("./SoundEngine5000/reklam.wav")
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1024, 512))

    screen.fill('Black')
    pygame.display.set_caption("Escape from Rimbo")
    background_image = pygame.image.load("img/rimbo2.jpg").convert()
    background_image = pygame.transform.scale(background_image, (1024, 512))
    pygame.display.set_icon(background_image)
    screen.blit(background_image, (0, 0))

    pygame.display.update()

    time.sleep(5)
    pygame.display.quit()
        

