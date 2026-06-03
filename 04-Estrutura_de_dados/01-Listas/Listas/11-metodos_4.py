## Métodos de listas - Parte 3
    # pop() - remove e retorna o último elemento da lista (ou o elemento no índice

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5


# pop() - remove e retorna o último elemento da lista (ou o elemento no índice)

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]