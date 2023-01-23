import pygame
from pygame.locals import *


clock = pygame.time.Clock()
screen = pygame.display.set_mode((256, 512))


def game_engine():
    pygame.init()
    pygame.font.init()

    screen.fill('Black')
    pygame.display.set_caption("Escape from Rimbo")
    background_image = pygame.image.load("img/EscRimbo.jpg").convert()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(background_image, (0, 0))
        
    #Display properties
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

game_engine()
