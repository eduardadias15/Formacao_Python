Saldo = 2000
Saque = 500

status = "sucesso" if Saldo >= Saque else "Falha"

print (f"saque realizado com {status}.")