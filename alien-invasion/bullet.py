import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe que gerencia os projéteis."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria um retângulo para a bala
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

    def update(self):
        """Move a bala para cima."""
        self.rect.y -= self.settings.bullet_speed

    def draw_bullet(self):
        """Desenha a bala na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)