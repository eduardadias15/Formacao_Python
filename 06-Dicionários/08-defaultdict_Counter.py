from collections import defaultdict, Counter

# defaultdict — valor padrão automático para chaves novas
contagem = defaultdict(int)
for letra in "banana":
    contagem[letra] += 1
# → {"b":1, "a":3, "n":2}

# Counter — conta elementos automaticamente
c = Counter("banana")
# → Counter({"a":3, "n":2, "b":1})
c.most_common(2)  # → [("a", 3), ("n", 2)]