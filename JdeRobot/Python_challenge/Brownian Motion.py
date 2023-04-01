import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window dimensions
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball in a Box")

# Set up the ball dimensions
BALL_RADIUS = 20
ball_color = (255, 255, 255)

# Set up the box dimensions
box_width = WIDTH
box_height = HEIGHT
box_color = (255, 255, 255)
box_thickness = 5

# Set up the box position
box_x = 0
box_y = 0

# Set up the ball's initial position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.randint(-5, 5)
ball_dy = random.randint(-5, 5)

# Set up the game loop
clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the ball's position and velocity
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x < BALL_RADIUS or ball_x > WIDTH - BALL_RADIUS:
        ball_dx *= -1
    if ball_y < BALL_RADIUS or ball_y > HEIGHT - BALL_RADIUS:
        ball_dy *= -1

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the box
    pygame.draw.rect(window, box_color, (box_x, box_y,
                     box_width, box_height), box_thickness)

    # Draw the ball
    pygame.draw.circle(window, ball_color, (ball_x, ball_y), BALL_RADIUS)

    # Update the display
    pygame.display.update()
    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
