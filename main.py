import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load Image Safely
try:
    icecream_boss_surface = pygame.image.load(r'C:\Users\owenc\Downloads\pixil-frame-0.png').convert_alpha()
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    exit()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen
    screen.fill("purple")

    # Render the image
    screen.blit(icecream_boss_surface, (100, 100))  # Adjust position as needed

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)

pygame.quit()
