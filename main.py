import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Load the images
player_img = pygame.image.load("player.png")
coin_img = pygame.image.load("coin.png")
obstacle_img = pygame.image.load("obstacle.png")

# Load the sound effects
coin_sound = pygame.mixer.Sound("coin_sound.wav")
hit_sound = pygame.mixer.Sound("hit_sound.wav")

# Create the game objects
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.centery = HEIGHT // 2

coin_rect = coin_img.get_rect()
coin_rect.centerx = random.randint(50, WIDTH - 50)
coin_rect.centery = random.randint(50, HEIGHT - 50)

obstacle_rect = obstacle_img.get_rect()
obstacle_rect.centerx = random.randint(50, WIDTH - 50)
obstacle_rect.centery = -50
obstacle_speed = 2

# Set up the game loop
running = True
coins_collected = 0
pygame.mixer.init()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Move the coin
    coin_rect.y += 2
    if coin_rect.top > HEIGHT:
        coin_rect.centerx = random.randint(50, WIDTH - 50)
        coin_rect.centery = random.randint(50, HEIGHT - 50)

    # Move the obstacle
    obstacle_rect.y += obstacle_speed
    if obstacle_rect.top > HEIGHT:
        obstacle_rect.centerx = random.randint(50, WIDTH - 50)
        obstacle_rect.centery = -50

    # Check for collisions
    if player_rect.colliderect(coin_rect):
        coin_rect.centerx = random.randint(50, WIDTH - 50)
        coin_rect.centery = random.randint(50, HEIGHT - 50)
        coins_collected += 1
        coin_sound.play()

    if player_rect.colliderect(obstacle_rect):
        font = pygame.font.Font(None, 36)
        hit_sound.play()
        text1 = font.render("You Lost!", True, (255, 0, 0))
        text2 = font.render("Coins collected: " + str(coins_collected), True, (255, 255, 255))
        text1_rect = text1.get_rect()
        text2_rect = text2.get_rect()
        text1_rect.centerx = screen.get_rect().centerx
        text2_rect.centerx = screen.get_rect().centerx
        text1_rect.centery = screen.get_rect().centery - 20
        text2_rect.centery = screen.get_rect().centery + 20
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    # Draw the game objects
    screen.fill((0, 0, 0))
    screen.blit(player_img, player_rect)
    screen.blit(coin_img, coin_rect)
    screen.blit(obstacle_img, obstacle_rect)
    pygame.display.flip()

    # Set the game FPS
    clock = pygame.time.Clock()
    clock.tick(60)

# Quit Pygame
pygame.quit()
