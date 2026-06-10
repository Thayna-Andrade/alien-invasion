import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        
        self.screen_rect = self.screen.get_rect()

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")
        
        # Flag para controlar se estamos mostrando game over
        self.showing_game_over = False

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active and not self.showing_game_over:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_high_scores()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.stats.game_active and not self.showing_game_over:
                self._fire_bullet()
            elif self.showing_game_over:
                # Espaço recomeça o jogo na tela de game over
                self._restart_game()
        elif event.key == pygame.K_q:
            self.stats.save_high_scores()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        """Responde à colisão da nave com um alien."""
        if self.stats.game_active:
            # Marca que o jogo acabou
            self.stats.game_active = False
            self.showing_game_over = True
            
            # Salva a pontuação se for uma das melhores
            if self.stats.score > min(self.stats.high_scores):
                # Salva a pontuação se for uma das melhores
                self.stats.add_score(self.stats.score)
                self.sb.update_high_scores()
            
            # Mostra o mouse
            pygame.mouse.set_visible(True)
            
            # Pequena pausa para evitar cliques acidentais
            sleep(0.5)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        alien_height = alien.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_play_button(self, mouse_pos):
        """Inicia um novo jogo quando o jogador clicar no botão."""
        button_clicked = False
        
        # Se estiver mostrando game over, verifica o botão "Jogar Novamente"
        if self.showing_game_over and hasattr(self, 'play_again_button'):
            button_clicked = self.play_again_button.rect.collidepoint(mouse_pos)
        # Se não, verifica o botão "Play" inicial
        elif hasattr(self, 'play_button') and not self.stats.game_active:
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        
        if button_clicked:
            self._restart_game()

    def _restart_game(self):
        """Reinicia o jogo completamente."""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.showing_game_over = False

        # Limpa todos os sprites
        self.aliens.empty()
        self.bullets.empty()

        # Recria a frota e reposiciona a nave
        self._create_fleet()
        self.ship.center_ship()

        # Esconde o mouse durante o jogo
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        
        # SEMPRE desenha a nave, aliens e balas (mesmo no game over)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.aliens.draw(self.screen)
        
        # Se o jogo está ativo, mostra a pontuação normal
        if self.stats.game_active:
            self.sb.show_score()
        
        # Se não está mostrando game over e o jogo não está ativo, mostra tela inicial
        if not self.showing_game_over and not self.stats.game_active:
            self.play_button.draw_button()
        
        # Se está mostrando game over, desenha a tela de game over
        if self.showing_game_over:
            self._draw_game_over_screen()
    
        pygame.display.flip()

    def _draw_game_over_screen(self):
        """Desenha a tela de game over por cima do jogo."""
        # Fundo semitransparente escuro
        overlay = pygame.Surface((self.settings.screen_width, self.settings.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))  # Preto mais escuro e mais opaco
        self.screen.blit(overlay, (0, 0))
        
        # Título GAME OVER grande
        game_over_font = pygame.font.SysFont(None, 100)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 50, 50))
        game_over_rect = game_over_text.get_rect()
        game_over_rect.centerx = self.screen_rect.centerx
        game_over_rect.centery = self.screen_rect.centery - 180
        self.screen.blit(game_over_text, game_over_rect)
        
        # Pontuação final
        score_font = pygame.font.SysFont(None, 60)
        score_text = score_font.render(f"Pontuação Final: {self.stats.score:,}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.centerx = self.screen_rect.centerx
        score_rect.centery = self.screen_rect.centery - 80
        self.screen.blit(score_text, score_rect)
        
        # Título "Melhores Pontuações"
        highscores_title_font = pygame.font.SysFont(None, 48)
        highscores_title = highscores_title_font.render("Melhores Pontuações:", True, (255, 255, 255))
        highscores_title_rect = highscores_title.get_rect()
        highscores_title_rect.centerx = self.screen_rect.centerx
        highscores_title_rect.centery = self.screen_rect.centery
        self.screen.blit(highscores_title, highscores_title_rect)
        
        # Lista das 3 melhores pontuações
        highscores_font = pygame.font.SysFont(None, 40)
        for i, score in enumerate(self.stats.high_scores):
            color = (255, 215, 0) if score == self.stats.score else (255, 255, 255)  # Destaca pontuação atual
            score_text = highscores_font.render(f"{i+1}º: {score:,} pontos", True, color)
            score_rect = score_text.get_rect()
            score_rect.centerx = self.screen_rect.centerx
            score_rect.centery = self.screen_rect.centery + 50 + (i * 50)
            self.screen.blit(score_text, score_rect)
        
        # Botão "Jogar Novamente"
        self.play_again_button = Button(self, "Jogar Novamente", 
                                       (self.screen_rect.centerx, self.screen_rect.centery + 230))
        self.play_again_button.draw_button()
        
        # Instruções
        instructions_font = pygame.font.SysFont(None, 30)
        instructions = instructions_font.render("Clique em 'Jogar Novamente' ou pressione ESPAÇO", True, (200, 200, 200))
        instructions_rect = instructions.get_rect()
        instructions_rect.centerx = self.screen_rect.centerx
        instructions_rect.bottom = self.screen_rect.bottom - 40
        self.screen.blit(instructions, instructions_rect)
        
        instructions2 = instructions_font.render("Pressione Q para sair", True, (200, 200, 200))
        instructions2_rect = instructions2.get_rect()
        instructions2_rect.centerx = self.screen_rect.centerx
        instructions2_rect.bottom = self.screen_rect.bottom - 10
        self.screen.blit(instructions2, instructions2_rect)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()