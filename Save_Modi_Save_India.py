# Import Pygame module
import pygame
import os

# Import random for random numbers
import random

# Import different keys to use in the game
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

WIDTH = 1000
HEIGHT = 600


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.surf = pygame.Surface((75, 25))
        self.surf = pygame.image.load("Modi.png").convert()
        self.surf = pygame.transform.scale(self.surf, (75, 25))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(WIDTH + 20, WIDTH + 100), random.randint(0, HEIGHT)))
        # self.rect = self.surf.get_rect(center=(600, 400))#center=(random.randint(600, 800), random.randint(0, 600)))
        # self.speed = random.randint(5, 20)
        self.speed = 4

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Initialize pygame object
pygame.init()

# Set up game surface
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Setup screen Background
background = pygame.image.load("Parliament.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. Right now, this is just a rectangle
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Give Title to game
pygame.display.set_caption("SAVE MODI")
game_run = True

inputMap = [False, False]

while game_run:
    for event in pygame.event.get():
        # print(event.type)
        # print(KEYDOWN)
        if event.type == KEYDOWN:  # Did user press any key
            # print("HEREEEEEE")
            if event.type == K_ESCAPE:  # If escape is pressed, exit loop
                # print("YESSS")
                game_run = False
            if event.key == K_UP:
                inputMap[0] = True;
            if event.key == pygame.K_DOWN:
                inputMap[1] = True;
        elif event.type == pygame.QUIT:  # If window is closed, exit loop
            game_run = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            path = "E:\Python_Projects\Intermediate_Projects\Modi_Oppositions"
            opp_lst = os.listdir(path)
            opposition = random.choice(opp_lst)
            # print("*********", opposition)
            new_enemy = Enemy(path + "\\" + opposition)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Fill in the screen with White
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # recalculate speed based on current input state
    my_speed = 0
    if inputMap[0]:
        my_speed += 10
    if inputMap[1]:
        my_speed += 10

    # Update the player sprite based on user keypresses
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check for collision
    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        print("Oooo.....Modiji collided and lost.. :(")
        game_run = False

    # Update the display
    pygame.display.flip()

