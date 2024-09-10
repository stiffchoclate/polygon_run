import pygame
import time
from PIL import Image


def main():
    #Bring assets into memory and set initial pygame window.
    with open("assets/ai_space_inspiration.webp", mode = "r") as f:
        BG = pygame.image.load(f)
        SIZE = BG.width, BG.height
    with open ("assets/avatar.jpg", mode = "r") as f:
        SPRITE = pygame.image.load(f)
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(SIZE)
    running = True
    pygame.init()
    SCREEN.blit(BG, (0,0))
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_w] | keys[pygame.K_UP]:
                    print("move upwards")

                if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
                    print("do something")

                if keys[pygame.K_a] | keys[pygame.K_LEFT]:
                    print("do something")

                if keys[pygame.K_s] | keys[pygame.K_DOWN]:
                    print("move downwards")

        pygame.display.flip()
        CLOCK.tick(60)
    time.sleep(1)
    #Log out screen
    pygame.quit()

main()