 # 🚀 Alien Invasion - Space Shooter Game

Um jogo clássico de tiro espacial desenvolvido em Python com Pygame, baseado no projeto do livro "Python Crash Course" de Eric Matthes.

## 📋 Sobre o Jogo

Você controla uma nave espacial na parte inferior da tela e deve destruir uma frota de aliens que desce em sua direção. O jogo fica progressivamente mais difícil à medida que você avança de nível, com aliens se movendo mais rapidamente.

### Características

- **Sistema de pontuação**: Ganhe pontos ao destruir aliens
- **Tabela de recordes**: As 3 melhores pontuações são salvas localmente
- **Progressão de dificuldade**: A velocidade aumenta a cada nível
- **Tela de Game Over**: Mostra sua pontuação final e os recordes
- **Sistema de vidas**: Você tem 1 nave por partida
- **Controles simples e responsivos**

## 🎮 Como Jogar

### Controles

| Tecla | Ação |
|-------|------|
| **←** (Seta Esquerda) | Move a nave para a esquerda |
| **→** (Seta Direita) | Move a nave para a direita |
| **ESPAÇO** | Dispara projéteis |
| **Q** | Sai do jogo |
| **Mouse** | Clique nos botões da interface |

### Regras

1. **Destrua os aliens** atirando neles com seus projéteis
2. **Evite colisões** com os aliens - cada colisão custa uma vida
3. **Não deixe os aliens** chegarem ao fundo da tela
4. **Complete uma leva** de aliens para avançar de nível
5. **O jogo termina** quando você perde todas as 3 naves

### Pontuação

- Pontuação base: 50 pontos por alien
- A cada nível, a pontuação por alien aumenta 50%
- Sua pontuação final é comparada com os 3 melhores recordes

## 🛠️ Requisitos

- Python 3.7 ou superior
- Pygame

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/alien-invasion.git
cd alien-invasion
```

### 2. Instale o Pygame

```bash
pip install pygame
```

### 3. Crie as imagens do jogo

Execute o script de criação de imagens (cria imagens simples da nave e alien):

```bash
python create_images.py
```

### 4. Execute o jogo

```bash
python alien_invasion.py
```

## 📁 Estrutura do Projeto

```
alien-invasion/
├── alien_invasion.py      # Arquivo principal do jogo
├── settings.py            # Configurações do jogo
├── game_stats.py          # Estatísticas e sistema de recordes
├── scoreboard.py          # Exibição de pontuações
├── ship.py                # Classe da nave
├── alien.py               # Classe dos aliens
├── bullet.py              # Classe dos projéteis
├── button.py              # Botões da interface
├── reset_scores.py        # Utilitário para resetar recordes
├── create_images.py       # Cria imagens padrão
├── images/                # Pasta com sprites do jogo
│   ├── ship.png           # Imagem da nave
│   └── alien.png          # Imagem do alien
└── high_scores.json       # Arquivo com os recordes (criado automaticamente)
```

## 🎯 Funcionalidades em Detalhe

### Sistema de Recordes

- As 3 melhores pontuações são salvas no arquivo `high_scores.json`
- Pontuações duplicadas são tratadas automaticamente
- Para resetar os recordes, execute: `python reset_scores.py`

### Progressão de Dificuldade

| Nível | Velocidade da Nave | Velocidade dos Aliens | Pontos por Alien |
|-------|-------------------|----------------------|------------------|
| 1     | 1.5               | 1.0                  | 50               |
| 2     | 1.65              | 1.1                  | 75               |
| 3     | 1.81              | 1.21                 | 112              |
| ...   | +10% por nível    | +10% por nível       | +50% por nível   |

### Interface

- **Tela inicial**: Botão "Play" para começar
- **Durante o jogo**: Pontuação atual, nível e top 3 recordes no canto superior
- **Game Over**: Tela escurecida mostrando sua pontuação, recordes e botão "Jogar Novamente"

## 🐛 Possíveis Problemas e Soluções

### "Não foi possível carregar images/ship.png"

Execute o script `create_images.py` para gerar as imagens padrão:

```bash
python create_images.py
```

### Erro "No module named 'pygame'"

Instale o Pygame com pip:

```bash
pip install pygame
```

### O jogo está muito rápido/lento

Ajuste os valores de velocidade no arquivo `settings.py`:
- `ship_speed`: Velocidade da nave
- `alien_speed`: Velocidade dos aliens  
- `bullet_speed`: Velocidade dos projéteis

## 🔧 Personalização

Você pode modificar vários aspectos do jogo editando o arquivo `settings.py`:

```python
# Configurações da tela
self.screen_width = 1200    # Largura da tela
self.screen_height = 800    # Altura da tela
self.ship_limit = 3         # Número de vidas

# Configurações do projétil
self.bullets_allowed = 3    # Máximo de balas na tela

# Dificuldade
self.speedup_scale = 1.1    # Aumento de velocidade por nível
```

## 📝 Créditos

- Projeto baseado no livro **"Python Crash Course"** de Eric Matthes
- Desenvolvido como exercício de aprendizado de Python e Pygame

## 📄 Licença

Este projeto é de uso livre para fins educacionais.

---

**Divirta-se e bom jogo!** 🚀👾
