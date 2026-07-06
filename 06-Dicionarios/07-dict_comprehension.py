# Sintaxe: {chave: valor for item in iterável}

# Quadrados de 1 a 5
quadrados = {n: n**2 for n in range(1, 6)}
# → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrar dicionário
precos = {"maçã": 3, "banana": 1, "uva": 8}
caros = {k: v for k, v in precos.items() if v > 2}
# → {"maçã": 3, "uva": 8}

# Inverter chave e valor
invertido = {v: k for k, v in precos.items()}