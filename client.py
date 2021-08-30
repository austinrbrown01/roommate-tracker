# This is a client which will control the GUI and high-level operation of the applicatoin
import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    #screen = pygame.display.set_mode((480, 320))
    screen = pygame.display.set_mode((480, 320), pygame.FULLSCREEN)
    pygame.display.set_caption('Roommate Tracker')
    #screen = pygame.display.toggle_fullscreen()

    # Fill background
    background = pygame.Surface(screen.get_size())
    #background = pygame.Surface((480, 320))
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Set running to False to end the while loop.
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()