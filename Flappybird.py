import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Bird")

# Set up colors
background_color = (135, 206, 250)
bird_color = (255, 255, 0)
pipe_color = (0, 128, 0) 

# Set up the bird
bird_radius = 20
bird_x = 100
bird_y = window_height // 2

# Set up the pipes
pipe_width = 70
pipe_height = random.randint(100, 400)
pipe_gap = 150
pipe_x = window_width
pipe_y = random.randint(pipe_height + pipe_gap, window_height)

# Set up the game clock
clock = pygame.time.Clock()

# Set up game variables
gravity = 0.5
bird_movement = 0
score = 0

# Load game fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -10

    # Update bird position and movement
    bird_movement += gravity
    bird_y += bird_movement

    # Update pipe position
    pipe_x -= 3
    if pipe_x < -pipe_width:
        pipe_x = window_width
        pipe_height = random.randint(100, 400)
        pipe_y = random.randint(pipe_height + pipe_gap, window_height)
        score += 1

    # Check for collision
    if bird_y < 0 or bird_y > window_height - bird_radius or (
            bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width and (
            bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap)):
        running = False

    # Draw game elements
    window.fill(background_color)
    pygame.draw.circle(window, bird_color, (bird_x, int(bird_y)), bird_radius)
    pygame.draw.rect(window, pipe_color, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(window, pipe_color, (pipe_x, pipe_height + pipe_gap, pipe_width, window_height))

    # Display score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
