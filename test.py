import pygame
import random
import time
from pygame.locals import *



pygame.init()
pygame.display.set_caption("Pac-Man")

'''

pygame.init()

pygame./'''


# Set screen dimensions00K505
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)

# Load fonts
my_font = pygame.font.SysFont("Times New Roman", 40)
time_font = pygame.font.SysFont("Times New Roman", 70)

# Initialize clock
clock = pygame.time.Clock()

# List of images for fruits and ghosts
fruits_images = ["fruit1.png", "fruit2.png", "fruit3.png"]
ghost_images = ["ghost1.png", "ghost2.png", "ghost3.png"]

# Background management function
def change_bg(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(bg, (0, 0))

# Pac-Man sprite
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pacman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

# Fruit sprite
class Fruits(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width)
        self.rect.y = random.randrange(screen_height)

# Ghost sprite
class Ghost(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width)
        self.rect.y = random.randrange(screen_height)

# Initialize sprite groups
fruit_list = pygame.sprite.Group()
ghost_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Function to create fruits
def create_fruits():
    for _ in range(50):
        fruit = Fruits(random.choice(fruits_images))
        fruit_list.add(fruit)
        all_sprites.add(fruit)

# Function to create ghosts
def create_ghosts():
    for _ in range(30):
        ghost = Ghost(random.choice(ghost_images))
        ghost_list.add(ghost)
        all_sprites.add(ghost)

# Game initialization
def initialize_game():
    create_fruits()
    create_ghosts()
    pacman = Pacman()
    all_sprites.add(pacman)
    return pacman

# Function to handle user inputs
def handle_input(pacman):
    keys = pygame.key.get_pressed()
    if keys[K_UP] and pacman.rect.y > 0:
        pacman.rect.y -= 5
    if keys[K_DOWN] and pacman.rect.y < screen_height - 70:
        pacman.rect.y += 5
    if keys[K_LEFT] and pacman.rect.x > 0:
        pacman.rect.x -= 5
    if keys[K_RIGHT] and pacman.rect.x < screen_width - 50:
        pacman.rect.x += 5

# Function to check collisions and update score
def check_collisions(pacman, score):
    fruit_hit_list = pygame.sprite.spritecollide(pacman, fruit_list, True)
    ghost_hit_list = pygame.sprite.spritecollide(pacman, ghost_list, True)

    for _ in fruit_hit_list:
        score += 1
    for _ in ghost_hit_list:
        score -= 5

    return score

# Function to render the game screen
def render_game(pacman, score, timeElapsed):
    change_bg("gamescreen.jpg")
    countDown = time_font.render(str(60 - int(timeElapsed)), True, red)
    screen.blit(countDown, (800, 10))

    text = my_font.render("Score = " + str(score), True, white)
    screen.blit(text, (730, 80))

    all_sprites.draw(screen)
    pygame.display.update()

# Function to render the end screen
def render_end_screen(score):
    if score > 20:
        text = my_font.render("YOU WIN", True, red)
        change_bg("winscreen.jfif")
    else:
        text = my_font.render("BETTER LUCK NEXT TIME", True, red)
        change_bg("losescreen.jpg")
    screen.blit(text, (250, 40))
    pygame.display.update()

# Main game loop
def main_game():
    pacman = initialize_game()
    score = 0
    start_time = time.time()
    playing = True

    while playing:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False

        timeElapsed = time.time() - start_time
        if timeElapsed >= 60:
            render_end_screen(score)
        else:
            handle_input(pacman)
            score = check_collisions(pacman, score)
            render_game(pacman, score, timeElapsed)

    pygame.quit()

# Start the game
if __name__ == "__main__":
    main_game()
