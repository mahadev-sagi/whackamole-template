import pygame,random

def draw_grid(screen):
    row = 20
    col = 16
    squaresize = 32
    for i in range(col+1):
        pygame.draw.line(
            screen,
            "black",
            (i*squaresize,0),
            (i*squaresize,512),
            2
        )
    for i in range(row+1):
        pygame.draw.line(
            screen,
            "black",
            (0,i*squaresize),
            (640,i*squaresize),
            2

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
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()