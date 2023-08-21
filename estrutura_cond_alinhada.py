saldo = 1000.0
saldo_contaUniversatira = 1000.0
saque = 500.0
cheque_especial = 250.0
cheque_especial_universitaria = 200.0

while True:
    opcao = int(
        input(
            "Esolha o tipo de conta: \n[1] Conta correnta \n[2] Conta Universitaria \n[0] Encerrar atendimento \n"
        )
    )

    if opcao == 0:
        break

    if opcao == 1:
        print("Bem vindo a sua conta corrente!")
        valor_contaCorrente = float(input("Informa o valor para o Saque: "))
        if valor_contaCorrente <= saldo:
            print("Saque relizado com sucesso!")
        elif valor_contaCorrente <= (saldo + cheque_especial):
            print("Saque realizado com uso do cheque especial!")
        else:
            print("saldo insuficiente")
    # Fim do metodo conta corrente
    elif opcao == 2:
        print("Bem vindo a sua Universitaria!")
        valor_contaUniversitaria = float(input("Informa o valor para o Saque: "))
        if valor_contaUniversitaria <= saldo_contaUniversatira:
            print("Saque relizado com sucesso!")
        elif valor_contaUniversitaria <= (
            saldo_contaUniversatira + cheque_especial_universitaria
        ):
            print("Saque realizado com uso do cheque especial!")
        else:
            print("saldo insuficiente")
    if opcao > 2:
        print("Opção invalida, tente novamente!")
# Fim do metodo conta universitaria
print("Encerrando sistema!")
