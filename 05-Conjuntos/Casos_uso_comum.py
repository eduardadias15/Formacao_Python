# 1. Remover duplicatas de uma lista
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 6, 8, 8]
sem_duplicatas = list(set(lista))    # → [1, 2, 3, 4, 6, 8] (ordem pode variar)


# 2. Verificar pertencimento rapidamente (muito mais rápido que lista)
palavras = {"python", "java", "go"}
"python" in palavras   # O(1) — muito eficiente!


# 3. Encontrar elementos únicos em comum
usuarios_a = {"ana", "bia", "carlos"}
usuarios_b = {"bia", "daniel", "carlos"}
em_comum = usuarios_a & usuarios_b  # → {"bia", "carlos"}