import pygame,random
row = 20
col = 16
squaresize = 32

def draw_grid(screen):
    for i in range(col):
        pygame.draw.line(
            screen,
            "black",
            (i*squaresize,0),
            (i*squaresize,512),
            1
        )
    for i in range(row):
        pygame.draw.line(
            screen,
            "black",
            (0,i*squaresize),
            (640,i*squaresize),
            1

        )



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = event.pos

            screen.fill("light green")
            draw_grid(screen)
            x=0
            y=0
            #x = random.randrange(col)*squaresize
            #y = random.randrange(row)*squaresize
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()