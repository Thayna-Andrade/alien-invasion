import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carrega a imagem do alien
        try:
            self.image = pygame.image.load('images/alien.png').convert_alpha()
            print("✅ Imagem alien.png carregada")
        except:
            print("❌ ERRO: Não foi possível carregar images/alien.png")
            # Cria uma imagem de fallback
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.rect(self.image, (255, 0, 0), (0, 0, 40, 40))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        """Move o alien para a direita ou esquerda."""
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction

    def check_edges(self):
        """Retorna True se o alien estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0