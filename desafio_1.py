menu = '''
[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

==>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falou o valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falou! você não tem saldo suficiente.")

        elif excedeu_limite:
            print("operação falhou! o valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("operação falhou! numero maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("operação falou! valor invalido")

    elif opcao == "e":
        print("\n__________________________\n")
        if extrato:
            print(extrato)
        else:    
            print("Não tem movimentação da conta")
        print(f"\nsaldo atual {saldo:.2f}")
        print("\n__________________________\n")

    elif opcao == "q":
        break

    else:
        print("opeção errada.")


