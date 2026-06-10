# create_images.py
import pygame
import os

# Cria a pasta images se não existir
os.makedirs('images', exist_ok=True)

# Configurações
size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.init()

# Cria nave (triângulo verde)
ship_surface = pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.polygon(ship_surface, (0, 255, 0), [(30, 0), (0, 60), (60, 60)])
pygame.image.save(ship_surface, 'images/ship.png')
print("✅ ship.png criada")

# Cria alien (quadrado vermelho com olhos)
alien_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.rect(alien_surface, (255, 0, 0), (5, 5, 40, 40), border_radius=5)
pygame.draw.circle(alien_surface, (255, 255, 255), (15, 20), 6)
pygame.draw.circle(alien_surface, (255, 255, 255), (35, 20), 6)
pygame.draw.circle(alien_surface, (0, 0, 0), (15, 20), 3)
pygame.draw.circle(alien_surface, (0, 0, 0), (35, 20), 3)
pygame.image.save(alien_surface, 'images/alien.png')
print("✅ alien.png criada")

pygame.quit()
print("\n🎮 Execute: python alien_invasion.py")