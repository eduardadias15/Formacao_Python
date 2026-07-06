pessoa = {"nome": "Ana", "idade": 30}

# Acesso direto (erro se chave não existir)
pessoa["nome"]          # → "Ana"

# .get() — seguro, retorna None se não existir
pessoa.get("cidade")        # → None
pessoa.get("cidade", "BR")  # → "BR"  (valor padrão)

print(pessoa["nome"])
print(pessoa.get("cidade"))