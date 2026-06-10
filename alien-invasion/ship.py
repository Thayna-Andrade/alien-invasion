import pygame

class Ship:
    """Classe que gerencia a nave."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Carrega a imagem da nave
        try:
            self.image = pygame.image.load('images/ship.png').convert_alpha()
            print("✅ Imagem ship.png carregada")
        except:
            print("❌ ERRO: Não foi possível carregar images/ship.png")
            # Cria uma imagem de fallback
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.polygon(self.image, (0, 255, 0), [(25, 0), (0, 50), (50, 50)])
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Usa apenas rect.x, sem variável float separada
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da nave baseada nos flags de movimento."""
        # Move para direita
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        
        # Move para esquerda  
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Desenha a nave na posição atual."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a nave na parte inferior da tela."""
        self.rect.midbottom = self.screen_rect.midbottom