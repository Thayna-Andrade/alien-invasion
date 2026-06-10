import pygame.font

class Scoreboard:
    """Exibe a pontuação e as melhores pontuações."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 36)

        self.prep_score()
        self.prep_high_scores()
        self.prep_level()

    def prep_score(self):
        score_str = f"Score: {self.stats.score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_scores(self):
        """Prepara as imagens das 3 melhores pontuações."""
        self.high_score_images = []
        self.high_score_rects = []
        
        for i, score in enumerate(self.stats.high_scores):
            score_str = f"Top {i+1}: {score:,}"
            image = self.small_font.render(score_str, True, self.text_color)
            rect = image.get_rect()
            rect.left = 20
            rect.top = 20 + (i * 40)
            
            self.high_score_images.append(image)
            self.high_score_rects.append(rect)

    def prep_level(self):
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        # Mostra as 3 melhores pontuações
        for image, rect in zip(self.high_score_images, self.high_score_rects):
            self.screen.blit(image, rect)

    def update_high_scores(self):
        """Atualiza a exibição das melhores pontuações."""
        self.prep_high_scores()