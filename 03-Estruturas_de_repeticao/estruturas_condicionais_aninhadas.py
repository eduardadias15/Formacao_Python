conta_normal = False
conta_universitária = True

saldo = 2000
saque = 500
cheque_especial= 1000

if conta_normal:
    if saldo >= saque:
        print("saque realizado, com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print ("saque realizado usando o cheque especial.")
    else:
        print("não foi possivel realizar o saque, saldo infuficiente.")
elif conta_universitária:
    if saldo >= saque:
        print("saque realizado com sucesso.")
    else: 
        print("não foi possivel realizar o saque, saldo insuficiente.")
