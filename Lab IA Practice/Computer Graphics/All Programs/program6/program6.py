import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Moving Circle & Rectangle Animation')

# Define colors
blue = (30, 144, 255)
white = (255, 255, 255)

# Initial position of the circle
x, y = width // 2, height // 2
radius = 20
dx, dy = 5, 5  # Movement step

rect_x, rect_y = 50, 50  # Top-left corner position
rect_width, rect_height = 100, 50  # Width and height of the rectangle
rect_dx, rect_dy = 7, 3  # Movement steps for rectangle

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the circle
    x += dx
    y += dy

    # Bounce the circle off the edges
    if x - radius < 0 or x + radius > width:
        dx = -dx
    if y - radius < 0 or y + radius > height:
        dy = -dy
# Rectangle movement and bounce
    rect_x += rect_dx
    rect_y += rect_dy

    if rect_x < 0 or rect_x + rect_width > width:
        rect_dx = -rect_dx
    if rect_y < 0 or rect_y + rect_height > height:
        rect_dy = -rect_dy


    # Fill the screen with black
    window.fill(white)

    # Draw the circle 
    pygame.draw.circle(window, blue, (x, y), radius)
    pygame.draw.rect(window, blue, (rect_x, rect_y,rect_width,rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
