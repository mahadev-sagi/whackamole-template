import pygame,random
row = 20
col = 16
squaresize = 32
length = 640
width = 512

def draw_grid(screen):
    for i in range(row):
        pygame.draw.line(
            screen,
            "black",
            (i*squaresize,0),
            (i*squaresize,width),
            1
        )
    for i in range(col):
        pygame.draw.line(
            screen,
            "black",
            (0,i*squaresize),
            (length,i*squaresize),
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
        mole_x = 0
        mole_y = 0


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]//32
                    y = event.pos[1]//32
                    if (x,y) == (mole_x//32, mole_y//32):
                        mole_x = random.randrange(0,640,32)
                        mole_y = random.randrange(0,512,32)




            screen.fill("light green")
            draw_grid(screen)
            pygame.draw.line(screen, "black", (640,0), (640,512), 1)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))
            pygame.display.flip()
            clock.tick(300)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()