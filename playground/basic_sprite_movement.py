import pygame
import time
import shapes

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

def blitting_manual():
    pygame.init()
    screen = pygame.display.set_mode(size = (500,500))
    clock = pygame.time.Clock()
    running = True
    playerpos = [screen.get_width() / 2, screen.get_height() / 2]

    #GAME LOOP
    while running:
        screen.fill("black")
        pygame.draw.rect(surface = screen, rect = (playerpos, (100, 100)),color="red",)
        pygame.draw.circle(surface = screen, color = "blue", center = playerpos, radius = 100)
        pygame.display.flip()
        #running = False
        

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_w] | keys[pygame.K_UP]:
                    print("move upwards")
                    playerpos[1]=playerpos[1]-5

                if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
                    print("move right")
                    playerpos[0]=playerpos[0]+5

                if keys[pygame.K_a] | keys[pygame.K_LEFT]:
                    print("move left")
                    playerpos[0]=playerpos[0]-5

                if keys[pygame.K_s] | keys[pygame.K_DOWN]:
                    print("move down")
                    playerpos[1]=playerpos[1]+5
            #pygame.display.flip()
        clock.tick(60)

    #QUIT GAME        
    screen.fill("purple")
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()

def pygame_blitting():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size = (500,500))
    playerpos = [screen.get_width() / 2, screen.get_height() / 2]
    rect = pygame.draw.rect(surface = screen, rect = (playerpos, (100, 100)),color="red",)
    circ = pygame.draw.circle(surface = screen, color = "blue", center = playerpos, radius = 100)
    running = True

    while running:
        screen.blit(circ, playerpos)
        screen.blit(rect, playerpos)

        pygame.display.flip()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_w] | keys[pygame.K_UP]:
                    print("move upwards")
                    playerpos[1]=playerpos[1]-5

                if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
                    print("move right")
                    playerpos[0]=playerpos[0]+5

                if keys[pygame.K_a] | keys[pygame.K_LEFT]:
                    print("move left")
                    playerpos[0]=playerpos[0]-5

                if keys[pygame.K_s] | keys[pygame.K_DOWN]:
                    print("move down")
                    playerpos[1]=playerpos[1]+5
            #pygame.display.flip()
        
        clock.tick(60)


    pygame.quit()

#blitting_manual()
pygame_blitting()