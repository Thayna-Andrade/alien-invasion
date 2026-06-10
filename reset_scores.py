# reset_scores.py
import json

# Reseta as pontuações para [0, 0, 0]
with open('high_scores.json', 'w') as f:
    json.dump([0, 0, 0], f)

print("✅ Pontuações resetadas para [0, 0, 0]")