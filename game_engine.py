import pygame
import time
from pygame.locals import *

def game_engine():
    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((512, 600))

    screen.fill('Black')
    pygame.display.set_caption("Escape from Rimbo")
    background_image = pygame.image.load("img/EscRimbo.jpg").convert()
    background_image = pygame.transform.scale(background_image, (512, 600))
    pygame.display.set_icon(background_image)
    screen.blit(background_image, (0, 0))

    pygame.display.update()

    time.sleep(5)
    pygame.display.quit()
        

