import pygame
from pygame.locals import *


clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))


#background_image = pygame.image.load("rimbo.png")

user_input = ''

def game_engine():
    pygame.init()
    pygame.font.init()

    base_font = pygame.font.Font(None,32)

    screen.fill('Black')
    pygame.display.set_caption("Escape from Rimbo")
    
    user_input = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
        #screen.blit(background_image, (0, 0))
        
        text_surface = base_font.render(user_input,True,(255, 255, 255))
        screen.blit(text_surface, (0, 0))
        
        #Display properties
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

game_engine()
