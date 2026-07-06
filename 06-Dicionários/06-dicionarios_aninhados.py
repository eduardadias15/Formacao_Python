usuarios = {
    "ana": {"idade": 30, "cargo": "dev"},
    "bia": {"idade": 25, "cargo": "design"},
}

# Acessando valor aninhado
usuarios["ana"]["cargo"]   # → "dev"

# Percorrendo
for nome, dados in usuarios.items():
    print(f"{nome} — {dados['cargo']}")