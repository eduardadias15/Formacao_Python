a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

# Merge com |
c = a | b       # → {"x": 1, "y": 99, "z": 3}

# Atualizar no lugar
a |= b