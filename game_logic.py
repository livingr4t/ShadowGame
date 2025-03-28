import pygame

# Ustawienia gry
WIDTH, HEIGHT = 800, 600
FPS = 60

# Kolory
WHITE = (255, 255, 255)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)

# Inicjalizacja Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bajkowa Przygoda")
clock = pygame.time.Clock()

# Gracz
player = pygame.Rect(50, 50, 50, 50)
player_speed = 5

# Przeciwnicy
enemies = [pygame.Rect(400, 300, 50, 50)]

def main_game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Ruch gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        if keys[pygame.K_UP]:
            player.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.y += player_speed

        # Rysowanie
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for enemy in enemies:
            pygame.draw.rect(screen, GREEN, enemy)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

# Uruchomienie gry
if __name__ == "__main__":
    main_game_loop()
