## Métodos de listas - Parte 2
    # count() - conta quantas vezes um elemento aparece na lista

cores = ["vermelho", "azul", "rosa", "azul", "rosa", "verde"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
print(cores.count("rosa"))  # 2


## extend() - estende a lista com outra lista

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])


## index() - retorna o índice da primeira ocorrência do elemento

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0