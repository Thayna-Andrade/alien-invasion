import json
import os

class GameStats:
    """Acompanha estatísticas do jogo."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        
        # Carrega as melhores pontuações
        self.high_scores = [0, 0, 0]
        self._load_high_scores()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_scores(self):
        """Carrega as 3 melhores pontuações do arquivo."""
        try:
            with open('high_scores.json', 'r') as f:
                loaded_scores = json.load(f)
                # Garante que temos exatamente 3 pontuações
                if isinstance(loaded_scores, list):
                    # Pega apenas os 3 primeiros valores únicos
                    unique_scores = []
                    for score in loaded_scores:
                        if score not in unique_scores:
                            unique_scores.append(score)
                    
                    # Preenche com zeros se necessário
                    while len(unique_scores) < 3:
                        unique_scores.append(0)
                    
                    # Ordena em ordem decrescente e pega apenas 3
                    unique_scores.sort(reverse=True)
                    self.high_scores = unique_scores[:3]
                else:
                    self.high_scores = [0, 0, 0]
                    
            print(f"✅ Pontuações carregadas: {self.high_scores}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("ℹ️ Nenhum arquivo de pontuações encontrado, usando padrão")
            self.high_scores = [0, 0, 0]

    def save_high_scores(self):
        """Salva as 3 melhores pontuações no arquivo."""
        try:
            with open('high_scores.json', 'w') as f:
                json.dump(self.high_scores, f)
            print(f"💾 Pontuações salvas: {self.high_scores}")
        except Exception as e:
            print(f"❌ Erro ao salvar pontuações: {e}")

    def add_score(self, new_score):
        """Adiciona uma pontuação à lista de melhores, evitando duplicatas."""
        print(f"🎯 Nova pontuação: {new_score}")
        print(f"📊 Melhores atuais: {self.high_scores}")
        
        # Só adiciona se a pontuação for maior que a menor das melhores
        if new_score > min(self.high_scores):
            # Remove duplicatas da nova pontuação (se já existir)
            if new_score in self.high_scores:
                print(f"⚠️ Pontuação {new_score} já existe, removendo duplicata")
                self.high_scores.remove(new_score)
            
            # Adiciona a nova pontuação
            self.high_scores.append(new_score)
            
            # Ordena em ordem decrescente
            self.high_scores.sort(reverse=True)
            
            # Mantém apenas as 3 melhores
            self.high_scores = self.high_scores[:3]
            
            print(f"🔄 Melhores atualizadas: {self.high_scores}")
            
            # Salva no arquivo
            self.save_high_scores()
        else:
            print(f"📉 Pontuação {new_score} não é maior que {min(self.high_scores)}, ignorando")