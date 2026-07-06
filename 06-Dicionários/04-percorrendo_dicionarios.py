d = {"nome": "Ana", "idade": 30, "cidade": "SP"}

# Iterar sobre chaves
for chave in d:
    print(chave)

# Iterar sobre valores
for valor in d.values():
    print(valor)

# Iterar sobre pares chave-valor ✅ mais comum
for chave, valor in d.items():
    print(f"{chave}: {valor}")