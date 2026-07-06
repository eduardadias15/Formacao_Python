d = {"a": 1, "b": 2}

# Adicionar ou atualizar
d["c"] = 3           # → {"a": 1, "b": 2, "c": 3}
d["a"] = 99          # → atualiza "a" para 99

# Atualizar com outro dicionário
d.update({"b": 20, "d": 4})

# Remover
del d["a"]           # Remove a chave (erro se não existir)
d.pop("b")           # Remove e retorna o valor
d.pop("z", None)     # Remove sem erro se não existir
d.popitem()          # Remove e retorna o último par inserido
d.clear()            # Esvazia o dicionário