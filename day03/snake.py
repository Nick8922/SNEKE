import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH / 2
head_y = WINDOW_HEIGHT /2 + 100

snake_dx = 0

score = 0
# Set colors
GREEN = (0, 255, 0)  # (r, g, b)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED) #make a text object
title_rect = title_text.get_rect() # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) # places the box containing the text object's center to the middle of the screen.

score_Text = font.render("Score: " + str(score), True, GREEN, DARKRED)
score_rect = score_Text.get_rect()
score_rect.topleft = (WINDOW_WIDTH//10, WINDOW_HEIGHT//10)

Game_over_text = font.render("Game Over!", True, RED, DARKRED)
Game_over_rect = Game_over_text.get_rect()
Game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("press any key to play again", True, RED, DARKRED)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 +64)
# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

Head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
Head_rect = pygame.draw.rect(display_surface, GREEN, Head_coord)

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentilalyl move all of the snakes body by one position in the list

    # Update the x,y position of the snakes head and make a new coordinate

    # Check for game over

    # Check for collisions

    # Update HUD
   Score_text = font.render(f"Score: " + str(score), True, GREEN, DARKRED)
    # Fill the surface
    display_surface.fill(WHITE)
    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_Text, score_rect)
    # Blit assets
    pygame.draw.rect(display_surface, GREEN, Head_coord)
    pygame.draw.rect(display_surface, RED, apple_rect)
    # Update display and tick clock
  pygame.display.update()
    clock.tick(FPS)
# End the game
pygame.quit()
