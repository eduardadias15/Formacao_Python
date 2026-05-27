# Operadores lógicos combinam ou invertem valores booleanos (True/False)
# Python possui 3 operadores lógicos principais:

# and   # True somente se AMBOS forem True
# or    # True se PELO MENOS UM for True
# not   # Inverte o valor (True vira False, False vira True)

# AND — retorna True apenas quando os dois lados são True

tem_conta    = True
tem_saldo    = True
pode_pagar   = tem_conta and tem_saldo
print(pode_pagar)   # True

tem_conta    = True
tem_saldo    = False
pode_pagar   = tem_conta and tem_saldo
print(pode_pagar)   # False — saldo insuficiente


# OR — retorna True quando pelo menos um lado é True

tem_wifi     = False
tem_dados    = True
tem_internet = tem_wifi or tem_dados
print(tem_internet)  # True — dados móveis salva

tem_wifi     = False
tem_dados    = False
tem_internet = tem_wifi or tem_dados
print(tem_internet)  # False — sem conexão

# NOT — inverte o valor booleano

logado       = False
nao_logado   = not logado
print(nao_logado)    # True

logado       = True
nao_logado   = not logado
print(nao_logado)    # False


# Exemplo prático: sistema de login com verificação de acesso

usuario_valido = True
senha_correta  = True
conta_bloqueada = False

pode_entrar = (usuario_valido and senha_correta) and not conta_bloqueada
print(pode_entrar)   # True — acesso liberado

conta_bloqueada = True
pode_entrar = (usuario_valido and senha_correta) and not conta_bloqueada
print(pode_entrar)   # False — conta bloqueada

# Uso com if:
if pode_entrar:
    print("Bem-vindo ao sistema!")
else:
    print("Acesso negado.")