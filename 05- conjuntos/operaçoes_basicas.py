numeros = {1, 2, 3, 4, 5, 6}

numeros.add(4)          # Adiciona (sem erro se já existir)
numeros.remove(2)       # Remove (erro se não existir)
numeros.discard(99)     # Remove sem erro se não existir
numeros.pop()           # Remove e retorna um elemento aleatório
numeros.clear()         # Esvazia o set

len(numeros)            # Tamanho
3 in numeros            # Verifica pertencimento → True/False