import pygame
import time

#Understanding how blitting actually works
def concept_blitting():
    print("\nWelcome to the first dimension.")
    playerpos = 3
    map = [1, 1, 2, 2, 2, 1]
    print(f'This is the map:\n{map}')
    screen = [i for i in map]

    print("Rendering character...")
    screen[playerpos] = 8
    playerpos = 3
    print(screen)

    """ Moving the character//
    Can't be replicated easily without having a immutable copy of the background
    to replace the pixels in which the character moves from.
    """
    map = [1, 1, 2, 2, 2, 1]
    screen[playerpos-1] = screen[playerpos]
    screen[playerpos] = map[playerpos]
    playerpos = playerpos -1
    print(screen)

def blitting_2d():
    pygame.init()
    screen = pygame.display.set_mode(size = (500,500))
    clock = pygame.time.Clock()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.draw.rect(
            surface = screen,
            color = "orange",
            rect = (0,0, 200, 200) )
        pygame.display.flip()
        clock.tick(60)

    time.sleep(2)
    pygame.quit()

blitting_2d()