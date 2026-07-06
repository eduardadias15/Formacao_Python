d = {"a": 1, "b": 2, "c": 3, "d": 4}

d.keys()     # → dict_keys(["a", "b", "c", "d"])
d.values()   # → dict_values([1, 2, 3, 4])
d.items()    # → dict_items([("a",1), ("b",2), ("c",3), ("d",4)])

len(d)       # → 4 (número de chaves)
"a" in d     # → True  (verifica chave)
1 in d.values()  # → True (verifica valor)

# Copia
d.copy()         # Cópia rasa (shallow)