## Métodos de listas - Parte 3
    # pop() - remove e retorna o último elemento da lista (ou o elemento no índice


linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python



## remove() - remove a primeira ocorrência do elemento

linguagens = ["python", "javas", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "javas", "java", "csharp"]



## reverse() - inverte a ordem dos elementos da lista

linguagens = ["python", "javas", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "javas", "python"]