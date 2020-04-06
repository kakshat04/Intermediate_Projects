import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

# Set up drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Window to draw the game is created using set mode

# run until user asks to quit
game_run = True

while game_run:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            game_run = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 250, 250), (280, 280), 50)

        # Create your own surface
        surface = pygame.Surface([50, 50])

        # Give surface the color
        surface.fill((0, 255, 250))
        rect = surface.get_rect()

        # # Put the center of surf at the center of the display
        # surf_center = (
        #     (WIDTH - surface.get_width()) / 2,
        #     (HEIGHT - surface.get_height()) / 2
        # )
        #
        # screen.blit(surface, surf_center)
        screen.blit(surface, (WIDTH / 2, HEIGHT / 2))

        # Flip the display
        pygame.display.flip()

pygame.quit()
