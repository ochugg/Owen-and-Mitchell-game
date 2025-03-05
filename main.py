import pygame 

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fartchell")
clock = pygame.time.Clock()
running = True

# Load player sprite image
try:
    player_image = pygame.image.load(r'C:\Users\owenc\Downloads\New_Piskel-4.png.png').convert_alpha()
except pygame.error as e:
    print(f"Error loading player image: {e}")
    pygame.quit()
    exit()

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(player_image, (80, 80))  # Scale the image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Movement speed

    def update(self, keys):
        """Handles player movement based on key presses."""
        if keys[pygame.K_w]:  # Move up
            self.rect.y -= self.speed
        if keys[pygame.K_s]:  # Move down
            self.rect.y += self.speed
        if keys[pygame.K_a]:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Move right
            self.rect.x += self.speed

        # Keep player within screen bounds
        self.rect.clamp_ip(screen.get_rect())

# Create the player instance
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load Ice Cream Boss Image
try:
    icecream_boss_surface = pygame.image.load(r'C:\Users\owenc\Downloads\pixil-frame-0.png').convert_alpha()
except pygame.error as e:
    print(f"Error loading boss image: {e}")
    pygame.quit()
    exit()

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Update player movement
    all_sprites.update(keys)

    # Fill screen
    screen.fill("purple")

    # Render the boss image
    screen.blit(icecream_boss_surface, (100, 100))  # Adjust position as needed

    # Draw player
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)

pygame.quit()
