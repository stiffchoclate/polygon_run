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
    playerpos = [screen.get_width() / 2, screen.get_height() / 2]

    while running:
        screen.fill("black")
        pygame.draw.rect(
            surface = screen, rect = (playerpos, (100, 100)),color="red",
        )
        pygame.draw.circle(
            surface = screen, color = "blue", center = playerpos, radius = 100
        )
        pygame.display.flip()
        #running = False
        

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            while event.type == pygame.KEYDOWN:
                if keys[pygame.K_w] | keys[pygame.K_UP]:
                    print("move upwards")
                    playerpos[1]=playerpos[1]+5
                if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
                    print("move right")
                    playerpos[0]=playerpos[0]+5
                if keys[pygame.K_a] | keys[pygame.K_LEFT]:
                    print("move left")
                    playerpos[0]=playerpos[0]-5
                if keys[pygame.K_s] | keys[pygame.K_DOWN]:
                    print("move down")
                    playerpos[1]=playerpos[1]-5
            #pygame.display.flip()
        clock.tick(60)
            
    screen.fill("purple")
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()

blitting_2d()