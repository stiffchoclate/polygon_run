import pygame
import  time

def scroll_bg():
    pygame.init()
    screen = pygame.display.set_mode(size = (500,500))
    with open("assets/ai_space_inspiration.webp", "r") as f:
        BACKGROUND = pygame.image.load(f)
    clock = pygame.time.Clock()
    running = True
    playerpos = [screen.get_width() / 2, screen.get_height() / 2]
    bg_pos = [0,0]

    #GAME LOOP
    while running:
        screen.fill("black")
        screen.blit(BACKGROUND, bg_pos)
        pygame.draw.rect(surface = screen, rect = (playerpos, (100, 100)),color="red",)
        pygame.draw.circle(surface = screen, color = "blue", center = playerpos, radius = 100)
        pygame.display.flip()
        #running = False
        

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] | keys[pygame.K_UP]:
                    #print("move upwards")
                    playerpos[1]=playerpos[1]-5

                if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
                    #print("move right")
                    bg_pos[0]=bg_pos[0]-5

                if keys[pygame.K_a] | keys[pygame.K_LEFT]:
                    #print("move left")
                    bg_pos[0]=bg_pos[0]+5

                if keys[pygame.K_s] | keys[pygame.K_DOWN]:
                    #print("move down")
                    playerpos[1]=playerpos[1]+5
                print(bg_pos)
            #pygame.display.flip() 




        clock.tick(60)

    #QUIT GAME        
    screen.fill("purple")
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()


scroll_bg()
